from sqlalchemy.exc import IntegrityError

from app.database.db import db
from app.exceptions.errors import DatabaseError
from app.models.student import Student
from app.models.course import Course


class StudentRepository:

    def create(self, student):
        try:
            db.session.add(student)
            db.session.commit()

            return student

        except IntegrityError:
            db.session.rollback()

            raise DatabaseError(
                "A student with this email already exists."
            )

    def get_all(self, page, limit):
        offset = (page - 1) * limit

        return Student.query.order_by(
            Student.id
        ).offset(offset).limit(limit).all()

    def get_by_id(self, student_id):
        return db.session.get(Student, student_id)

    def update(self, student_id, student):
        existing_student = db.session.get(Student, student_id)

        if existing_student is None:
            return None

        try:
            existing_student.name = student.name
            existing_student.age = student.age
            existing_student.course_id = student.course_id
            existing_student.email = student.email
            existing_student.marks = student.marks

            db.session.commit()

            return existing_student

        except IntegrityError:
            db.session.rollback()

            raise DatabaseError(
                "A student with this email already exists."
            )

    def delete(self, student_id):
        student = db.session.get(Student, student_id)

        if student is None:
            return False

        try:
            db.session.delete(student)
            db.session.commit()

            return True

        except IntegrityError:
            db.session.rollback()

            raise DatabaseError(
                "Student could not be deleted."
            )

    def search(self, keyword):
        return Student.query.join(
            Course
        ).filter(
            (Student.name.ilike(f"%{keyword}%")) |
            (Student.email.ilike(f"%{keyword}%")) |
            (Course.name.ilike(f"%{keyword}%"))
        ).order_by(Student.id).all()

    def get_by_course(self, course_id, page, limit):
        offset = (page - 1) * limit

        return Student.query.filter(
            Student.course_id == course_id
        ).order_by(
            Student.id
        ).offset(offset).limit(limit).all()