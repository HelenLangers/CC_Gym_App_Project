from flask import Flask, render_template, Blueprint
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

lessons_blueprint = Blueprint("classes", __name__)

@lessons_blueprint.route("/classes")
def locations():
    lessons = lesson_repository.select_all()
    return render_template("/lesson/lessons.html", lessons = lessons)

@lessons_blueprint.route("/classes/<id>")
def view_one(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.get_member_list_for_lesson(lesson)
    return render_template("lesson/onelesson.html", lesson = lesson, members = members)