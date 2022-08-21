from flask import Flask, render_template
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

from controllers.lesson_controller import lessons_blueprint
from controllers.member_controller import members_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(lessons_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def index():
    bookings_total = booking_repository.select_all_len()
    members_total = member_repository.select_all_len()
    lessons_total = lesson_repository.select_all_len()
    member_list = member_repository.select_all()
    lesson_list = lesson_repository.select_all()
    return render_template("index.html", bookings_total = bookings_total, members_total = members_total, lessons_total = lessons_total, member_list = member_list, lesson_list = lesson_list)

if __name__ == "__main__":
    app.run(debug=True)