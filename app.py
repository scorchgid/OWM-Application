from datetime import datetime
from flask import Flask, request, make_response, jsonify, Response, render_template

import jwt
import requests

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm.m@tesco.com'


@app.route('/')
def welcome():
    print('Please provide key: ')
    encoded_jwt_key = input()
    print('Please provide token: ')
    encoded_jwt_token = input()
    return get_weather_data(encoded_jwt_key, encoded_jwt_token)


@app.route('/weather', methods=['HEAD'])
def weather():
    authorization = request.headers.get("AUTHORIZATION")
    return render_template('weather.html')
    # return render_template('weather.html',)
    #jsonify({'Message': 'Token is missing or invalid'}

    # Check if bearer is undefined
    # if type(authorization) != 'str':
    auth = request.authorization
    if auth and auth.password == app.config['SECRET_KEY']:
        token = authorization.replace("Bearer ", "")
        # r = requests.post()
        print(get_weather_data(app.config['SECRET_KEY'], token))

    else:
        make_response(render_template('weather.html'), 401)

    return render_template('weather.html')


def get_weather_data(key, token):
    decoded_jwt = decode(key, token)
    url = url_builder(decoded_jwt)
    data = open_weather_retrieval(url)
    return configure_data(data, decoded_jwt)


def decode(key, token):
    decoded_jwt = jwt.decode(token, key, 'HS256')
    return decoded_jwt
    # print("Unable to decode provided jwt. Key" + key + " Token: " + token)


def url_builder(decoded_jwt):
    url_address = 'http://api.openweathermap.org/data/2.5/weather'
    query = '?q='
    location = decoded_jwt['location']
    app_id_prefix = '&APPID='
    application_id = decoded_jwt['appID']
    temp_cel = '&units=metric'
    url = url_address + query + location + app_id_prefix + application_id + temp_cel
    return url


def open_weather_retrieval(url):
    res = requests.get(url)
    data = res.json()
    return data


def configure_data(data, decoded_jwt):
    time_format = '%H:%M:%S'
    temp = str(data['main']['temp_max']) + ' C'
    time = str(datetime.utcfromtimestamp(data['sys']['sunset']).strftime(time_format))
    location = decoded_jwt['location']
    return jsonify({
        "Location": location,
        "data":
            {'Max Temperature': temp, 'Sunset Time': time}
    })


if __name__ == '__main__':
    app.run()
