from db.run_sql import run_sql

from models.instructor import Instructor

def save(instructor):
    sql = "INSERT INTO instructors (name, speciality, bio) VALUES (%s, %s, %s) RETURNING id"
    values = [instructor.name, instructor.speciality, instructor.bio]
    results = run_sql(sql, values)
    instructor.id = results[0]['id']
    return instructor

def select(id):
    instructor = None
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        instructor = Instructor(result['name'], result['speciality'], result['bio'], result['id'])
    return instructor

def select_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for row in results:
        instructor = Instructor(row['name'], row['speciality'], row['bio'], row['id'])
        instructors.append(instructor)
    return instructors

def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)

def select_all_len():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for row in results:
        instructor = Instructor(row['name'], row['speciality'], row['bio'], row['id'])
        instructors.append(instructor)
    return len(instructors)

def update(instructor):
    sql = "UPDATE members SET (name, speciality, bio) = (%s, %s, %s) WHERE id = %s"
    values = [instructor.name, instructor.speciality, instructor.bio, instructor.id]
    run_sql(sql, values)