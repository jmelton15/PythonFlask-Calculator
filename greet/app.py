from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def landing_page():
    """landing page
    """
    html = """
    <html>
        <body>
            <h1> Welcome To The Landing Page</h1>
            <a href='/welcome/home'>Go to Home Page</a>
            <a href='/welcome/back'>Go to Back Page</a>
        </body>
    </html>
    """
    return html

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    return "welcome back"