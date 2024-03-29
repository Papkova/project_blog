import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import LoginManager
from models import Zodiac

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

from . import routes


@app.route("/")
def home():
    return render_template("index.html", title="Main")


@app.route("/zodiac/<int:id>")
def zodiacs(id):
    zodiac = Zodiac.query.get(id)
    name = zodiac.name
    description = zodiac.description
    return render_template("zodiac.html", name=name, description=description)