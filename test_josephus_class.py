import unittest
from josephus_class import Josephus

class TestJosephus(unittest.TestCase):
    """针对约瑟夫类的测试"""

    def setUp(self):
        self.test_peoples = Josephus(10)

    def test_josephus_class_traverse(self):
        self.test_peoples.traverse_older(4,4)
        result = [7,1,5,10,6,3,2,4,9]
        self.assertEqual(self.test_peoples.traverse_older(4,4),result)
    
    def test_josephus_class_survivor(self):
        self.test_peoples.survivor(4,4)
        result = [8]
        self.assertEqual(self.test_peoples.survivor(4,4),result)


unittest.main()
