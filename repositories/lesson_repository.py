from db.run_sql import run_sql

from models.lesson import Lesson
from models.member import Member

import repositories.instructor_repository as instructor_repository

def save(lesson):
    sql = "INSERT INTO lessons (title, date, time, duration, instructor_id, location, capacity, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.title, lesson.date, lesson.time, lesson.duration, lesson.instructor.id, lesson.location, lesson.capacity, lesson.description]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        instructor = instructor_repository.select(result['instructor_id'])
        lesson = Lesson(result['title'], result['date'], result['time'], result['duration'], instructor, result['location'], result['capacity'], result['description'], result['id'])
    return lesson

def select_all():
    lessons = []

    sql = "SELECT * FROM lessons ORDER BY date ASC, time ASC"
    results = run_sql(sql)
    for row in results:
        instructor = instructor_repository.select(row['instructor_id'])
        lesson = Lesson(row['title'], row['date'], row['time'], row['duration'], instructor, row['location'], row['capacity'], row['description'], row['id'])
        lessons.append(lesson)
    return lessons

def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)

def get_member_list_for_lesson(lesson):
    members = []

    sql = """SELECT * FROM members
            INNER JOIN bookings
            on members.id = bookings.member_id
            WHERE bookings.lesson_id = %s"""
    values = [lesson.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def lesson_full(lesson):
    if len(get_member_list_for_lesson(lesson)) >= lesson.capacity:
        return True
    return False

def select_all_len():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    for row in results:
        lesson = Lesson(row['title'], row['date'], row['time'], row['duration'], row['instructor_id'], row['location'], row['capacity'], row['description'], row['id'])
        lessons.append(lesson)
    return len(lessons)

def update(lesson):
    sql = "UPDATE lessons SET (title, date, time, duration, instructor_id, location, capacity, description) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.title, lesson.date, lesson.time, lesson.duration, lesson.instructor, lesson.location, lesson.capacity, lesson.description, lesson.id]
    run_sql(sql, values)   