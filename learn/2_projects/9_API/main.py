import datetime as dt
import requests # pip install requests
import password 

base_url = 'http://api.openweathermap.org/data/2.5/forecast?'

city = "Szczecin"

try:
    url = base_url + "appid=" + password.api_key + "&q=" + city
    response = requests.get(url).json()
    print(response)
except requests.exceptions.HTTPError as e:
    print("wrong connectrion result: {0}".format(e))
    exit(0)



