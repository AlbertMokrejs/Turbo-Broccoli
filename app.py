
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

#home route, subject to change what it loads
@app.route("/")
def start():
    return render_template("home.html")

#route to register a user
@app.route("/register")
def register():
    return render_template("register.html")

#route to login, subject to change
@app.route("/login")
def login():
    return render_template("login.html")


#overall route to pass something to backend from front without reloading page
@app.route("/get_functions")
def get_functions():
    return null;

#overall route to change something backend without reloading page
@app.route("/set_functions")
def set_functions():
    return null;

if __name__ == "__main__":
    app.debug = True;
    app.run(host="0.0.0.0", port=8000)
