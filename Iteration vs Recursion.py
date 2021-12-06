"""
Iteration : Looping construct that updates itself after every iteration of the loop.
Recursion : A function that is calling on itself to solve a problem until a base case is reached.

EXAMPLE : Factorials
"""
def main():
    #a = 5
    #b = 5
    #n = 5
    #print(a,"*", b,"=", iter_multiply(a, b))
    #print(str(n)+"! =", iter_facorial(n))
    #print(str(n)+"! =", recur_factorial(n))

    #base = float(input("base ="))
    #exp = float(input("exp ="))
    #print(iterPower(base, exp))

    #a = int(input("a = "))
    #b = int(input("b = "))
    #print("de grootste gemeenschappelijke deler van", a, "en", b, "is", gcdIter(a, b))

    while True:
        x = int(input("Give a number : "))
        print(fib(x), "is the", x, "number of the Fibonacci sequence.")

def iter_multiply(a, b):
    """
    multiply a * b with an Iterative algorithm
    """
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def iter_facorial(n):
    """
    Give the factorial of n!
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def recur_factorial(n):
    """
    Give the factorial of n!
    """
    if n == 0 or n==1:
        return 1
    else:
        return n * recur_factorial(n-1)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b :
        x = a
        y = b
    else :
        x = b
        y = a
    for i in range(y):
        z = y - i
        if x % z == 0 and y % z == 0:
            return z


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

if __name__ == '__main__':
    main()