from re import L


class Instructor:

    def __init__(self, name, speciality, bio, id = None):
        self.name = name
        self.speciality = speciality
        self.bio = bio
        self.id = id