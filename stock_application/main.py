
from flask import Flask, jsonify, render_template, request
import requests, sqlite3
import finnhub
from abc import ABC, abstractmethod #used for class structure
from enum import Enum #used for environments

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

'''If user does not exist add to the database'''



class stockdata(ABC):
    '''Base Class'''
    @abstractmethod
    def get_stock_data(self, symbol):
        pass

class finnhub_data(stockdata):
    '''Inherits from Base Class, returns real data from API'''
    def __init__(self, api_key):
        self.api_key = api_key

    def get_stock_data(self, symbol):
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={finnhub_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get('c') is not None:
                return data
            else:
                print("No valid data returned for symbol: ", symbol)
                return None
        else:
            print("Error: ", response.status_code, response.text)

class mock_data(stockdata):
    '''Inherits from Base Class, returns mock data'''

    def get_stock_data(self, symbol):
        '''return data for demonstration'''
        return {
            "c": 100.0,
            "h": 110.0,
            "l": 90.0,
            "o": 95.0,
            "pc": 98.0
        }
      
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
    return render_template('home2.html', data=data, symbol=symbol)

@app.route('/')
def index():
    '''
    This is the base route to load the homepage
    '''
    return render_template('home2.html')

'''Global variable for environment'''
data_provider = None

def main():
    '''Here we define which environment we are in, production environment calls API
    while mock environment only returns static data'''

    global data_provider
    ENV = ENVIRONMENT.PRODUCTION
    #Initialize teh data provider based on environment
    data_provider = stock_data_provider(ENV)


if __name__ == '__main__':
    main()
    app.run(debug=True)
