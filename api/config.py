import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DB_URL')
        or 'sqlite:///' + os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'core.db'
        ))
