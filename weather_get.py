import requests
import json

r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
print(json.loads(r.content))
