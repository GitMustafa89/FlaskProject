from flask import Flask, render_template

app = Flask(__name__)

#home page
@app.route("/")
def index():
    return "Hello Flask"

#about page
@app.route("/about<name>")
def about(name):
    return f"welcome Mr. {name} to about page"


if __name__ == "__main__":
    app.run(debug=True)