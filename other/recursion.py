"""
x = factorial (5);
x = (5 * factorial (4));
x = (5 * (4 * factorial (3)));
x = (5 * (4 * (3 * factorial (2))));
x = (5 * (4 * (3 * (2 * factorial (1)))));
"""


def factorial(n):
    # print(f"factorial() called with n = {x}")
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        # print(f"-> factorial({x}) returns {res}")
        return res


print(factorial(3))


def fib(n):
    if n < 0:
        return None
    result = 1
    for n in range(1, n + 1):
        result *= n
    return result
