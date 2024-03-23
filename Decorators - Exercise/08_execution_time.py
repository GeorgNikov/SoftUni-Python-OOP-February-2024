from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()  # gets the current time
        func(*args, **kwargs)
        end = time()  # gets the current time

        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0

    for x in range(start, end):
        total += x

    return total


@exec_time
def concatenate(strings):
    result = ""

    for string in strings:
        result += string

    return result


print(concatenate(["a" for i in range(10000000)]))