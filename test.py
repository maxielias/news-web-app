# import os
import json
import re
import params
import search_news
import asyncio
import aiohttp
from concurrent.futures import CancelledError
import logging
logging.basicConfig(level=logging.DEBUG)

a = [c for c in params.country]
# urls = ['https://newsapi.org/v2/top-headlines?country={}'.format(c[0]) for c in a]
urls = ['https://newsapi.org/v2/top-headlines?country=us']

search_news.replace_null_img()

"""async def main():
    try:

        #token_wallet_balances.get_latest_blocks()
        await search_news.update_top_headlines()
        # token_wallet_balances.moralis_url(chain_list, token_list, wallet_list)

    except CancelledError:
        raise CancelledError

    except Exception as e:
        logging.exception(e)
        raise e
        # return None


if __name__ == "__main__":

    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
    # balances = asyncio.get_event_loop().run_until_complete(main())
    # print(balances)"""

"""with open('data/top_headlines_us.json', 'r', encoding="utf8") as jsonfile:
    jsonfile = json.load(jsonfile)

    replace_null = 'https://imgs.search.brave.com/Ia4xwMxHraroG2AhGFyeaM5KLPQjGCu1924x_5U5Rq8/rs:fit:640:400:1/g:ce/aHR0cHM6Ly9hcnRz/bWlkbm9ydGhjb2Fz/dC5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMTQvMDUvbm8t/aW1hZ2UtYXZhaWxh/YmxlLWljb24tNi5w/bmc'          

    for uti in jsonfile['articles']:
        if uti['urlToImage'] == None:
            uti['urlToImage'] = replace_null
            print("None value found")
    # url_to_image = [a['urlToImage'] == replace_null for a in jsonfile['articles'] if a['urlToImage'] == None]

    print(jsonfile)"""

"""print([a for a in jsonfile['articles']])
print([a['title'].split(' - ')[0] for a in jsonfile['articles']])"""


'https://search.brave.com/images?q=Republicans%20turn%20Ketanji%20Brown%20Jackson%20hearing%20into%20a%20political%20circus%20-%20The%20Guardian'
