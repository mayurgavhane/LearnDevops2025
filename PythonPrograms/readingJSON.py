import json
import requests

response = requests.get=('http://api.open-notify.org/astros.json')
FileName = "data.json"
dataJSON = json.load(FileName)

print (dataJSON)