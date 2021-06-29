import requests
import jsonpath
import json

def test_add_new_data():
    url='http://the testingworldapi.com/api/studentdetails'
    f=open("C:\Users\umasankar.panigrahy\Desktop\Docker\PM\CreateData.json", 'r')
    read=json.loads(f.read())
    response=json.post(url,read)
    name=jsonpath.jsonpath(response.json(), 'id')