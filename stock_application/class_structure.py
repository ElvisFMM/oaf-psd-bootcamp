import requests
from abc import ABC, abstractmethod
import finnhub, requests, sqlite3


'''finnhub API Key'''
finnhub_client = finnhub.Client(api_key="crb6ae9r01qo7cafvcbgcrb6ae9r01qo7cafvcc0")
finnhub_key = 'crb6ae9r01qo7cafvcbgcrb6ae9r01qo7cafvcc0'


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