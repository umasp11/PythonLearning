import requests

r=requests.get('https://the-internet.herokuapp.com/basic-auth', auth=('admin','admin'))
print(r.status_codes)