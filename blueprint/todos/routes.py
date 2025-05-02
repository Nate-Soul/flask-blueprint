from flask import Blueprint, render_template, redirect, request, flash, url_for

from blueprint.app import db
from blueprint.todos.models import Todo

todos = Blueprint("todos", __name__, template_folder="templates")

@todos.route("/")
def home():
    todos = Todo.query.all()
    return render_template("todos/index.html", todos=todos)


@todos.route("/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        is_active = True if 'is_active' in request.form.keys() else False

        description = description if description != "" else None

        todo = Todo(title=title, description=description, is_active=is_active)

        db.session.add(todo)
        db.session.commit()

        # flash("New task was added successfully")
        return redirect(url_for("todos.home"))
    return render_template("todos/new.html")