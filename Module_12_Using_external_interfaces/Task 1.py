import requests
import json

request = requests.get("https://api.chucknorris.io/jokes/random")
response = request.json()
print(json.dumps(response["value"], indent=4))