from sqlalchemy.exc import IntegrityError

from app.database.db import db
from app.exceptions.errors import DatabaseError
from app.models.course import Course


class CourseRepository:

    def create(self, course):
        try:
            db.session.add(course)
            db.session.commit()

            return course

        except IntegrityError:
            db.session.rollback()

            raise DatabaseError(
                "Course already exists."
            )

    def get_all(self):
        return Course.query.order_by(
            Course.id
        ).all()

    def get_by_id(self, course_id):
        return db.session.get(Course, course_id)

    def get_by_name(self, name):
        return Course.query.filter_by(
            name=name
        ).first()