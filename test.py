# import os
import json

with open("data/top_headlines.json", "r") as jsonfile:
    top_headlines_json = json.load(jsonfile)

title = [a['title'] for a in top_headlines_json]
list_title_agg = []
for t in range(0, len(title), 4):
        start = t
        end = t + 3
        list_title_agg.append(title[start:end])

print(list_title_agg)
print(len(list_title_agg))
print(len(list_title_agg[1]))
