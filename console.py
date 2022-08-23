import datetime

from models.member import Member
from models.booking import Booking
from models.lesson import Lesson
from models.instructor import Instructor

import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.instructor_repository as instructor_repository

instructor_repository.delete_all()
member_repository.delete_all()
lesson_repository.delete_all()
booking_repository.delete_all()

instructor1 = Instructor("Jim", "Cycling", "Legend has it, Jim won the Tour de France three times, but got caught doping. You'll not find a record of it, but you'll not stop hearing about it. We're thrilled to have him leading our spin classes at Active Gym.")
instructor_repository.save(instructor1)
instructor2 = Instructor("Clara", "Yoga", "Learning her craft in Bali then India, you're in great hands even if you're a total beginner to yoga.")
instructor_repository.save(instructor2)
instructor3 = Instructor("Luke", "Strength", "Luke doesn't take steroids, we promise. We've tested. He's just really strong, and you can be too!")
instructor_repository.save(instructor3)
instructor4 = Instructor("Pam", "Strength", "Pam is passionate about getting more women working with weights, especially as they get older and more at risk of poor bone health")
instructor_repository.save(instructor4)
instructor5 = Instructor("Joe", "Core", "Joe works with a range of members who want to activate their core better. If you've got a bad back - seek out Joe.")
instructor_repository.save(instructor5)
instructor6 = Instructor("Linda", "Thai Chi", "If you know, you know.")
instructor_repository.save(instructor6)

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

lesson1 = Lesson("Spin with Jim", datetime.date(2022, 9, 5), datetime.time(7, 00, 00), "60 mins", instructor1, "Spin Room", 20, "Rise and shine with an hour's intense spin class that'll have you hitting your VO2 max over and over again. Don't forget your own electrolyte drink and towel")
lesson_repository.save(lesson1)
lesson2 = Lesson("Peaceful Yoga", datetime.date(2022, 9, 7), datetime.time(17, 30, 00), "60 mins", instructor2, "Studio", 5, "Stretch off the stresses of mid-week with our restorative yoga hour")
lesson_repository.save(lesson2)
lesson3 = Lesson("Circuits", datetime.date(2022, 9, 6), datetime.time(12, 00, 00), "30 mins", instructor3, "Weights Room", 10, "Hit every muscle group with dynamic exercises across 10 stations in a short and sharp 30 minute circuits class")
lesson_repository.save(lesson3)
lesson4 = Lesson("Legs, Bums and Tums", datetime.date(2022, 9, 5), datetime.time(11, 00, 00), "45 mins", instructor4, "Studio", 6, "Wear your squat proof leggings for this one, folks. Unless you want to embarrass yourself")
lesson_repository.save(lesson4)
lesson5 = Lesson("The Core Essentials", datetime.date(2022, 9, 5), datetime.time(19, 00, 00), "45 mins", instructor5, "Weights Room", 10, "You use your core for everything, including drinking that beer. So give it the workout it deserves")
lesson_repository.save(lesson5)
lesson6 = Lesson("Thai Chi", datetime.date(2022, 9, 6), datetime.time(7, 00, 00), "45 mins", instructor6, "Studio", 5, "If you know, you know. All welcome")
lesson_repository.save(lesson6)

booking1 = Booking(lesson1, member2)
booking_repository.save(booking1)
booking2 = Booking(lesson2, member1)
booking_repository.save(booking2)
booking3 = Booking(lesson1, member4)
booking_repository.save(booking3)
booking4 = Booking(lesson4, member6)
booking_repository.save(booking4)
booking5 = Booking(lesson3, member4)
booking_repository.save(booking5)
booking6 = Booking(lesson6, member1)
booking_repository.save(booking6)
booking7 = Booking(lesson5, member3)
booking_repository.save(booking7)
booking8 = Booking(lesson2, member7)
booking_repository.save(booking8)
booking9 = Booking(lesson3, member5)
booking_repository.save(booking9)
booking10 = Booking(lesson6, member6)
booking_repository.save(booking10)