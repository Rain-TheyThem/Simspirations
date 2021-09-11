from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create-cas-board")
def create_cas_board():
    return render_template("create_cas_board.html")


app.run("0.0.0.0")
