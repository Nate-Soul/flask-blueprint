import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    db.init_app(app)

    #register app here
    from blueprint.core.routes import core
    from blueprint.todos.routes import todos
    from blueprint.person.routes import person

    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(person, url_prefix="/person")

    migrate = Migrate(app, db)

    return app