from flask import Flask, request, redirect, render_template
from flask import Blueprint
import repositories.booking_repository as booking_repositories
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
from models.booking import Booking

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def view_all():
    booking_list = booking_repositories.select_all()
    return render_template("/bookings/bookings.html", booking_list = booking_list)

@bookings_blueprint.route("/bookings/newbooking")
def booking_form():
    member_list = member_repository.select_all()
    lesson_list = lesson_repository.select_all()
    return render_template("/bookings/newbooking.html", lesson_list = lesson_list, member_list = member_list)


@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    new_booking = Booking(lesson, member)
    
    if booking_repositories.save(new_booking) == False:
        return render_template("/bookings/duplicatebooking.html", member = member, lesson = lesson)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repositories.delete(id)
    return redirect("/bookings")