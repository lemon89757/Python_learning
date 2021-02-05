import unittest
from person_class import Person
from josephus_class import Josephus


class TestJosephus(unittest.TestCase):
    """针对约瑟夫类的测试"""

    def setUp(self):
        self.test_peoples = Person()
        self.test_peoples_info = self.test_peoples.get_persons_info()
        self.test_josephus = Josephus(2, 5)

    def test_append_1(self):
        result = self.test_josephus.appends(self.test_peoples_info)
        expected_result = [['Aa', 'male', 11], ['Bb', 'female', 12], ['Cc', 'female', 13], ['Dd', 'male', 14],
                           ['Ee', 'male', 15], ['Ff', 'male', 16], ['Gg', 'male', 17], ['Hh', 'female', 18],
                           ['Ii', 'male', 19], ['Jj', 'male', 20], ['Kk', 'female', 21], ['Ll', 'female', 22],
                           ['Nn', 'female', 23], ['Mm', 'male', 24]]
        self.assertEqual(expected_result, result)

    def test_append_2(self):
        person_1 = Person('Aa', 'male', 10).list_person_info()
        result = self.test_josephus.appends(person_1)
        expected_result = [['Aa', 'male', 10]]
        self.assertEqual(expected_result, result)

    def test_erase(self):
        self.test_josephus.appends(self.test_peoples_info)
        result = self.test_josephus.erase(2)
        expected_result = ['Bb', 'female', 12]
        self.assertEqual(expected_result, result)

    def test_killed_order(self):
        self.test_josephus.appends(self.test_peoples_info)
        result = self.test_josephus.killed_order()
        expected_result = [['Ff', 'male', 16], ['Kk', 'female', 21], ['Bb', 'female', 12], ['Hh', 'female', 18],
                           ['Mm', 'male', 24], ['Gg', 'male', 17], ['Aa', 'male', 11], ['Jj', 'male', 20],
                           ['Ee', 'male', 15], ['Dd', 'male', 14], ['Ii', 'male', 19], ['Nn', 'female', 23],
                           ['Cc', 'female', 13]]
        self.assertEqual(expected_result, result)

    def test_get_survivor(self):
        self.test_josephus.appends(self.test_peoples_info)
        result = self.test_josephus.get_survivor()
        expected_result = [['Ll', 'female', 22]]
        self.assertEqual(expected_result, result)

    def test_iterator_iter(self):
        self.test_josephus.appends(self.test_peoples_info)
        result = []
        for person in self.test_josephus:
            result.append(person)
        expected_result = [['Ff', 'male', 16], ['Kk', 'female', 21], ['Bb', 'female', 12], ['Hh', 'female', 18],
                           ['Mm', 'male', 24], ['Gg', 'male', 17], ['Aa', 'male', 11], ['Jj', 'male', 20],
                           ['Ee', 'male', 15], ['Dd', 'male', 14], ['Ii', 'male', 19], ['Nn', 'female', 23],
                           ['Cc', 'female', 13], ['Ll', 'female', 22]]
        self.assertEqual(expected_result, result)

    def test_iterator_yield(self):
        self.test_josephus.appends(self.test_peoples_info)
        result = []
        for person in self.test_josephus.iterator_josephus():
            result.append(person)
        expected_result = [['Ff', 'male', 16], ['Kk', 'female', 21], ['Bb', 'female', 12], ['Hh', 'female', 18],
                           ['Mm', 'male', 24], ['Gg', 'male', 17], ['Aa', 'male', 11], ['Jj', 'male', 20],
                           ['Ee', 'male', 15], ['Dd', 'male', 14], ['Ii', 'male', 19], ['Nn', 'female', 23],
                           ['Cc', 'female', 13], ['Ll', 'female', 22]]
        self.assertEqual(expected_result, result)


unittest.main
