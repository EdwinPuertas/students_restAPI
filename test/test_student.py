import unittest
from logic.student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student(idn=123, name="Name", surname="SurName")

    def test_student(self):
        self.assertEqual(self.student.idn, 123)
        self.assertEqual(self.student.name, "Name")
        self.assertEqual(self.student.surname, "SurName")

    def test_string_student(self):
        with self.assertRaises(TypeError, msg="Student must be a string"):
            self.student.name = 'Name'
            self.student.surname = 'SurName'

    def test_int_student(self):
        with self.assertRaises(TypeError, msg="Student must be a integer"):

            self.student.idn = 123
if __name__ == '__main__':
    unittest.main()
