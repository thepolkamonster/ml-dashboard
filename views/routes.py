from flask import render_template
from flask_smorest import Blueprint

blp = Blueprint("routes", __name__, description = "The main views blueprint")

@blp.route("/")
def index():
    return render_template('index.html')
@blp.route("/elements")
def elements():
    return render_template('elements.html')
@blp.route("/sample")
def sample():
    return render_template("sample.html")