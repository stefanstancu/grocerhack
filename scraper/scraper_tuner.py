""" Tool for determining which conditions are fastest while still stable for the Loblaws API"""
from scrape import fetch_codes, generate_codes
import asyncio
import time

max_step = 1000
test_range = 10000
starting_int = 20154836

def test_step(step, codes):
    print(f'testing {len(codes)} with batch_size={step}')
    print('-------------------------------------')
    num_batches = len(codes)/step
    for i in range(0, len(codes), step):
        print(f'running batch {int(i/step)+1} of {num_batches}')
        try:
            asyncio.run(fetch_codes(codes[i:i+step]))
        except Exception as e:
            print(e)
            return False
    return True

def test_bounds(upper, lower, codes):
    if lower < upper:
        step = int((upper - lower)/2 + lower)
        a = test_step(step, codes)
        if a:
            return test_bounds(upper, step, codes)
        else:
            sleep(60*10)
            return test_bounds(step, lower, codes)
    else:
        return lower

def sleep(s):
    t = s
    while t > 0:
        print(f'sleeping {t}s', end='\r')
        time.sleep(1)
        t -= 1

if __name__=='__main__':

    # generate #test_range codes
    codes = generate_codes(starting_int, test_range)
    print(f'generated {len(codes)} codes')

    # find the step size using binary search
    opt_step = test_bounds(max_step, 0, codes)
    print(f'optimal step size is {a}')
    
