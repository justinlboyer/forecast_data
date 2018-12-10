import requests
import json
import pandas as pd

#%%

ws_url = 'https://api.weather.gov/gridpoints/OKX/32,34/forecast/hourly'


def get_data(url):
    headers = {'accept': 'application/geo+json'}
    response = requests.get(url, headers=headers)
    jData = json.loads(response.text)
    data = pd.read_json(json.dumps(jData['properties']['periods']))
    return data

