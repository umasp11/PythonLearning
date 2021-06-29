import requests
import json

r=requests.get('https://httpbin.org/delay/10',timeout=5)        #delay is 10 sec, error will give after 5 sec
print(r.status_code)