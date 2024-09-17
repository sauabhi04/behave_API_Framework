import json

import requests

response = requests.get("https://gorest.co.in/public/v2/users/6940794")

print(json.dumps(response.json(), indent=4))