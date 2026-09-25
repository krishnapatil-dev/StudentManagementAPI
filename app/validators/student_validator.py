from app.exceptions.errors import ValidationError

def validate_required_fields(data):

    if not isinstance(data, dict):
        raise ValidationError("Request body must contain valid JSON.")

    required_fields = ["first_name", "last_name", "course_id", "email", "marks"]

    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Error: {field} is required.")


def validate_student_data(name, age, course_id, email, marks):

    # isinstance checks for the appropriate datatype
    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Name cannot be empty.")

    if not isinstance(age, int):
        raise ValidationError("Age must be a number.")

    if age < 16 or age > 100:
        raise ValidationError("Age must be between 16 and 100.")

    if not isinstance(course_id, int):
        raise ValidationError("Course ID must be a number.")

    if course_id <= 0:
        raise ValidationError("Course ID must be greater than 0.")

    if not isinstance(email, str) or "@" not in email:
        raise ValidationError("Invalid email address.")

    if not isinstance(marks, (int, float)):
        raise ValidationError("Marks must be a number.")

    if marks < 0 or marks > 100:
        raise ValidationError("Marks must be between 0 and 100.")