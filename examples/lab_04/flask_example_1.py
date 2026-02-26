from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"


@app.route("/sum", methods=["GET"])
def sum():
    """Return the sum of two numbers."""

    a = request.args.get("a")
    b = request.args.get("b")

    return jsonify({"sum": int(a) + int(b)})


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route("/factorial", methods=["GET"])
def factorial_route():
    """Return the factorial of a number."""

    n = request.args.get("n",10)
    r = factorial(int(n))
    response = f'{n}! equals {r}'
    return response


if __name__ == "__main__":
    app.run(debug=True)
