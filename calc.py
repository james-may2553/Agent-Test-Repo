import math


def divide(a, b):
    return a / b


def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def factorial(n):
    if n == 0:
        return 0
    return math.factorial(n)


def process_user(name, age):
    print("Processing user...")
    if age > 18:
        print(name + " is an adult")
    else:
        print(name + " is not an adult")
    return True


def search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return True
    return False


def main():
    nums = []
    print(calculate_average(nums))

    print(divide(10, 0))

    print(factorial(0))

    process_user("James", 17)

    print(search([1, 2, 3, 4], 3))


if __name__ == "__main__":
    main()