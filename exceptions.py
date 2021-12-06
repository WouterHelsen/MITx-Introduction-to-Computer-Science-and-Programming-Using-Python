"""
an exception is an unexpected error or event that occurs while the program is running and changes the flow of execution.

We have four blocks:

try: this is the code that you will try to run. What happens after this depends on whether an exception was thrown or not.

except: this block handles the exception if it occurs when the try block is executed.

else: this code block runs only if no exceptions were thrown in the try block.

finally: this block always runs, even if there were exceptions in the try block. As noted in the lecture, this block if very helpful for “clean up code” such as closing files.
"""

try:
    a = int(input("Give a number: "))
    b = int(input("Give a second number: "))
    print("The first number divided by the second is", a/b)
    c = input("Give a letter: ")
    d = input("Give a second letter: ")
    print("The two letters concatenate together are ", c + d)

except ValueError:
    print("ValueError: an inappropriate value. We are expecting integers.")

except IndexError:
    print("IndexError: an object of inappropriate type. We are expecting integers.")

except ZeroDivisionError:
    print("Error: division by zero")

else:
    print("No exceptions were thrown!")

finally:
    print("Even with exceptions, this message always shows.")


def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0