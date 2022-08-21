from flask import Flask, render_template
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

from controllers.lesson_controller import lessons_blueprint

app = Flask(__name__)

app.register_blueprint(lessons_blueprint)

@app.route("/")
def index():
    bookings_total = booking_repository.select_all_len()
    members_total = member_repository.select_all_len()
    lessons_total = lesson_repository.select_all_len()
    return render_template("index.html", bookings_total = bookings_total, members_total = members_total, lessons_total = lessons_total)

if __name__ == "__main__":
    app.run(debug=True)