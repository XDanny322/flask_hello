import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/hello/<name>")
def hello(name):
    return {"hello": name}


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port)
