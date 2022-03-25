# from unittest import result
# from wsgiref import headers
import config
import params
import aiohttp
import asyncio
# import os
import json


def get_country():
    return params.country


def get_category():
    return params.category


def get_source():
    return params.source

"""def json_news(path):
    with open(path, 'r', encoding="utf8") as jsonfile:
        jsonfile = json.load(jsonfile)

    data = [a for a in jsonfile['articles']]

    return data"""


def replace_null_img():
    country_list = [c[0].lower() for c in params.country]
    
    for c in country_list:
        path = 'data/top_headlines_' + c + '.json'

        with open(path, 'r', encoding="utf8") as jsonfile:     
            try:
                data = json.load(jsonfile)
                replace_null = 'https://imgs.search.brave.com/Ia4xwMxHraroG2AhGFyeaM5KLPQjGCu1924x_5U5Rq8/rs:fit:640:400:1/g:ce/aHR0cHM6Ly9hcnRz/bWlkbm9ydGhjb2Fz/dC5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMTQvMDUvbm8t/aW1hZ2UtYXZhaWxh/YmxlLWljb24tNi5w/bmc'
                for uti in data['articles']:
                    if uti['urlToImage'] == None:
                        uti['urlToImage'] = replace_null

            except:
                pass

        if data:
            with open(path, 'w', encoding="utf8") as jsonfile:
                json.dump(data, jsonfile)


async def get_headlines(sem, session, url, api_key=None):

    if api_key is None:
        api_key = config.api_key_newsapi

    headers = {
        'accept': 'application/json',
        'X-Api-Key': api_key
    }

    """if country is None:
        country = get_country()

    if category is None:
        category = get_category()"""

    res_json = {}

    async with aiohttp.ClientSession(headers=headers) as session:

        async with sem, session.get(url=url) as resp:
            with open('data/top_headlines_' + url.split("country=",1)[-1] +'.json', "wb") as jsonfile:
                async for chunk in resp.content.iter_chunks():
                    jsonfile.dumps(chunk, indent=1)
            # print(resp.status)
            # res = await resp.json()
            # res_json.update({url.split("country=",1)[-1]: res})

            return res_json


async def get_all_requests(sem, session, urls, api_key=None):
    if api_key is None:
        api_key = config.api_key_newsapi

    """headers = {
        'accept': 'application/json',
        'X-Api-Key': api_key
    }"""

    sem = asyncio.Semaphore(10)

    for url in urls:
        tasks = []
        task = asyncio.create_task(get_headlines(sem, session, url))
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    return results


async def main(urls, api_key=None):
    if api_key is None:
        api_key = config.api_key_newsapi

    """headers = {
        'accept': 'application/json',
        'X-Api-Key': api_key
    }"""

    sem = asyncio.Semaphore(10)

    async with aiohttp.ClientSession() as session:
        data = await get_all_requests(sem, session, urls)

        return data


async def update_top_headlines():
    country_list = [c for c in params.country]

    urls = ['https://newsapi.org/v2/top-headlines?country=ar'] # .format(c[0].lower()) for c in country_list]

    results = await main(urls)

    replace_null_img()

    """for code, name in country_list:
        articles_dict = [a for a in results[code][0]['articles']]

        print(articles_dict)

        with open('data/top_headlines' + name.lower() + '.json', 'w') as jsonfile:
            json.dump(articles_dict, jsonfile, indent=1)"""
