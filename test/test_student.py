import unittest
from logic.student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student(idn=123, name="Name", surname="SurName")

    def test_student(self):
        self.assertEqual(self.student.idn, 123)
        self.assertEqual(self.student.name, "Name")
        self.assertEqual(self.student.surname, "SurName")


if __name__ == '__main__':
    unittest.main()
