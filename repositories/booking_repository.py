from db.run_sql import run_sql

from models.booking import Booking

def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

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
        booking = Booking(row['lesson_id'], row ['member_id'], row['id'])
        bookings.append(booking)
    return bookings

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql = (sql, values)

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
