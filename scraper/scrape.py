import sys
import aiohttp
import asyncio
import time
from string import ascii_uppercase


url_base = 'https://www.loblaws.ca/api/product/'
headers = { 'Site-Banner':'loblaw' }
letter_endings = [ 'KG', 'EA']

file_name = 'test_codes.txt'
err_f = 'err_codes.txt'
step = 10
sleep_time = 0
starting_int = 20154836
ending_int = 20154936 

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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        starting_int = int(sys.argv[1])

    for i in range(starting_int, ending_int, step):
        codes = []
        for j in range(i, i+step):
            for ending in letter_endings:
                code = str(j) + "_" + ending 
                codes.append(code)

        # print(f'generated {len(codes)} codes from {i} to {i + 500}')

        asyncio.run(fetch_codes(codes))

        t = sleep_time
        while t > 0:
            print(f"Sleeping for {t}s", end='\r')
            time.sleep(1)
            t -= 1

