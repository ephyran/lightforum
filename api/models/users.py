from . import db

from workzeug.security import generate_password_hash, check_password_hash

import sqlalchemy as sqlal

class User(db.Model):
    id: sqlal.orm.Mapped[int] = sqlal.orm.mapped_column(primary_key=True)
    username: sqlal.orm.Mapped[str] = sqlal.orm.mapped_column(sqlal.String(64), index=True, unique=True)
    email: sqlal.orm.Mapped[str] = sqlal.orm.mapped_column(sqlal.String(254), index=True, unique=True)
    pwd_hash: sqlal.orm.Mapped[str] = sqlal.orm.mapped_column(sqlal.String(256))
    two_factor_enabled: sqlal.orm.Mapped[bool] = sqlal.orm.mapped_column(sqlal.Boolean(False))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.pwd_hash, password)
