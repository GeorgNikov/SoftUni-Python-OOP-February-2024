from project import Employee
from project import Person


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."