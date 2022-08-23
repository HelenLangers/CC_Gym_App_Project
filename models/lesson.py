import datetime

class Lesson:

    def __init__(self, title, date, time, duration, instructor, location, capacity, description, id = None):
        self.title = title
        self.date = date
        self.time = time
        self.duration = duration
        self.instructor = instructor
        self.location = location
        self.capacity = capacity
        self.description = description
        self.id = id

    