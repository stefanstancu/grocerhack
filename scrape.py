import requests as r

test_url = 'https://www.loblaws.ca/api/product/20599700_EA'
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
     'Cookie':'ADRUM=s=1554327425433&r=https%3A%2F%2Fwww.loblaws.ca%2FFood%2FMeat-%2526-Seafood%2FBeef-%2526-Veal%2FOffal-%2526-Other-Cuts%2FBeef-Kidney%2Fp%20599700_EA%3F0; loblaw-cart=c9d0af30-91be-4e72-a356-081fac0c5477;'
}

item = r.get(test_url, headers=headers).json()

print(item)

