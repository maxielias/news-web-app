# import os
import json

with open("data/top_headlines.json", "r") as jsonfile:
    top_headlines_json = json.load(jsonfile)

print([a['title'] for a in top_headlines_json])
