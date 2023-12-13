"""lightforum API application
Takes the form of a flask backend serving up a REST API for the React frontend.

Is separately accessible from the proper endpoints.
"""
from config import Config

from flask import Flask

import os

def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)

    from routes import status
    app.register_blueprint(status)

    from models import db, migrate
    from models import User

    db.init_app(app)
    migrate.init_app(app, db)

    return app

app = create_app()
