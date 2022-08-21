from flask import Flask, render_template, Blueprint
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)
