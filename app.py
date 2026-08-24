from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/astro")
def astro():
    return render_template("astro.html")


@app.route("/travel")
def travel():
    return render_template("travel.html")


@app.route("/street")
def street():
    return render_template("street.html")


@app.route("/animal")
def animal():
    return render_template("animal.html")
