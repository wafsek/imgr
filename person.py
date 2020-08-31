class Person:
    """A Person class"""

    def __init__(self, firstname=None, middle_name=None, lastname=None, gender=None, dob=None, tlf=None, email=None):
        self.firstname = firstname
        self.middle_name = middle_name
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        self.tlf = tlf
        self.email = email

    @property
    def fullname(self):
        return '{}{}{}'.format((self.firstname, self.middle_name, self.lastname))
