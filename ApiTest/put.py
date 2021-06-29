import requests
import json


url= 'https://reqres.in/api/users/2'

#Read json file
f= open("C:\Users\umasankar.panigrahy\Desktop\Docker\PM\CreateData.json", 'r')
read=f.read()
request_json= json.loads(read)         #parse the data in json format

#Make PUT request with json input body
response = requests.put(url, request_json)
assert response.status_code==200
print(response.content)
