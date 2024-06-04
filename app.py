from flask import Flask, request, jsonify, render_template
import pyttsx3
import requests
import os

app = Flask(__name__)

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather_data(data, city):
    if data:
        current = data["current"]
        temp = current["temp_c"]
        condition = current["condition"]["text"]
        return f"The temperature of {city} is {temp}°C with {condition}"
    else:
        return "Not valid"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    city = request.form['city']
    api_key = os.getenv('WEATHER_API_KEY', '683dfb79bd1749f89e4144310240206')  # Replace with your actual API key or use environment variable
    weather = get_weather(api_key, city)
    report = get_weather_data(weather, city)
    return jsonify(report=report)

if __name__ == "__main__":
    app.run(debug=True)
