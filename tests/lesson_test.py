import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", "Jim", "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
        self.lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")