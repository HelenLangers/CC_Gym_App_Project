from db.run_sql import run_sql

from models.member import Member
from models.lesson import Lesson

def save(member):
    sql = "INSERT INTO members (name) VALUES (%s) RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return results

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['id'])
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def list_lessons_member_is_signed_up_for(member):
    lessons = []
    sql = """SELECT * FROM lessons INNER JOIN bookings on bookings.lesson_id = lessons.id WHERE bookings.member_id = %s"""
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        lesson = Lesson(row['title'], row['date'], row['time'], row['duration'], row['instructor'], row['location'], row['capacity'], row['description'])
        lessons.append(lesson)
    return lessons

def select_all_len():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return len(members)   

def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)