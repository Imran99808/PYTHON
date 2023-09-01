
def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)


a=5
print(factorial_recursive(a))       