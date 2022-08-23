from db.run_sql import run_sql

import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository

from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    if results != []:
        booking.id = results[0]['id']
        return booking
    return False

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        booking = Booking(result['member_id'], result['lesson_id'], result['id'])
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        booking = Booking(lesson, member, row['id'])
        bookings.append(booking)
    return bookings

def lesson_of_booking(booking):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [booking.lesson.id]
    results = run_sql(sql, values)[0]
    instructor = instructor_repository.select(results['instructor_id'])
    lesson = Lesson(results['title'], results['date'], results['time'], results['duration'], instructor, results['location'], results['capacity'], results['description'], results['id'])
    return lesson

def member_of_booking(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)
    member = Member(results['name'], results ['id'])
    return member

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def select_all_len():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        booking = Booking(row['lesson_id'], row ['member_id'], row['id'])
        bookings.append(booking)
    return len(bookings)
