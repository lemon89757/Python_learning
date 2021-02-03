import unittest
from person_class import Person


class TestPerson(unittest.TestCase):
    """针对人类的测试"""

    def setUp(self):
        self.test_group = Person()

    def test_get_name(self):
        result = self.test_group.get_name(5)
        expected_result = "Ee"
        self.assertEqual(expected_result, result)

    def test_get_age(self):
        result = self.test_group.get_age(7)
        expected_result = 17
        self.assertEqual(expected_result, result)

    def test_get_gender(self):
        result = self.test_group.get_gender(8)
        expected_result = "female"
        self.assertEqual(expected_result, result)

    def test_get_persons_number(self):
        result = self.test_group.get_persons_number()
        expected_result = 14
        self.assertEqual(expected_result, result)

    def test_get_person_info(self):
        result = self.test_group.get_person_info(10)
        expected_result = ['Jj', 'male', 20]
        self.assertEqual(expected_result, result)


unittest.main
