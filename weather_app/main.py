import requests
import json

city = input("enter city name")
url=f"https://api.weatherapi.com/v1/current.json?key=a70d6afa93164ced9db173958241206&q={city}"
r =requests.get(url)
print(r.text)
dic =json.loads(r.text)
print(dic["current"]["temp_c"])
