from datetime import datetime
from random import randint, seed

# CONST VALUES
primes = []

rectangles = []
points = []


# GENERATION
def generate_n():
    seed()
    return randint(0, 15)


def generate_point(n, i):
    seed()
    return [(primes[(randint(0, len(primes) - 1))] * i) ** 31 % (20 * n),
            (primes[(randint(0, len(primes) - 1))] * i) ** 31 % (20 * n)]


def generate_rectangle(n, i):
    return [10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)]


# COMPRESSION
def compress_coordinates():
    x = set({})
    y = set({})
    for rectangle in rectangles:
        x.add(rectangle[0])
        x.add(rectangle[2])
        y.add(rectangle[1])
        y.add(rectangle[3])

    x = sorted(list(x))
    y = sorted(list(y))

    compressed_rectangles = []
    for rectangle in rectangles:
        compressed_rectangles.append(
            [binary_search(0, len(x), rectangle[0], x), binary_search(0, len(y), rectangle[1], y),
             binary_search(0, len(x), rectangle[2], x), binary_search(0, len(y), rectangle[3], y)])

    return compressed_rectangles, x, y


def find_compressed(point, x, y):
    return [binary_search(0, len(x), point[0], x), binary_search(0, len(y), point[1], y)]


# ADDITIONAL FUNCTIONS
def binary_search(left, right, target, numbers):
    p = left + (right - left) // 2

    if left >= right:
        return right - 1

    if numbers[p] == target:
        return p

    if target > numbers[p]:
        return binary_search(p + 1, right, target, numbers)
    if target < numbers[p]:
        return binary_search(left, p, target, numbers)


def fillPrimes():
    global primes
    for i in range(10000, 40000):
        if isPrime(i): primes.append(i)


def isPrime(n):
    return (2 ** (n - 1) - 1) % n == 0


def printObj(obj):
    for i in obj:
        print(i)
    print()


def check_time(function, q):
    times = []
    for t in range(q):
        start = datetime.now()

        function()

        end = datetime.now()
        times.append((end - start).total_seconds())

    print(function)
    return f"{(sum(times) / len(times)):.5}"
