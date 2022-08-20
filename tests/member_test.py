import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def SetUp(self):
        self.member1 = Member("Mike Langridge")
        self.member2 = Member("Helen Langridge")