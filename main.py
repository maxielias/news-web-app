from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
import json
# import os
import search_news
import asyncio

app = Flask(__name__)
# db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
async def home():
    await search_news.update_top_headers()
    asyncio.sleep(1.0)

    with open("data/top_headlines.json", "r") as jsonfile:
        top_headlines_json = json.load(jsonfile)

    title = [a['title'] for a in top_headlines_json]
    url = [a['url'] for a in top_headlines_json]
    n_articles = len([a['title'] for a in top_headlines_json])

    return render_template("home.html",
                           top_headlines_json,
                           top_headlines_titles=title,
                           top_headlines_url=url,
                           n_articles=n_articles)


@app.route("/top_headlines")
def get_top_headlines():
    with open("data/top_headlines.json", "r") as jsonfile:
        top_headlines_json = json.load(jsonfile)

    title = [a['title'] for a in top_headlines_json]
    n_articles = len([a['title'] for a in top_headlines_json])

    return render_template("top_headlines.html",
                           top_headlines_json,
                           top_headlines_titles=title,
                           n_articles=n_articles)


@app.route("/headlines")
def top_headlines():
    return render_template("headlines.html")


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000, debug=True)
