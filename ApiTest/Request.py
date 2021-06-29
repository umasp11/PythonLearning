import requests
import json


#get request
url= 'https://reqres.in/api/users/2'
resp= requests.get(url)
json_resp=resp.json()
print(json_resp['total'])
assert (json_resp['total'])==12
print(json_resp['data'][0]['email'])

#post req
url='abc.com'
data= {'name':'uma', 'id':11, 'address':'delhi'}
post_req=requests.post(url,data)
print(post_req.json())

#put/patch:
#All properties of the object to be provided while making request. wnat to change addres syntax: {'name':'uma', 'id':11, 'address':'puri'}
#if record exist-it will update/replace. If record doent exist, it will create the data
# Patch: specifies only the properties that you want to update syntax: {'address':'puri'}