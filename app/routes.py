from flask import Blueprint, blueprints, render_template
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template('index.html')
