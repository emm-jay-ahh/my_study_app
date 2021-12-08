from flask import Blueprint, jsonify, request, render_template
from main import db
from models.courses import Course
from schemas.course_schema import courses_schema, course_schema


courses = Blueprint('courses', __name__)

# @app.route('/', methods=["GET"])
#     def home():
#         return "Welcome to 'My Study App'"

@courses.route("/courses/", methods=["GET"])
def get_courses():
    data = {
    "page_title": "Course Index",
    "courses": courses_schema.dump(Course.query.all())
    }
    return render_template("course_index.html", page_data = data)


@courses.route("/courses/", methods=["POST"])
def create_course():
    new_course = course_schema.load(request.json)
    db.session.add(new_course)
    db.session.commit()
    return jsonify(course_schema.dump(new_course))


@courses.route("/courses/<int:id>/", methods = ["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course_schema.dump(course))


@courses.route("/courses/<int:id>/", methods=["PUT", "PATCH"])
def update_course(id):
    course = Course.query.filter_by(course_id=id)
    updated_fields = course_schema.dump(request.json)
    if updated_fields:
        course.update(updated_fields)
        db.session.commit()
    return jsonify(course_schema.dump(course.first()))


@courses.route("/courses/<int:id>/", methods = ["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify(course_schema.dump(course))