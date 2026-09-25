from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.services.student_service import StudentService
from app.exceptions.errors import ValidationError


student_bp = Blueprint("student", __name__)

service = StudentService()


@student_bp.route("/students", methods=["POST"])
@jwt_required()
def add_student():

    data = request.get_json()

    if not isinstance(data, dict):
        raise ValidationError(
            "Request body must contain valid JSON."
        )

    name = data.get("name")
    age = data.get("age")
    course_id = data.get("course_id")
    email = data.get("email")
    marks = data.get("marks")

    student = service.add_student(
        name,
        age,
        course_id,
        email,
        marks
    )

    return jsonify({
        "message": "Student created successfully.",
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": {
                "id": student.course.id,
                "name": student.course.name
            },
            "email": student.email,
            "marks": student.marks
        }
    }), 201


@student_bp.route("/students", methods=["GET"])
@jwt_required()
def get_students():

    course_id = request.args.get(
        "course_id",
        type=int
    )

    page = request.args.get(
        "page",
        1,
        type=int
    )

    limit = request.args.get(
        "limit",
        10,
        type=int
    )

    if page < 1:
        raise ValidationError(
            "Page must be greater than 0."
        )

    if limit < 1:
        raise ValidationError(
            "Limit must be greater than 0."
        )

    if course_id:
        students = service.get_students_by_course(
            course_id,
            page,
            limit
        )
    else:
        students = service.get_all_students(
            page,
            limit
        )

    return jsonify({
        "page": page,
        "limit": limit,
        "students": [
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": {
                    "id": student.course.id,
                    "name": student.course.name
                },
                "email": student.email,
                "marks": student.marks
            }
            for student in students
        ]
    })


@student_bp.route(
    "/students/<int:student_id>",
    methods=["GET"]
)
@jwt_required()
def get_student(student_id):

    student = service.get_student_by_id(
        student_id
    )

    if student is None:
        return jsonify({
            "error": "Student not found."
        }), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": {
            "id": student.course.id,
            "name": student.course.name
        },
        "email": student.email,
        "marks": student.marks
    })


@student_bp.route(
    "/students/search",
    methods=["GET"]
)
@jwt_required()
def search_students():

    keyword = request.args.get("keyword")

    students = service.search_students(keyword)

    return jsonify({
        "keyword": keyword.strip(),
        "students": [
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": {
                    "id": student.course.id,
                    "name": student.course.name
                },
                "email": student.email,
                "marks": student.marks
            }
            for student in students
        ]
    })


@student_bp.route(
    "/students/<int:student_id>",
    methods=["PUT"]
)
@jwt_required()
def update_student(student_id):

    data = request.get_json()

    if not isinstance(data, dict):
        raise ValidationError(
            "Request body must contain valid JSON."
        )

    name = data.get("name")
    age = data.get("age")
    course_id = data.get("course_id")
    email = data.get("email")
    marks = data.get("marks")

    student = service.update_student(
        student_id,
        name,
        age,
        course_id,
        email,
        marks
    )

    if student is None:
        return jsonify({
            "error": "Student not found."
        }), 404

    return jsonify({
        "message": "Student updated successfully.",
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": {
                "id": student.course.id,
                "name": student.course.name
            },
            "email": student.email,
            "marks": student.marks
        }
    })


@student_bp.route(
    "/students/<int:student_id>",
    methods=["DELETE"]
)
@jwt_required()
def delete_student(student_id):

    success = service.delete_student(
        student_id
    )

    if not success:
        return jsonify({
            "error": "Student not found."
        }), 404

    return jsonify({
        "message": "Student deleted successfully."
    })