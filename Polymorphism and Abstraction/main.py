class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_area(self):
        print("Calc circle area")


class Triangle(Shape):
    def calculate_area(self):
        print("Calc triangle area")


class Square(Shape):
    def calculate_area(self):
        print("Calc square area")


shapes = [Triangle(), Circle(), Circle(), Square()]

for s in shapes:
    s.calculate_area()
