
import requests 
from requests.sessions import Request
S = requests.Session()

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f"Name: {name}, Email: {email}"



URL = "http://www.songsterr.com/a/wa/bestMatchForQueryString"

PARAMS = {'s':'New Light', 'a':'John Mayer', 'inst': 'guitar'}

R = S.get(url=URL, params=PARAMS)
print(R.content)



if __name__ == '__main__':
    app.run(debug=True)