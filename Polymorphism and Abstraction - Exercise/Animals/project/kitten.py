from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, self.gender_is())

    @staticmethod
    def make_sound():
        return "Meow"

    @staticmethod
    def gender_is():
        return "Female"
