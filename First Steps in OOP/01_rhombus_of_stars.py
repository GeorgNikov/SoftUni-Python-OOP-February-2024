def draw_top(size):
    for i in range(1, size + 1):
        print(f"{' ' * (size - i)}{'* ' * i}")


def draw_bottom(size):
    for i in range(size - 1, 0, -1):
        print(f"{' ' * (size - i)}{'* ' * i}")


def draw_rhombus(size):
    draw_top(size)
    draw_bottom(size)


size = int(input())
draw_rhombus(size)
