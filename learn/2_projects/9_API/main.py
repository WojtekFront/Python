import datetime as dt
import requests # pip install requests
import password # external file with password

api_key = password.api_key
city_name = "Szczecin"

def kelvin_to_celsius(kelvin):
    ''' Convert the given kelvin to celsius'''
    celsius = kelvin - 273.15
    return int(celsius) # I don't know what rounding is used in the weather forecast

try:
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
except requests.exceptions.HTTPError as e:
    print("wrong connectrion result: {0}".format(e))
    exit(0)

if response.status_code == 200:
    # collect data
    temp_in_celsius = kelvin_to_celsius(data['main']['temp'])
    feels_like_celsius = kelvin_to_celsius(data['main']['feels_like'])
    sunrise_time = dt.datetime.fromtimestamp(data['sys']['sunrise'])
    # print(data)

    # response data
    print("temperatura dzisiaj:      {0} C".format(temp_in_celsius))
    print("odczuwalna temperatura:   {0} C".format(feels_like_celsius))
    print("wschód słońca o godzinie :{0}".format(sunrise_time))




