from app.models.course import Course
from app.database.course_repository import CourseRepository
from app.exceptions.errors import ValidationError


class CourseService:

    def __init__(self):
        self.repository = CourseRepository()

    def create_course(self, name):

        if not isinstance(name, str) or not name.strip():
            raise ValidationError(
                "Course name cannot be empty."
            )

        existing_course = self.repository.get_by_name(
            name.strip()
        )

        if existing_course:
            raise ValidationError(
                "Course already exists."
            )

        course = Course(
            name=name.strip()
        )

        return self.repository.create(course)

    def get_all_courses(self):
        return self.repository.get_all()

    def get_course_by_id(self, course_id):
        return self.repository.get_by_id(course_id)