from app.database.db import db

class Student(db.Model): # SQLAlchemy knows this class represents a database table.
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course_id = db.Column(
        db.Integer, db.ForeignKey('courses.id'), nullable=False # foreign key to id column of 'courses' table
    )
    email = db.Column(db.String(100), unique=True, nullable=False)
    marks = db.Column(db.Float, nullable=False)

    course = db.relationship('Course')