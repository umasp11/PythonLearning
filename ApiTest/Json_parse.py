import requests
import jsonpath
import json

url='https://reqres.in/api/users?page=2'

response=requests.get(url)

#parse response to json format
json_response= json.loads(response.text)
print(json_response)

#Fetch value using jsonpath
pages= jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])




