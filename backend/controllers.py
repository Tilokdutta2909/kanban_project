from flask import Flask,render_template
from flask import current_app as app #alias for current running app

@app.route("/")  #it refers to the url 127.0.0.1:5000
def home():
    return render_template("landing.html")

@app.route("/login")
def user_login():
    return render_template("login_from.html")

@app.route("/signin")
def user_signin():
    return render_template("signin_from.html");

@app.route("/user")
def user():
    return render_template("user_dashboard.html");