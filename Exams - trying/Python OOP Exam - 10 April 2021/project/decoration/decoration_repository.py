# from project.decoration.plant import Plant


class DecorationRepository:

    def __init__(self):
        self.decoration = []

    def add(self, decoration):
        self.decoration.append(decoration)

    def remove(self, decoration):
        if decoration in self.decoration:
            self.decoration.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type):
        for deco in self.decoration:
            if decoration_type == deco.__class__.__name__:
                return deco
        return "None"

#
#
# d = DecorationRepository()
# d1 =d.add(Plant())
# print(d.decoration)
# a = d.find_by_type("Plant")
# print(a)