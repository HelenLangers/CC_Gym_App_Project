from models.member import Member
from models.booking import Booking
from models.lesson import Lesson

import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository

member_repository.delete_all()
lesson_repository.delete_all()
booking_repository.delete_all()

member1 = Member("Mike Langridge")
member_repository.save(member1)
member2 = Member("Helen Langridge")
member_repository.save(member2)

lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", "Jim", "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
lesson_repository.save(lesson1)
lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")
lesson_repository.save(lesson2)

booking1 = Booking(lesson1, member2)
booking_repository.save(booking1)
booking2 = Booking(lesson2, member1)
booking_repository.save(booking2)