import requests
import random

'''for i in range(1000000):
    i = i + 1
    url = "http://127.0.0.1:5000/"
    payload = {
        "title": i,
        "desc": i
    }
    r = requests.post(url, data=payload)
    print(r.status_code)'''

for i in range(255):
    i = 2000 + 1
    url = f"http://127.0.0.1:5000/delete/{i}"
    print(requests.get(url).status_code)