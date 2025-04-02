from itertools import count

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """

    count = lst.count(x)

    for _ in range(count):
        lst.append(el)


def group_by(seq, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """

    groups = {}

    for value in seq:
        modified_value = fn(value)

        if modified_value not in groups:
            groups[modified_value] = [value]

        if modified_value in groups:
            if value not in groups[modified_value]:
                groups[modified_value].append(value)

    return groups

def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    value = 0
    def add(j):
        nonlocal value
        result = n + j + value
        value += 1
        return result

    return add

def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    value = n

    def func(function):
        nonlocal value

        result = function(value)
        value = result

        return result

    return func


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.
    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>>
    12
    """
    current = 0
    next = 1

    def fib():
        nonlocal current
        nonlocal next

        result = current

        current, next = next, current + next
        return result

    return fib


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """


    password_attempts = []

    def withdraw(amount, passw):
        nonlocal balance

        if len(password_attempts) >= 3:
            locked = f"Your account is locked. Attempts: {password_attempts}"
            return locked

        if passw != password:
            password_attempts.append(passw)
            return 'Incorrect password'

        if amount > balance:
            return 'Insufficient funds'

        balance = balance - amount

        return balance

    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    check = withdraw(0, old_password)

    if type(check) == str:
        return check

    def joint_withdraw(amount, attempt_password):
        if attempt_password == new_password:
            return withdraw(amount, old_password)

        return withdraw(amount, attempt_password)

    return joint_withdraw
