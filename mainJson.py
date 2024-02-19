import requests
import json

r = requests.get("https://dummyjson.com/products/1")
res = r.json()

print(json.dumps(res, indent=4))
