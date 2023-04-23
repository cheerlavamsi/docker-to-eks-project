import json
import requests

url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q":"Girls"}

response = requests.get(url, params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")