import pandas as pd
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"


@app.get("/api/list")
def list():

    # Get the query parameters
    format = request.args.get("format", "json")
    filterby = request.args.get("filterby", None)
    filtervalue = request.args.get("filtervalue", None)
    limit = int(request.args.get("limit", 1000))
    offset = int(request.args.get("offset", 0))

    # Load the data
    data = pd.read_csv("videos_data.csv")

    # filter the data
    data = filter_by_value(data, filterby, filtervalue)
    if isinstance(data, str):
        return data

    # applying the limit and offset
    data = apply_limit_offset(data, limit, offset)

    # convert the data to the requested format
    data = convert_to_format(data, format)

    return data


def filter_by_value(data, filterby, filtervalue):

    if filterby:
        if filtervalue is None:
            return "Invalid filtervalue"
        elif filterby not in data.columns:
            return "Invalid filterby column"
        else:
            data = data[data[filterby] == int(filtervalue)]
    return data


def apply_limit_offset(data, limit, offset):
    return data.iloc[offset : offset + limit]


def convert_to_format(data, format):
    if format == "json":
        return data.to_json(orient="records")
    elif format == "csv":
        return data.to_csv(index=False)
    else:
        return "Invalid format"


if __name__ == "__main__":
    app.run(debug=True)
