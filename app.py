from datetime import datetime
from flask import Flask, request, make_response, jsonify, Response, render_template

import jwt
import requests

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm.m@tesco.com'
app.config['TOKEN'] = 'm.m@tesco.com'


@app.route('/')
def welcome():
    print('Please provide key: ')
    encoded_jwt_key = input()

    print('Please provide token: ')
    encoded_jwt_token = input()

    authorise(encoded_jwt_key, encoded_jwt_token)
    return "hello"


@app.route('/weather', methods=['HEAD'])
def weather():
    authorization = request.headers.get("AUTHORIZATION")
    print("authorization " + authorization)

    return render_template('weather.html')


def authorise(key, token):
    decoded_jwt = jwt.decode(token, key, 'HS256')

    url_address = 'http://api.openweathermap.org/data/2.5/weather'
    query = '?q='
    location = decoded_jwt['location']
    app_id_prefix = '&APPID='
    application_id = decoded_jwt['appID']
    temp_cel = '&units=metric'

    url = url_address + query + location + app_id_prefix + application_id + temp_cel

    res = requests.get(url)
    data = res.json()
    time_format = '%H:%M:%S'
    temp = str(data['main']['temp_max']) + ' C'
    time = str(datetime.utcfromtimestamp(data['sys']['sunset']).strftime(time_format))
    return jsonify({'Max Temperature': temp, 'Sunset Time': time})


if __name__ == '__main__':
    app.run(debug=True)
