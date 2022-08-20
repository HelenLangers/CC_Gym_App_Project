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
member3 = Member("Matt Thomson")
member_repository.save(member3)
member4 = Member("Elaine Taylor")
member_repository.save(member4)
member5 = Member("Jasmin Langridge")
member_repository.save(member5)
member6 = Member("Johnny Milner")
member_repository.save(member6)
member7 = Member("Emily Willing")
member_repository.save(member7)

lesson1 = Lesson("Spin with Jim", "Monday 5th September", "07:00", "60 mins", "Jim", "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
lesson_repository.save(lesson1)
lesson2 = Lesson("Peaceful Yoga", "Wednesday 7th September", "17:30", "60 mins", "Clara", "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")
lesson_repository.save(lesson2)
lesson3 = Lesson("Circuits", "Tuesday 6th September", "12:00", "30 mins", "Luke", "Weights Room", 10, "Hit every muscle group with dynamic exercises across 10 stations in a short and sharp 30 minute circuits class")
lesson_repository.save(lesson3)
lesson4 = Lesson("Legs, Bums and Tums", "Monday 5th September", "11:00", "45 mins", "Pam", "Studio", 6, "Wear your squat proof leggings for this one, folks. Unless you want to embarrass yourself")
lesson_repository.save(lesson4)
lesson5 = Lesson("The Core Essentials", "Monday 5th September", "19:00", "45 mins", "Weights Room", 10, "You use your core for everything, including drinking that beer. So give it the workout it deserves")
lesson_repository.save(lesson5)
lesson6 = Lesson("Thai Chi", "Tuesday 6th September", "07:00", "45 mins", "Linda", "Studio", 5, "If you know, you know. All welcome")
lesson_repository.save(lesson6)

booking1 = Booking(lesson1, member2)
booking_repository.save(booking1)
booking2 = Booking(lesson2, member1)
booking_repository.save(booking2)