from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


@app.route("/echo", methods=["GET", "POST"])
def echo():
    print("-----START-----")
    print("Method:", request.method)
    print("URL:", request.url)
    print("Headers:\n")
    print(request.headers)
    print(f'Body: "{request.get_data(as_text=True)}"')
    print("-----END-----")
    return "see console"


df = pd.DataFrame(
    {
        "A": [0, 1, 2, 3, 4],
        "B": [5, 6, 7, 8, 9],
        "C": ["a", "b", "c--", "d", "e"],
    }
)


@app.route("/table")
def show_table():
    """Based on https://stackoverflow.com/a/52644615/358804"""
    return render_template("index.html", table=df.to_html())
