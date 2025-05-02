from flask import Blueprint, render_template, redirect, request, flash, url_for

from blueprint.app import db
from blueprint.person.models import Person

person = Blueprint("person", __name__, template_folder="templates")

@person.route("/")
def home():
    people = Person.query.all()
    return render_template("person/index.html", people=people)


@person.route("/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        job = request.form.get("job")        

        age = age if age != "" else None
        job = job if job != "" else None

        person = Person(name=name, age=age, job=job)

        db.session.add(person)
        db.session.commit()

        # flash("New person was added successfully")
        return redirect(url_for("person.home"))
    return render_template("person/new.html")