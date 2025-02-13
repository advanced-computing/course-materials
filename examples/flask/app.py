"""Based on https://stackoverflow.com/a/52644615/358804"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame(
    {
        "A": [0, 1, 2, 3, 4],
        "B": [5, 6, 7, 8, 9],
        "C": ["a", "b", "c--", "d", "e"],
    }
)


@app.route("/")
def show_table():
    return render_template("index.html", table=df.to_html())


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
