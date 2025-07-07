from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "26300f19ae7845dbbd372940250707"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "icon": data["current"]["condition"]["icon"]
            }
        else:
            error = "City not found or API error."

    return render_template('weather.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
