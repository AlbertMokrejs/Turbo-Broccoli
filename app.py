
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route("/")
def start():
    return render_template("home.html")

@app.route("/register")
def register():
    return null

@app.route("/login")
def login():
    return null

@app.route("/calender")
def calender():
    return null

if __name__ == "__main__":
    app.debug = True;
    app.run(host="0.0.0.0", port=8000)
