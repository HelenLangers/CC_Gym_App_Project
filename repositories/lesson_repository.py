from db.run_sql import run_sql

from models.lesson import Lesson

def save(lesson):
    sql = "INSERT INTO lessons (title, date, time, duration, instructor, location, capacity, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.title, lesson.date, lesson.time, lesson.duration, lesson.instructor, lesson.location, lesson.capacity, lesson.description]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return results

def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        lesson = Lesson(result['title'], result['date'], result['time'], result['duration'], result['instructor'], result['location'], result['capacity'], result['description'])
    return lesson

