#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scraping")
def scraping():
    data = [
        {"strong": True, "content": "Test"},
        {"strong": False, "content": "Test"},
    ]
    return render_template("scraping.html", table=data)


# starts the webserver
if __name__ == "__main__":
    app.run()
