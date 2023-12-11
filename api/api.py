"""lightforum API application
Takes the form of a flask backend serving up a REST API for the React frontend.

Is separately accessible from the proper endpoints.
"""
from flask import Flask

def create_app():
    app = Flask(__name__)

    from routes import status
    app.register_blueprint(status)

    return app

app = create_app()
