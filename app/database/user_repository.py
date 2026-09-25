from app.database.db import db
from app.models.user import User

class UserRepository:

    def create(self, user):
        db.session.add(user)
        db.session.commit()

        return user

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()