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


async def get_top_headlines(session, url, q=None, country='ar', category=None,
                            api_key=None):

    if api_key is None:
        api_key = config.api_key_newsapi

    headers = {
        'accept': 'application/json',
        'X-Api-Key': api_key
    }

    if country is None:
        country = get_country()

    if category is None:
        category = get_category()

    async with aiohttp.ClientSession(headers=headers) as session:

        async with session.get(url=url) as resp:
            print(resp.status)
            res = await resp.json()
            # print(res)

            return res


async def get_all_requests(session, urls, api_key=None):
    if api_key is None:
        api_key = config.api_key_newsapi

    """headers = {
        'accept': 'application/json',
        'X-Api-Key': api_key
    }"""

    for url in urls:
        tasks = []
        task = asyncio.create_task(get_top_headlines(session, url))
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

    async with aiohttp.ClientSession() as session:
        data = await get_all_requests(session, urls)

        return data


if __name__ == '__main__':
    country = 'ar'
    urls = ['https://newsapi.org/v2/top-headlines?country={}'.format(country)]

    results = asyncio.get_event_loop().run_until_complete(main(urls))

    # print(type(results))
    # print(results[0])
    print('{} top headlines for Argentina'.format(
            int(results[0]['totalResults'])))

    articles_dict = [a for a in results[0]['articles']]

    """dict_news = ()
    for a in articles_dict:
        print(a)
        dict_news += a
        # dict_news.update(a)"""

    # print(dict_news)
    # print(len(dict_news))

    with open("data/top_headlines.json", "w") as jsonfile:
        json.dump(articles_dict, jsonfile, indent=1)
