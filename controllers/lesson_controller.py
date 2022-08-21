from flask import Flask, render_template, Blueprint
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("classes", __name__)

@lessons_blueprint.route("/classes")
def locations():
    lessons = lesson_repository.select_all()
    return render_template("/classes/classes.html", lessons = lessons)