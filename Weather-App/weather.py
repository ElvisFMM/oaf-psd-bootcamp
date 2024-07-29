'''
Class structure to fetch data
'''

class fetchWeather:
    '''fetch weather data'''

    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_data(self, city: str) -> dict:
        
        '''test input'''
        if not isinstance(city, str):
            raise TypeError("City name must be valid.")
        
        pass

class weatherdata(fetchWeather):

    def __init__(self, temperature: float, humidity: float):
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%"

    pass

