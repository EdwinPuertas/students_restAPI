class Student(object):
    """
    Class used to represent a Student
    """

    def __init__(self, idn: int = 1, name: str = 'Name', surname: str = "surname") -> object:
        """ Person constructor object.

        :param idn: A unique number that uniquely identifies the student in the system.
        :type idn: int
        :param name: name of student.
        :type name: str
        :param surname: last name of student.
        :type surname: str
        :returns: Student object
        :rtype: object
        """
        self.__idn = idn
        self.__name = name
        self.__surname = surname

    @property
    def idn(self) -> int:
        """ Returns idn of the student.
          :returns: idn of student.
          :rtype: int
        """
        return str(self.__idn)

    @idn.setter
    def idn(self, val: int):
        """ The id of the student.
        :param id: id of student.
        :type: int
        """
        self.__idn = val

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
        return dict(idn=self.idn, name=self.name, surname=self.surname).__str__()

if __name__ == '__main__':

    edwin = Student(idn=23456, name="Edwin", surname="Puertas")
    print(edwin)
    juan = Student()
    print(juan)

