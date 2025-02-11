def sum_nats(n):
    if n == 0:
        return 0
    else:
        return n + sum_nats(n - 1)

def count_up(n):
    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        print(n)


def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n % 10
        rest = int(n // 10)
        return last + sum_digits(rest)
#  I learned that modulo 10 just always returns the last digit of a number
#  I learned that you can divide by ten for integer math to get anything but last
#  I learned that to check for a single digit, i can just check for lesst than 10
    
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

# Alot of recursion also relies on the fact that stuff after the call
# only occurs after the entire stack recturns, as in the case of the cascade function
