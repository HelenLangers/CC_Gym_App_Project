import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("Mike Langridge")
        self.member2 = Member("Helen Langridge")

    def test_member1_has_name(self):
        self.assertEqual("Mike Langridge", self.member1.name)