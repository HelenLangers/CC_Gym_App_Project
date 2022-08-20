import unittest
from models.member import Member
import repositories.member_repository as member_repository
from repositories.member_repository import *
from db.run_sql import run_sql

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("Mike Langridge")
        self.member2 = Member("Helen Langridge")

    def test_member1_has_name(self):
        self.assertEqual("Mike Langridge", self.member1.name)

    def test_member_added_to_db(self):
        member = Member("Matt Thomson")
        member_repository.save(member)
        member_repository.select(member.id)
        # sql = "SELECT name FROM members WHERE id = %s"
        # values = [member.id]
        # results = run_sql(sql,values)
        self.assertEqual("Matt Thomson", member.name)