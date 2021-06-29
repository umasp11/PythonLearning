import requests

url='https://reqres.in/api/users?page=2'

#Get request
req=requests.get(url)
print(req)                          #OP will be 200
code= req.status_code
assert code==200

#display contenet of get request
req=requests.get(url)
print(req.content)

