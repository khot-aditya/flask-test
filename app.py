from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About Page"


@app.route("/greet/")
@app.route("/greet/<name>")
def greet(name=None):
    if name:
        return "Hello " + name
    else:
        return "Missing parameter: Please provide a name."


if __name__ == "__main__":
    app.run(debug=True)
