import requests
from datetime import datetime
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm.m@tesco.com'


# Time is returned in unix, UTC and needs to be converted to 'readable format'


@app.route('/WEATHER')
def welcome():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Leeds&APPID=c024e85cef8f0fc928c3f0ef85d7ad00&units=metric'
    res = requests.get(url)
    data = res.json()
    time_format = '%H:%M:%S'
    temp = str(data['main']['temp_max'])

    time = str(datetime.utcfromtimestamp(data['sys']['sunset']).strftime(time_format))
    print('temp ' + temp)
    print('time ' + time)
    return jsonify({'Max Temperature': temp}, {'Sunset Time': time})


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

# http://api.openweathermap.org/data/2.5/weather?q=Leeds&APPID=c024e85cef8f0fc928c3f0ef85d7ad00  😊
# Authenticate using (A HS256 algorithm JWT
# JSON payload to contain the max temperature in Degrees C and time in readable format for the sunset.

# Key parts secretKey = m.m@tesco.com
# existingToken =
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.YVzW_1pwHsk912nHWQsSBofXU10vAQqOI4BYQV2weNo
