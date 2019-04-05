import sys
import requests as r
from string import ascii_uppercase


url_base = 'https://www.loblaws.ca/api/product/'
headers = { 'Site-Banner':'loblaw' }
letter_endings = [ 'KG', 'EA']


starting_int = 20060000

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ending = sys.argv[1]
        letter_endings = [ending]
        starting_int = int(sys.argv[2])

    for i in range(starting_int, 21000000):
        for ending in letter_endings:
            url = url_base + str(i) + "_" + ending 
            resp = r.get(url, headers=headers).json()
            print(str(i) + "_" + ending, end='\r')
            if 'code' in resp:
                print('found ' + resp['name'])
                with open('codes.txt', 'a+') as f:
                    f.write(resp['code'] + "\n")

