from flask import Flask, jsonify, render_template, request, redirect, url_for
import finnhub, requests, sqlite3
from abc import ABC, abstractmethod #used for class structure
from enum import Enum #used for environments
from werkzeug.security import generate_password_hash, check_password_hash # used for login feature
from class_structure import stockdata, finnhub_data, mock_data

app = Flask(__name__)


'''finnhub API Key'''
finnhub_client = finnhub.Client(api_key="crb6ae9r01qo7cafvcbgcrb6ae9r01qo7cafvcc0")
finnhub_key = 'crb6ae9r01qo7cafvcbgcrb6ae9r01qo7cafvcc0'


class ENVIRONMENT(Enum):
    MOCK = 1
    PRODUCTION = 2


'''Login Database'''
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS login_info(
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            )
            ''')
conn.commit()
conn.close()

    

@app.route('/', methods=['GET', 'POST'])
def login():
    '''login function to read in inputs
    and store new users into database'''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login_info WHERE username=?', (username,))
        user = cursor.fetchone()

        if user:
            '''check the password'''
            if check_password_hash(user[2], password):
                return redirect(url_for('index'))
            else:
                return "invalid password or username", 401
            
        else:
            '''create new user'''
            password_hash = generate_password_hash(password)
            cursor.execute('INSERT INTO login_info (username, password_hash) VALUES (?, ?)', (username, password_hash))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        

    return render_template('login.html')
            
        

def stock_data_provider(env):
    '''factory funciton for environment'''
    if env == ENVIRONMENT.MOCK:
        return mock_data()
    elif env == ENVIRONMENT.PRODUCTION:
        return finnhub_data(api_key = finnhub_key)
    else:
        raise ValueError("Unknown Environment")



@app.route('/get_company_profile/<symbol>')
def get_company_profile(symbol):
    profile = finnhub_client.company_profile2(symbol=symbol)
    return jsonify(profile)


@app.route('/stock', methods=['GET'])
def stock_info():
    '''Returns stock information through a API call'''
    symbol = request.args.get('symbol')
    data = None
    if symbol:
        data = data_provider.get_stock_data(symbol) #needed to reference global variable
    return render_template('home.html', data=data, symbol=symbol)

@app.route('/afterlogin')
def index():
    '''
    This is the base route to load the homepage
    '''
    return render_template('home.html')

'''Global variable for environment'''
data_provider = None

def main():
    '''Here we define which environment we are in, production environment calls API
    while mock environment only returns static data'''

    global data_provider
    ENV = ENVIRONMENT.PRODUCTION #change PRODUCTION TO MOCK if you want the mock environment
    #Initialize teh data provider based on environment
    data_provider = stock_data_provider(ENV)


if __name__ == '__main__':
    main()
    app.run(debug=True)
