import unittest
from models.lesson import Lesson
from models.instructor import Instructor
import repositories.lesson_repository as lesson_repository
import repositories.instructor_repository as instructor_respository
from db.run_sql import run_sql

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.instructor1 = Instructor("Jim", "Cycling", "TdF doping champion")

        self.lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", self.instructor1, "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
        self.lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")

    def test_lesson1_has_title(self):
        self.assertEqual("Spin with Jim", self.lesson1.title)

    def test_lesson2_has_date(self):
        self.assertEqual("Wednesday 7th September", self.lesson2.date)

    def test_lesson1_has_time(self):
        self.assertEqual("07:00", self.lesson1.time)

    def test_lesson2_has_duration(self):
        self.assertEqual("60 mins", self.lesson2.duration)

    def test_lesson1_has_instructor(self):
        print(self.lesson1.instructor.__dict__)
        self.assertEqual("Jim", self.lesson1.instructor.name)

    def test_lesson2_has_location_string(self):
        self.assertEqual("Studio", self.lesson2.location)

    def test_lesson1_has_capacity(self):
        self.assertEqual(20, self.lesson1.capacity)

    def test_lesson2_has_description(self):
        self.assertEqual("Stretch off the stresses of mid-week with our restorative yoga hour", self.lesson2.description)

# This test worked but commenting out to stop it running each time I run tests.
    # def test_lesson_added_to_db(self):
    #     lesson_repository.save(self.lesson1)
    #     lesson = lesson_repository.select(self.lesson1.id)
    #     # sql = "SELECT title FROM lessons WHERE id = %s"
    #     # values = [self.lesson1.id]
    #     # results = run_sql(sql,values)
    #     self.assertEqual("Spin with Jim", lesson.title)

# This test worked but commenting out as it won't work as tests continue
    # def test_select_all_list(self):
    #     lessons = lesson_repository.select_all()
    #     self.assertEqual(7, len(lessons))

# This test worked, commenting out for future tests not to be affected
    # def test_delete_by_id(self):
    #     lesson_repository.save(self.lesson2)        
    #     lesson_repository.delete(self.lesson2.id)
    #     lessons = lesson_repository.select_all()
    #     self.assertEqual(7, len(lessons))

# This test worked, commenting out for future tests not to be affected
    # def test_delete_all(self):
    #     lesson_repository.delete_all()
    #     lessons = lesson_repository.select_all()
    #     self.assertEqual(0, len(lessons))