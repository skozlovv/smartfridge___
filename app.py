from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/info")
def info_page():
    return "<p>information</p>"


if __name__ == "__main__":
    app.run(debug=True)

