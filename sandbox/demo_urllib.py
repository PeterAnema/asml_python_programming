import urllib.request
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=eindhoven&appid=d1526a9039658a6f76950cff21823aff&units=metric'

with urllib.request.urlopen(url) as f:
    print(f.read())

    print('The temperature is ')