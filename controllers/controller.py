from flask import render_template
from app import app

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

@app.route("/")
def index():
    bookings_total = booking_repository.select_all_len()
    members_total = member_repository.select_all_len()
    lessons_total = lesson_repository.select_all_len()
    return render_template("index.html", bookings_total = bookings_total, members_total = members_total, lessons_total = lessons_total)