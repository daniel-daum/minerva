# Question 1:
# Write a function skip_add that takes a single argument n and computes the sum of every other integer between 0 and n. Assume n is non-negative.
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.
    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    """
    if n <= 0:
        return 0
    else:
        return n + skip_add(n - 2)

# Question 2
# Recall the hailstone function from Lab 2. First, pick a positive integer n as the start. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)

    if n == 1:
        return 1
        
    if n % 2 == 0:
        a = hailstone(int(n / 2))
        return a + 1
    else:
        a = hailstone(int((n * 3) + 1))
        return a + 1

# Question 3
# Write a recursive implementation of summation, which takes a positive integer n and a function term. It applies term to every number from 1 to n including n and returns the sum of the results.
def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    """
    if n == 1:
        return term(1)

    else:
        return term(n) + summation(n - 1, term)

# Question 4
# Write a function is_prime that takes a single argument n and returns True if n is a prime number and Falseotherwise. Assume n > 1. We implemented this iteratively before, now time to do it recursively!
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def check(a):
        if a == 1:
            return True

        if n % a == 0:
            return False

        return check(a - 1)
    
    return check(n - 1)


# Question 5
def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a % b == 0:
        return b

    else:
        return gcd(b, a % b)


def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(5)
    8
    """

    if n == 1:
        return 1

    if n == 2:
        return 2

    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
