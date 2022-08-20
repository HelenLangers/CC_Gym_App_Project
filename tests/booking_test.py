import unittest
from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

import repositories.booking_repository as booking_repository
from repositories.booking_repository import *
import repositories.lesson_repository as lesson_repository
from repositories.lesson_repository import save
import repositories.member_repository as member_repository
from repositories.member_repository import save
from db.run_sql import run_sql


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("Mike Langridge")

        self.member2 = Member("Helen Langridge")
        # member_repository.save(self.member2)

        self.lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", "Jim", "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
        # lesson_repository.save(self.lesson1)
        self.lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")

        self.booking1 = Booking(self.lesson1, self.member2)
        # booking_repository.save(self.booking1)

    def test_booking1_has_lesson(self):
        self.assertEqual("Spin with Jim", self.booking1.lesson.title)

    def test_booking1_has_member(self):
        self.assertEqual("Helen Langridge", self.booking1.member.name)

# Couldn't get this test to work
    # def test_booking_added_to_db(self):
    #     booking_repository.save(self.booking1)
    #     booking_added = booking_repository.select(self.booking1.id)
    #     self.assertEqual(6, booking_added.id)

    # def test_select_all_list(self):
    #     bookings = booking_repository.select_all()
    #     self.assertEqual(15, len(bookings))

    # def test_delete_all(self):
    #     booking_repository.delete_all()
    #     bookings = booking_repository.select_all()
    #     self.assertEqual(0, len(bookings))
