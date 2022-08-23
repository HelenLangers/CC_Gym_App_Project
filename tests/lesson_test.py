import unittest
from models.lesson import Lesson
from models.instructor import Instructor
from models.member import Member
from models.booking import Booking
import repositories.lesson_repository as lesson_repository
import repositories.instructor_repository as instructor_respository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
from db.run_sql import run_sql

class TestLesson(unittest.TestCase):

    def setUp(self):

        self.member1 = Member("Mike Langridge")
        member_repository.save(self.member1)
        self.member2 = Member("Helen Langridge")
        member_repository.save(self.member2)
        self.member3 = Member("Matt Thomson")
        member_repository.save(self.member3)
        self.member4 = Member("Elaine Taylor")
        member_repository.save(self.member4)


        self.instructor1 = Instructor("Jim", "Cycling", "TdF doping champion")
        instructor_respository.save(self.instructor1)

        self.lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", self.instructor1, "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
        lesson_repository.save(self.lesson1)
        self.lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", self.instructor1, "Studio", 2, "Stretch off the stresses of mid-week with our restorative yoga hour")
        lesson_repository.save(self.lesson2)

    # def test_lesson1_has_title(self):
    #     self.assertEqual("Spin with Jim", self.lesson1.title)

    # def test_lesson2_has_date(self):
    #     self.assertEqual("Wednesday 7th September", self.lesson2.date)

    # def test_lesson1_has_time(self):
    #     self.assertEqual("07:00", self.lesson1.time)

    # def test_lesson2_has_duration(self):
    #     self.assertEqual("60 mins", self.lesson2.duration)

    # def test_lesson1_has_instructor(self):
    #     print(self.lesson1.instructor.__dict__)
    #     self.assertEqual("Jim", self.lesson1.instructor.name)

    # def test_lesson2_has_location_string(self):
    #     self.assertEqual("Studio", self.lesson2.location)

    # def test_lesson1_has_capacity(self):
    #     self.assertEqual(20, self.lesson1.capacity)

    # def test_lesson2_has_description(self):
    #     self.assertEqual("Stretch off the stresses of mid-week with our restorative yoga hour", self.lesson2.description)

    # def test_is_space(self):
    #     booking1 = Booking(self.lesson2, self.member2)
    #     booking_repository.save(booking1)
    #     booking2 = Booking(self.lesson2, self.member1)
    #     booking_repository.save(booking2)
    #     self.assertEqual(True, lesson_repository.is_space(self.lesson2))

    def test_is_full(self):
        booking1 = Booking(self.lesson2, self.member2)
        booking_repository.save(booking1)
        booking2 = Booking(self.lesson2, self.member1)
        booking_repository.save(booking2)
        booking3 = Booking(self.lesson2, self.member3)
        booking_repository.save(booking3)
        self.assertEqual(True, lesson_repository.lesson_full(self.lesson2))


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