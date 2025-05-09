import json
import os
import ast
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.student import Student


class StudentController(object):

    def __init__(self):
        self.file = os.path.join(DIR_DATA, 'storage.json')

    def add(self, new_student: Student = Student()) -> dict:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.append(new_student.to_dict())  # ✅ guardar como diccionario (objeto JSON)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()  # elimina datos sobrantes si el nuevo json es más corto

        return new_student.to_dict()

    def show(self):
        with open(self.file, 'r', encoding='utf-8') as openfile:
            data = json.load(openfile)
        return data  # ✅ devolver directamente como lista de objetos