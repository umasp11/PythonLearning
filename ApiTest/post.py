import requests
import json


url= 'https://reqres.in/api/users'

#Read json file
f= open("C:\Users\umasankar.panigrahy\Desktop\Docker\PM\CreateData.json", 'r')
read=f.read()
request_json= json.loads(read)         #parse the data in json format

#Make post request with json input body
response = requests.post(url, request_json)
assert response.status_code==201
print(response.content)

