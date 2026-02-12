from flask import Flask, request

app = Flask(__name__)

# hello world
@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"

@app.route("/sum", methods=["GET"])
def sum():
    """Return the sum of two numbers."""

    a = request.args.get("a")
    b = request.args.get("b")

    return str( int(a) + int(b))

if __name__ == "__main__":
    app.run(debug=True)

