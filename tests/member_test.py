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

# This test worked but commenting out as it will keep adding to database each time I run the tests and they'll fail because this exists
    # def test_member_added_to_db(self):
    #     member = Member("Matt Thomson")
    #     member_repository.save(member)
    #     member_added = member_repository.select(member.id)
    #     # sql = "SELECT name FROM members WHERE id = %s"
    #     # values = [member.id]
    #     # results = run_sql(sql,values)
    #     self.assertEqual("Matt Thomson", member_added.name)

# This test worked but commenting out as it won't work as tests continue
    # def test_select_all_list(self):
    #     members = member_repository.select_all()
    #     self.assertEqual(4, len(members))

# This test worked, commenting out for future tests not to be affected
    # def test_delete_by_id(self):
    #     member_repository.save(self.member2)        
    #     member_repository.delete(self.member2.id)
    #     members = member_repository.select_all()
    #     self.assertEqual(5, len(members))

# This test worked, commenting out for future tests not to be affected
    # def test_delete_all(self):
    #     member_repository.delete_all()
    #     members = member_repository.select_all()
    #     self.assertEqual(0, len(members))        