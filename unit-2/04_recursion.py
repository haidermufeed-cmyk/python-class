def product_to_one(value):
    if value == 1 or value == 0:
        return 1
    return value * product_to_one(value - 1)


number = 5
print("Product result:", product_to_one(number))


def show_steps(value, spaces=""):
    print(spaces + "Processing:", value)

    if value <= 1:
        print(spaces + "Finished")
        return 1

    answer = value * show_steps(value - 1, spaces + "  ")
    print(spaces + "Result:", answer)
    return answer


show_steps(4)


def reverse_count(value):
    if value == 0:
        print("Start!")
        return

    reverse_count(value - 1)
    print(value)


reverse_count(4)


def sequence(a, b, terms):
    if terms == 0:
        return

    print(a, end=" ")

    sequence(b, a + b, terms - 1)


print("Fibonacci:")
sequence(0, 1, 8)
print()


def factorial_with_loop(value):
    answer = 1

    while value > 1:
        answer *= value
        value -= 1

    return answer


def factorial_with_recursion(value):
    if value <= 1:
        return 1

    return value * factorial_with_recursion(value - 1)


print("Loop result:", factorial_with_loop(6))
print("Recursive result:", factorial_with_recursion(6))