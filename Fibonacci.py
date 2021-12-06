def fib(x):
    """
    returns fibonacci number for x with a recursive function
    """
    global num_fib_calls

    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

def fib_efficient(x, d):
    """
    returns fibonacci number for x with a recursive function, but is using a dictionary d (memoization) to make the function more efficient
    (and much faster!).
    """
    global num_fib_calls

    num_fib_calls += 1
    if x in d:
        return d[x]
    else :
        answer = fib_efficient(x - 1, d) + fib_efficient(x - 2, d)
        d[x] = answer
        return answer

"""
num_fib_calls will keep track of the number of runs each function has to do before returning the anwser.
Notice how fib(x) has to run exponentially more runs for higher numbers, slowing it down drastically in comparison with
fib_efficient(x, d) using a dictionary to store previous results. 
"""

num_fib_calls = 0
x = int(input("number = "))
print(fib(x))
print(num_fib_calls)
num_fib_calls = 0
d = {1: 1, 2: 2}
print(fib_efficient(x, d))
print(num_fib_calls)

