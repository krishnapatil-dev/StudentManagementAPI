from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.services.course_service import CourseService
from app.exceptions.errors import ValidationError


course_bp = Blueprint("course", __name__)

service = CourseService()


@course_bp.route("/courses", methods=["POST"])
@jwt_required()
def create_course():

    data = request.get_json()

    if not isinstance(data, dict):
        raise ValidationError(
            "Request body must contain valid JSON."
        )

    name = data.get("name")

    course = service.create_course(name)

    return jsonify({
        "message": "Course created successfully.",
        "course": {
            "id": course.id,
            "name": course.name
        }
    }), 201


@course_bp.route("/courses", methods=["GET"])
@jwt_required()
def get_courses():

    courses = service.get_all_courses()

    return jsonify({
        "courses": [
            {
                "id": course.id,
                "name": course.name
            }
            for course in courses
        ]
    })


@course_bp.route(
    "/courses/<int:course_id>",
    methods=["GET"]
)
@jwt_required()
def get_course(course_id):

    course = service.get_course_by_id(
        course_id
    )

    if course is None:
        return jsonify({
            "error": "Course not found."
        }), 404

    return jsonify({
        "id": course.id,
        "name": course.name
    })