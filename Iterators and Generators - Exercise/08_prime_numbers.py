from math import sqrt

def get_primes(numbers):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


print(list(get_primes([-2, 0, 0, 1, 1, 0])))