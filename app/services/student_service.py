from app.models.student import Student
from app.validators.student_validator import validate_student_data
from app.database.student_repository import StudentRepository
from app.database.course_repository import CourseRepository
from app.exceptions.errors import ValidationError


class StudentService:

    def __init__(self):
        self.repository = StudentRepository()
        self.course_repository = CourseRepository()

    def add_student(self, name, age, course_id, email, marks):

        validate_student_data(
            name,
            age,
            course_id,
            email,
            marks
        )

        course = self.course_repository.get_by_id(course_id)

        if course is None:
            raise ValidationError("Course not found.")

        student = Student(
            name=name,
            age=age,
            course_id=course_id,
            email=email,
            marks=marks
        )

        return self.repository.create(student)

    def get_all_students(self, page, limit):
        return self.repository.get_all(page, limit)

    def get_student_by_id(self, student_id):
        return self.repository.get_by_id(student_id)

    def update_student(
        self,
        student_id,
        name,
        age,
        course_id,
        email,
        marks
    ):

        validate_student_data(
            name,
            age,
            course_id,
            email,
            marks
        )

        course = self.course_repository.get_by_id(course_id)

        if course is None:
            raise ValidationError("Course not found.")

        student = Student(
            name=name,
            age=age,
            course_id=course_id,
            email=email,
            marks=marks
        )

        updated_student = self.repository.update(student_id, student)

        if updated_student is None:
            return None

        return updated_student

    def delete_student(self, student_id):
        return self.repository.delete(student_id)

    def search_students(self, keyword):

        if not keyword or not keyword.strip():
            raise ValidationError(
                "Search keyword is required."
            )

        return self.repository.search(keyword.strip())

    def get_students_by_course(
        self,
        course_id,
        page,
        limit
    ):
        return self.repository.get_by_course(
            course_id,
            page,
            limit
        )