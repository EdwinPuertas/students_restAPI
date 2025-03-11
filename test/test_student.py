import unittest
from logic.student import Student


class TestStudent(unittest.TestCase):
person = Student(id=1, name='Name', surname='Surname')

    def test_instance(self):
        self.assertIsInstance(self.person, Student, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, 1)

    def test_name(self):
        self.assertEqual(self.person.name, "Name")

    def test_surname(self):
        self.assertEqual(self.person.surname, 'Surname')

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'id': 1, 'name': 'Name', 'surname': 'Surname'})

if __name__ == '__main__':
    unittest.main()
