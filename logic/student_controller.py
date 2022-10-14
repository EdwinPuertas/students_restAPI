import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.student import Student


class StudentController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage.json')

    def add(self, student: Student = Student()) -> str:
        with open(self.file, 'r+') as openfile:
            data = json.load(openfile)
            data['students'].append(student)
            openfile.seek(0)
            json.dumps(data)
        openfile.close()
        return str(data)

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object