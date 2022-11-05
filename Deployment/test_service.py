# You can upload images in https://postimages.org/
import requests
import json

data = {'url': "https://i.postimg.cc/pX0LpQ4t/shorts.jpg"}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=data)
result = response.json()

print(json.dumps(result, indent=2))
