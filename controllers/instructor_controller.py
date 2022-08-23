from flask import Flask, render_template, redirect
from flask import Blueprint
import repositories.instructor_repository as instructor_repositories
from models.instructor import Instructor

instructor_blueprint = Blueprint("instructors", __name__)

@instructor_blueprint.route("/instructors")
def view_all_instructors():
    instructors = instructor_repositories.select_all()
    return render_template("/instructors/allinstructors.html", instructors = instructors)

@instructor_blueprint.route("/instructors/<id>/delete", methods=['POST'])
def delete_instructor(id):
    instructor_repositories.delete(id)
    return redirect("/instructors")