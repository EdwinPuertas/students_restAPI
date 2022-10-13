import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.student import Student


class StudentController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage.json')
        print('controller')

    def add(self, student: Student = Student()) -> None:
        # Serializing json
        json_object = json.dumps(student, indent=4)
        # Writing to sample.json
        with open(self.file, "w") as outfile:
            outfile.write(json_object)

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object