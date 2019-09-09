import jwt
import requests
from datetime import datetime
from flask import Flask, request, make_response, jsonify

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm.m@tesco.com'


@app.route('/WEATHER')
def welcome():
    print('Please provide key: ')
    encoded_jwt = input()
    decoded_jwt = jwt.decode(encoded_jwt, app.config['SECRET_KEY'], 'HS256')
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


@app.route('/WEATHER', methods=['HEAD'])
def weather():
    return 'Weather will go here'


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        return ''
    return make_response('Could not verify', 401, {'WWW-Authenticate': "Basic realm=Login Required"})


if __name__ == '__main__':
    app.run(debug=True)
