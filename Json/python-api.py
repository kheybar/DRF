from urllib.request import urlopen
import json


url = 'https://api.exchangeratesapi.io/latest'


with urlopen(url) as f:
    data = f.read()

python_data = json.loads(data)

with open('python-api-result.js', 'w') as c:
    json.dump(python_data, c, indent=2)
