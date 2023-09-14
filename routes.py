from flask import render_template
from flask_smorest import Blueprint

blp = Blueprint("routes", __name__, description = "The main routes blueprint")

@blp.route('/')
def index():
    return render_template('index.html')