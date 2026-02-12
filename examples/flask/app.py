from textwrap import indent

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


@app.route("/echo", methods=["GET", "POST"])
def echo():
    """Showing use of the `Request` object. https://flask.palletsprojects.com/en/stable/api/#flask.Request"""

    headers_str = indent(str(request.headers), "  ")
    body = request.get_data(as_text=True)

    print(f"""-----START-----
Method: {request.method}
URL: {request.url}
Headers:
{headers_str}
Body: "{body}"
-----END-----""")

    return "See server logs for details on the request."


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


@app.route("/data.json")
def data_api():
    """Dictionaries and lists are treated as JSON. https://flask.palletsprojects.com/en/stable/quickstart/#about-responses"""
    return df.to_dict(orient="records")


@app.route("/divide")
def divide():
    """Example showing use of query parameters. https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object"""

    numerator = request.args.get("numerator", type=float)
    denominator = request.args.get("denominator", type=float)

    if numerator is None or denominator is None:
        return {
            "error": "Both 'numerator' and 'denominator' parameters are required to be numeric values"
        }, 400

    if denominator == 0:
        return {"error": "Division by zero is not allowed"}, 400

    result = numerator / denominator
    return {"numerator": numerator, "denominator": denominator, "result": result}
