from flask import Flask, render_template
import json
# import os
# import search_news

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/top_headlines")
def get_top_headlines():
    with open("data/top_headlines.json", "r") as jsonfile:
        top_headlines_json = json.load(jsonfile)

    return render_template("top_headlines.html",
                           top_headlines_title=top_headlines_json)


@app.route("/headlines")
def top_headlines():
    return render_template("headlines.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
