class Cat:

    def __init__(self, name):
        self.name = name


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return f"{self.name} {other.name}"

    def __lt__(self, other):
        return len(self.name) < len(other.name)


p = Person("Gosho")
p2 = Person("Ivan")
c = Cat("Muncho")
print(p + p2)
print(p + c)
print(len(p))
print(p < p2)
print(p < c)
