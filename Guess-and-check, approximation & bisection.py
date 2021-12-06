"""
Guess-and-check : runs through a while loop & does a guess and check, trying different versions of answers until it reaches a point close enough to the answer.
Approximation :
Bisection :

EXAMPLE : Square root
"""

def main():
    bisection_search()

#def guess_and_check():
    """
    input : asks for an integer
    output: gives the square root of input
    """
    answer = 0
    neg_flag = False
    x = int(input("Enter an integer: "))
    if x < 0 :
        neg_flaf = True
    while answer ** 2 < x :
        answer += 1
    if answer ** 2 == x :
        print("Square root of", x, "is", answer)
    else :
        print(x, "is not a perfect square")
        if neg_flag:
            print("Just checking... Did you mean", -x,"?")

#def approx_square_root():

def bisection_search():
    x = int(input("Enter an integer: "))
    epsilon = 0.01
    num_guesses = 0
    low = 1
    high = x
    answer = (low + high) / 2
    while abs(answer ** 2 - x ) >= epsilon:
        print("low = ", low, " high = ", high, " answer = ", answer)
        num_guesses += 1
        if answer ** 2 < x:
            low = answer
        else :
            high = answer
        answer = (low + high) / 2
    print("After", num_guesses, "guesses")
    print(answer, "is a very close approximation to the root of", x)

if __name__ == '__main__':
    main()


