from flask import Blueprint, render_template

# from blueprint.app import db

core = Blueprint("core", __name__, template_folder="templates")

@core.route("/")
def home():
    return render_template("core/index.html")