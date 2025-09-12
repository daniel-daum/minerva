# Question 1
# Write a function lambda_curry2 that will curry any two argument functions using lambdas. See the doctest or refer to the textbook Links to an external site. if you're not sure what this means.
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)

# Question 2
# Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on that number returns True.
def keep_ints(cond, n):
   """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
   i = 1
   while i <= n:
        if cond(i):
            print(i)
        i+= 1


# Question 3
# Write a function similar to keep_ints like before, but now it takes in a number n and returns a function that has one parameter cond. The returned function prints out numbers from 1 to n where calling cond on that number returns True. 
def make_keeper(n): 
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n  where calling cond(i) returns True.
    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def some_func(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return some_func

# Question 4
# Write a function and_add that takes a one-argument function f and a number n as arguments. It should return a function that takes one argument, and does the same thing as the function f, except also adds n to the result.
def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """

    return lambda x: f(x) + n

# # Question 5
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f

make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)
