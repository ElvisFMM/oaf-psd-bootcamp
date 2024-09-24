
import openmeteo_requests
import requests_cache
import pandas as pd
import matplotlib.pyplot as plt
from retry_requests import retry


'''establish the connection to url and retrieve data'''
class builder:

    def __init__(self, cache_dir='.cahce', cache_expire_after=3600):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession(cache_dir, expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.client = openmeteo_requests.Client(session = retry_session)
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    def get_weather_data(self, latitude, longitude, variables):
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": "temperature_2m"
        }
        responses = self.client.weather_api(self.base_url, params=params)
        return responses[0]
    

    def get_hourly_temp(self, latitude, longitude):
        # Process first location. Add a for-loop for multiple locations or weather models
        response = self.get_weather_data(latitude, longitude, "temperature_2m")

        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        print(hourly_dataframe)

        return hourly_dataframe


# class weatherservice:

#     def __init__(self, weather_service):
#         self.weather_service = weather_service

#     def get_hourly_temp(self, latitude, longitude):
#         response - self.weather_




class handler:

    def __init__(self, weather_service):
        self.weather_service = weather_service

    def plot_hourly_temp(self, df):
        plt.figure(figsize=(10, 5))
        plt.plot(df['date'], df['temperature_2m'], marker='o')
        plt.title('Hourly Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":

    #initialize
    weather_service = builder()
    weather_handler = handler(weather_service)

    latitude = 52.52
    longitude = 13.41

    hourly_dataframe = weather_service.get_hourly_temp(latitude, longitude)
    
    weather_handler.plot_hourly_temp(hourly_dataframe)