
from flask import Flask, jsonify, render_template, request
import requests, finnhub

app = Flask(__name__)

POLYGON_API_KEY = 'ZNcFikpUii72nVpvjRw24JH1FVXAZCJ6'

'''finnhub API Key'''
finnhub_client = finnhub.Client(api_key="cr6er1pr01qnuep5kdb0cr6er1pr01qnuep5kdbg")
finnhub_key = 'cr6er1pr01qnuep5kdb0cr6er1pr01qnuep5kdbg'



@app.route('/get_company_profile/<symbol>')
def get_company_profile(symbol):
    profile = finnhub_client.company_profile2(symbol=symbol)
    return jsonify(profile)

# def get_stock_data(symbol):
#     '''
#     Function to return stock information for user input
#     '''
#     url = f"https://api.polygon.io/v1/last/stocks/{symbol}?apiKey={POLYGON_API_KEY}"
#     response = requests.get(url)
#     return response.json()

# @app.route('/stock/<symbol>', methods=['GET'])
# def stock_info(symbol):
#     symbol = request.args.get('symbol')
#     data = None
#     if symbol:
#         data = get_stock_data(symbol)
#     return render_template('home.html', data=data, symbol=symbol)

def get_stock_data(symbol):
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


@app.route('/stock', methods=['GET'])
def stock_info():
    symbol = request.args.get('symbol')
    data = None
    if symbol:
        data = get_stock_data(symbol)
    return render_template('home2.html', data=data, symbol=symbol)

@app.route('/')
def index():
    '''
    This is the base route to load the homepage
    '''
    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug=True)
