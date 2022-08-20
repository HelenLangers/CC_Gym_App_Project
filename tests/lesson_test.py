import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", "Jim", "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
        self.lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")

    def test_lesson1_has_title(self):
        self.assertEqual("Spin with Jim", self.lesson1.title)

    def test_lesson2_has_date(self):
        self.assertEqual("Wednesday 7th September", self.lesson2.date)

    def test_lesson1_has_time(self):
        self.assertEqual("07:00", self.lesson1.time)

    def test_lesson2_has_duration(self):
        self.assertEqual("60 mins", self.lesson2.duration)

    def test_lesson1_has_instructor_string(self):
        self.assertEqual("Jim", self.lesson1.instructor)

    def test_lesson2_has_location_string(self):
        self.assertEqual("Studio", self.lesson2.location)

    def test_lesson1_has_capacity(self):
        self.assertEqual(20, self.lesson1.capacity)

    def test_lesson2_has_description(self):
        self.assertEqual("Stretch off the stresses of mid-week with our restorative yoga hour", self.lesson2.description)