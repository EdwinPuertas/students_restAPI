import unittest
import json
import ast
from unittest.mock import patch, mock_open
from logic.student_controller import StudentController
from logic.student import Student  # Asegúrate de que la clase Student está bien importada


class TestStudentController(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("json.dump")
    def test_add_student(self, mock_json_dump, mock_open_file):
        controller = StudentController()
        new_student = Student(idn=123, name="Name", surname="SurName")

        result = controller.add(new_student)

        mock_open_file.assert_called_once_with(controller.file, 'r+', encoding='utf-8')
        mock_json_dump.assert_called_once()  # Se asegura de que json.dump se ejecutó
        self.assertEqual(result, new_student)

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"idn": 123, "name": "Edwin", "surname": "Puertas"}]')

    def test_show_students(self, mock_open_file):
        controller = StudentController()

        result = controller.show()
        expected_data = '[{"idn": 123, "name": "Edwin", "surname": "Puertas"}]'

        mock_open_file.assert_called_once_with(controller.file, 'r')
        self.assertEqual(ast.literal_eval(result), ast.literal_eval(expected_data))


if __name__ == "__main__":
    unittest.main()