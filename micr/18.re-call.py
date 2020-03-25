import requests
import json

response = requests.get('https://lolm.noway.vip/web/api/ads/list')
results = response.json()

print(json.dumps(results))