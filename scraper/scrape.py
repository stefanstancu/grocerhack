import os
import requests as r
from string import ascii_uppercase

url_base = 'https://www.loblaws.ca/api/product/'
headers = {
     #'Host':'www.loblaws.ca',
     #'Connection':'keep-alive',
     #'Pickup-Location-Id':'1000',
     'Site-Banner':'loblaw',
     #'Accept-Language':'en',
     #'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
     #'Content-Type':'application/json;charset=utf-8',
     #'Accept':'application/json, text/plain, */*',
     #'ADRUM':'isAjax:true',
     #'Accept-Encoding':'gzip, deflate, br',
     # 'Cookie':'loblaw-cart=c9d0af30-91be-4e72-a356-081fac0c5477;' #ADRUM=s=1554327425433&r=https%3A%2F%2Fwww.loblaws.ca%2FFood%2FMeat-%2526-Seafood%2FBeef-%2526-Veal%2FOffal-%2526-Other-Cuts%2FBeef-Kidney%2Fp%20599701_EA;'
}
letter_endings = [
        'KG',
        'EA',
        ]

starting_int = 20060000
starting_int = 20062633

for i in range(starting_int, 21000000):
    for ending in letter_endings:
        url = url_base + str(i) + "_" + ending 
        resp = r.get(url, headers=headers).json()
        if 'code' in resp:
            print('found ' + resp['name'])
            with open('codes.txt', 'a+') as f:
                f.write(resp['code'] + "\n")

