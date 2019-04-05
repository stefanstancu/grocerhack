import sys
import aiohttp
import asyncio
import time
from string import ascii_uppercase


url_base = 'https://www.loblaws.ca/api/product/'
headers = { 'Site-Banner':'loblaw' }
letter_endings = [ 'KG', 'EA']

file_name = 'test_codes.txt'
step = 500
starting_int = 20154836
ending_int = 20154936 

async def fetch(session, code):
    url = url_base + code;
    async with session.get(url, headers=headers) as resp:
        data = await resp.json()
        if 'code' in data:
            with open(file_name, 'a+') as f:
                f.write(code + "\n")

async def fetch_codes(codes):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for code in codes:
            task = asyncio.ensure_future(fetch(session, code))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        starting_int = int(sys.argv[1])

    for i in range(starting_int, 21000000, step):
        codes = []
        for j in range(i, i+step):
            for ending in letter_endings:
                code = str(j) + "_" + ending 
                codes.append(code)

        print(f'generated {len(codes)} codes from {i} to {i + 500}')

        asyncio.run(fetch_codes(codes))
        time.sleep(3)

