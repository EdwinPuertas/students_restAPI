class Student(object):
    """
    Class used to represent a Student
    """

    def __init__(self, id: int = 1, name: str = 'Name', surname: str = "surname") -> object:
        """ Person constructor object.

        :param id: id of student.
        :type id: str
        :param name: name of student.
        :type name: str
        :param surname: last name of student.
        :type surname: str
        :returns: Student object
        :rtype: object
        """
        self.__id = id
        self.__name = name
        self.__surname = surname

    @property
    def id(self) -> int:
        """ Returns id of the student.
          :returns: id of student.
          :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """ The id of the student.
        :param id: id of student.
        :type: int
        """
        self.__id = id

    @property
    def name(self) -> str:
        """ Returns the name of the student.
          :returns: name of student.
          :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """ The name of the student.
        :param name: name of student.
        :type: str
        """
        self.__name = name

    @property
    def surname(self) -> str:
        """ Returns the last name of the student.
          :returns: last name of student.
          :rtype: str
        """
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__surname = surname

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return {"id": self.id, "name": self.name, "surname": self.surname}


if __name__ == '__main__':

    edwin = Student(id=73577376, name="Edwin", surname="Puertas")
    print(edwin)

