"""lightforum API application
Takes the form of a flask backend serving up a REST API for the React frontend.

Is separately accessible from the proper endpoints.
"""
from config import Config
from models import db

from flask import Flask
from flask_migrate import Migrate

import os

def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)

    from routes import status
    app.register_blueprint(status)

    db.init_app(app)

    return app

def setup_db(app):
    with app.app_context():
        db.create_all()

app = create_app()

if not os.path.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
    setup_db(app)

migrate = Migrate(app, db)


