# from pickle import GET
from flask import Flask, render_template, request, redirect
# from flask_wtf import FlaskForm
# from flask_sqlalchemy import SQLAlchemy
import json
# import search_news
import math
import params

app = Flask(__name__)
# db = SQLAlchemy(app)

"""class Country(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    country = db.Column(db.String(50))

class Form(FlaskForm):
    country = SelectField('country', choices=[c for c in params.config])"""

@app.route("/")
@app.route("/home")
async def home():
    """await search_news.update_top_headlines()
    asyncio.sleep(1.0)

    with open("data/top_headlines.json", "r") as jsonfile:
        top_headlines_json = json.load(jsonfile)

    title = [a['title'] for a in top_headlines_json]
    url = [a['url'] for a in top_headlines_json]
    n_articles = len([a['title'] for a in top_headlines_json])"""

    return render_template("home.html"),
                           # top_headlines_json=top_headlines_json,
                           # top_headlines_titles=title,
                           # top_headlines_url=url,
                           # n_articles=n_articles)


@app.route("/top_headlines" , methods=["GET", "POST"])
async def get_top_headlines():
    """await search_news.update_top_headlines()
    asyncio.sleep(1.0)"""
    
    countries = [c[1] for c in params.country]
    
    with open('data/top_headlines_us.json', 'r', encoding='utf8') as jsonfile:
        top_headlines_json = json.load(jsonfile)

    if request.method == 'POST':
        country = request.form.get('countries')
        print(country)
        country_id = [c for c in params.country]
        country_id = country_id[country_id==country.lower()][0].lower()

        # print(country_id)
        
        try:
            with open('data/top_headlines_' + country_id + '.json', 'r', encoding='utf8') as jsonfile:
                top_headlines_json = json.load(jsonfile)
                print(country_id)

        except:
            pass

    top_headlines_json = [a for a in top_headlines_json['articles']]
    title = [a['title'].split(' - ')[0] for a in top_headlines_json]
    title_fixed = title
    
    cols = 5
    rows = int(math.ceil(len(title)/cols))

    return render_template("top_headlines.html",
                           top_headlines_json=top_headlines_json,
                           top_headlines_titles=title_fixed,
                           available_countries=countries,
                           # country = country,
                           rows=rows,
                           cols=cols)


"""@app.route("/headlines")
def top_headlines():
    with open("data/top_headlines.json", "r") as jsonfile:
        top_headlines_json = json.load(jsonfile)

    title = [a['title'] for a in top_headlines_json]
    n_articles = len([a['title'] for a in top_headlines_json])


    return render_template("headlines.html",
                           top_headlines_json=top_headlines_json,
                           top_headlines_titles=title,
                           n_articles=n_articles)"""

@app.route("/test")
def test_html():
    return render_template("test.html")


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000, debug=True)
