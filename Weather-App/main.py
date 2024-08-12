'''
main app to fetch data
'''

from flask import Flask, render_template, request, redirect, url_for
from weather import fetchWeather, weatherdata


#start html
@app.route('/')
def index():
    return render_template('main.html')

#get data
@app.route('/get_weather', methods=['POST'])

def get_weather():
    city = request.form.get('city')
    api_key = 'your_api_key'
    weather_service = fetchWeather(api_key)

    data = weather_service.fetch_data(city)
    temperature = data.get('temperature')
    humidity = data.get('humidity')
