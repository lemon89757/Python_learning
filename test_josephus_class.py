import unittest
from josephus_class import Josephus


class TestJosephus(unittest.TestCase):
    """针对约瑟夫类的测试"""

    def setUp(self):
        self.test_peoples = Josephus(10)

    def test_josephus_class_traverse(self):
        result = self.test_peoples.traverse_order(4, 4)
        expect_result = [7, 1, 5, 10, 6, 3, 2, 4, 9]
        self.assertEqual(expect_result, result)

    def test_josephus_class_traverse_1(self):
        result = self.test_peoples.traverse_order(4, 1)
        expect_result = [4, 5, 6, 7, 8, 9, 10, 1, 2]
        self.assertEqual(expect_result, result)
    
    def test_josephus_class_survivor_2(self):
        result = self.test_peoples.survivor(4, 4)
        expect_result = [8]
        self.assertEqual(expect_result, result)


unittest.main
