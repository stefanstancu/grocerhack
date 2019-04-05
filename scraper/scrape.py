import sys
import aiohttp
import requests as r
import asyncio
import time
from string import ascii_uppercase


url_base = 'https://www.loblaws.ca/api/product/'
headers = { 'Site-Banner':'loblaw' }
letter_endings = [ 'KG', 'EA']

file_name = 'codes.txt'

step = 15
sleep_time = 0.1
starting_int = 20154876
ending_int = 21000000 

def generate_codes(starting_int, t_range):
    """ Generates #t_range codes
        @param starting_int: int the starting number
        @param t_range: int the number of codes to make
        @return codes: list[string] the codes generated
    """
    codes = []
    for i in range(starting_int, starting_int + t_range):
        for ending in letter_endings:
            code = str(i) + "_" + ending 
            codes.append(code)

    return codes

async def fetch(session, code):
    url = url_base + code;
    async with session.get(url, headers=headers) as resp:
        if resp.status == 200:
            with open(file_name, 'a+') as f:
                f.write(code + "\n")
        elif resp.status >= 400:
            print(f'failed with code {resp.status}')
            raise Exception

async def fetch_codes(codes):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for code in codes:
            task = asyncio.create_task(fetch(session, code))
            tasks.append(task)
        try:
            await asyncio.gather(*tasks)
        except:
            raise

def sleep(s):
    t = s
    while t > 0:
        print(f'sleeping {t}s', end='\r')
        time.sleep(1)
        t -= 1

def poll_till_allowed():
    status = 403
    print('Waiting for ban to end...')
    while status == 403:
        status = r.get(url_base + str(starting_int) + '_EA').status_code
        time.sleep(10)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        starting_int = int(sys.argv[1])

    print(f'starting with batch_size={step}')
    for i in range(starting_int, ending_int, step):
        codes = generate_codes(i, step)

        try:
            asyncio.run(fetch_codes(codes))
        except:
            poll_till_allowed()
        time.sleep(1)
