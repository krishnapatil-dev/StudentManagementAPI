from pathlib import Path
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from app.database.db import db
from app.routes.student_routes import student_bp
from app.routes.auth_routes import auth_bp
from app.routes.course_routes import course_bp
from app.exceptions.errors import ValidationError, DatabaseError
from dotenv import load_dotenv
import os

load_dotenv() # reads and gives access to .env file

def create_app():
    app = Flask(__name__)
    
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        BASE_DIR = Path(__file__).resolve().parent.parent
        DATABASE_PATH = BASE_DIR / "data" / "students.db"

        app.config["SQLALCHEMY_DATABASE_URI"] = ( # use sqlite and given db file
            f"sqlite:///{DATABASE_PATH.as_posix()}" # as_posix to convert \ into /
        )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Do not use SQLAlchemy modification tracking system

    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

    jwt = JWTManager(app)

    db.init_app(app) # connects db extension to flask application

    migrate = Migrate(app, db)

    app.register_blueprint(student_bp)

    app.register_blueprint(auth_bp)

    app.register_blueprint(course_bp)

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "str(error)"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Resource not found."
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": "HTTP method not allowed."
        }), 405

    @app.errorhandler(DatabaseError)
    def handle_database_error(error):
        return jsonify({
            "error": "str(error)."
        }), 409 # 409 = conflict

    return app
