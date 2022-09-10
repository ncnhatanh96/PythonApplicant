import time
import asyncio
import aiohttp
from faker import Faker
import json
fake = Faker('en_US')

from asgiref import sync
def fakeApplicant():
    applicant = {
        "name": fake.name(),
        "email": fake.email(),
        "dob": fake.date(),
        "country": fake.country_code() 
    }
    return applicant
def timed(func):
    """
    records approximate durations of function calls
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        print('{name:<30} started'.format(name=func.__name__))
        result = func(*args, **kwargs)
        duration = "{name:<30} finished in {elapsed:.2f} seconds".format(
            name=func.__name__, elapsed=time.time() - start
        )
        print(duration)
        timed.durations.append(duration)
        return result
    return wrapper

timed.durations = []

@timed
def async_aiohttp_post(urls):
    """
    performs asynchronous get requests
    """
    async def post(urls):
        async with aiohttp.ClientSession() as session:
            async def fetch(url):
                async with session.post(url, json=fakeApplicant()) as response:
                    return await response.json()
            return await asyncio.gather(*[
                fetch(url) for url in urls
            ])
    return sync.async_to_sync(post)(urls)

if __name__ == '__main__':
    urls = ['http://host.docker.internal:8000/applicant']*1000
    async_aiohttp_post(urls)
    print('----------------------')
    [print (duration) for duration in timed.durations] 
