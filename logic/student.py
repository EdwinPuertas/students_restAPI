class Student:
    """Represents a student with an ID, first name, and surname."""

    def __init__(self, idn: int = 1, name: str = "name", surname: str = "surname"):
        """
        Initialize a new Student instance.

        Args:
            idn (int): The student's unique identifier.
            name (str): The student's first name.
            surname (str): The student's surname.
        """
        self._idn = idn
        self._name = name
        self._surname = surname

    @property
    def idn(self) -> int:
        """Get the student's ID."""
        return self._idn

    @idn.setter
    def idn(self, val: int):
        """Set the student's ID."""
        self._idn = val

    @property
    def name(self) -> str:
        """Get the student's first name."""
        return self._name

    @name.setter
    def name(self, val: str):
        """Set the student's first name."""
        self._name = val

    @property
    def surname(self) -> str:
        """Get the student's surname."""
        return self._surname

    @surname.setter
    def surname(self, val: str):
        """Set the student's surname."""
        self._surname = val

    def to_dict(self) -> dict:
        """
        Return a clean dictionary representation of the student.

        Returns:
            dict: A dictionary with keys 'idn', 'name', and 'surname'.
        """
        return {
            'idn': self.idn,
            'name': self.name,
            'surname': self.surname
        }

    def __str__(self) -> str:
        """
        Return a string representation of the student.

        Returns:
            str: A stringified clean dictionary of the student's attributes.
        """
        return str(self.to_dict())



if __name__ == '__main__':

    edwin = Student(idn=23456, name="Edwin", surname="Puertas")
    print(edwin)
    juan = Student()
    print(juan)

