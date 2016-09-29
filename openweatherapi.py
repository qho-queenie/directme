import requests
import pprint

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=San+Jose&APPID=86487cba59a4c9fbbbcc3f25e61690f3")

search = (response.json())

weather = search['weather'][0]['main']

temp = (search['main']['temp']) * (9/5.0) - 459.67

pprint.pprint(temp)
pprint.pprint(weather)
