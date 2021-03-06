# To run Flask from VS Code, first type in: $env:FLASK_APP = "application.py"$env:FLASK_APP = "application.py"
#  and then: python -m flask run 

# imports Flask
from flask import Flask, render_template



# serves up the flask application from this file.
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bg_page.html")
def bg_page():
    return render_template("bg_page.html")

@app.route("/js_page.html")
def js_page():
    return render_template("js_page.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



