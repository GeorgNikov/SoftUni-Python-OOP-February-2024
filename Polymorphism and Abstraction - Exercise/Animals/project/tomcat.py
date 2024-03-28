from project import Cat


class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, self.gender_is())

    @staticmethod
    def make_sound():
        return "Hiss"

    @staticmethod
    def gender_is():
        return "Male"
