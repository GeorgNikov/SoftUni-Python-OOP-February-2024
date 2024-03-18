def read_next(*args):
    for seq in args:
        yield from seq


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)