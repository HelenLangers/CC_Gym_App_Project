from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.lesson_repository as lesson_repository
import repositories.instructor_repository as instructor_repository
from models.lesson import Lesson 

lessons_blueprint = Blueprint("classes", __name__)

@lessons_blueprint.route("/classes")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("/lessons/lessons.html", lessons = lessons)

@lessons_blueprint.route("/classes/<id>")
def view_one(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.get_member_list_for_lesson(lesson)
    return render_template("lessons/onelesson.html", lesson = lesson, members = members)

@lessons_blueprint.route("/classes", methods=['POST'])
def add_lesson():
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    instructor = instructor_repository.select(request.form['instructor_id'])
    location = request.form['location']
    capacity = request.form['capacity']
    description = request.form['description']
    new_lesson = Lesson(title, date, time, duration, instructor, location, capacity, description)
    lesson_repository.save(new_lesson)
    return redirect("/classes")

@lessons_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    instructors = instructor_repository.select_all()
    return render_template("/lessons/editlesson.html", lesson = lesson, instructors = instructors)

@lessons_blueprint.route("/classes/<id>", methods=['POST'])
def update_lesson(id):
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    instructor = request.form['instructor']
    location = request.form['location']
    capacity = request.form['capacity']
    description = request.form['description']
    lesson = Lesson(title, date, time, duration, instructor, location, capacity, description, id)
    lesson_repository.update(lesson)
    return redirect("/classes")

@lessons_blueprint.route("/classes/<id>/delete", methods=['POST'])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect("/classes")