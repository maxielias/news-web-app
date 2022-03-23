# import os
import json
import re

with open("data/top_headlines.json", "r") as jsonfile:
    top_headlines_json = json.load(jsonfile)

title = [a['title'] for a in top_headlines_json]
"""list_title_agg = []
for t in range(0, len(title), 4):
        start = t
        end = t + 3
        list_title_agg.append(title[start:end])

print(list_title_agg)
print(len(list_title_agg))
print(len(list_title_agg[1]))"""

#print(title[0])
#print(top_headlines_json[0]['source']['name'])
#print(title[0].lower().replace(' - ' + top_headlines_json[0]['source']['name'].lower(), ''))

# print(re.split('-', title[0])[-1].lower().replace(top_headlines_json[0]['source']['name'].lower(), ''))
# print(len(re.split('-', title[0])))
# print(re.findall(r'[^\w]{2,}', title[0])[-1])
# print(re.split(re.findall(r'[^\w]{2,}', title[0])[-1], title[0])[:-1])
# print(" ".join(re.split('-', title[0])[:-1]).lstrip(' ').rstrip(' '))
source = list(set([s['source']['name'] for s in top_headlines_json]))
title = [a['title'].split(' - ')[0] for a in top_headlines_json]
print(len(title))
