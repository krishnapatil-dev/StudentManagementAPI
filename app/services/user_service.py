from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.database.user_repository import UserRepository
from app.exceptions.errors import DatabaseError, ValidationError
from app.models.user import User

class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def register(self, username, password):

        if not username or not username.strip():
            raise ValidationError('Username cannot be empty')

        if not password:
            raise ValidationError('Password cannot be empty')

        if len(password) < 6:
            raise ValidationError('Password must be at least 6 characters long')

        existing_user = self.repository.get_by_username(username)

        if existing_user:
            raise DatabaseError('User already exists')

        password_hash = generate_password_hash(password)

        user = User(username=username, password=password_hash)

        return self.repository.create(user)

    def login(self, username, given_password):

        user = self.repository.get_by_username(username)

        if user is None:
            raise ValidationError('Invalid username or password')

        if not check_password_hash(user.password, given_password):
            raise ValidationError('Invalid password')

        token = create_access_token(identity=str(user.id))

        return token




