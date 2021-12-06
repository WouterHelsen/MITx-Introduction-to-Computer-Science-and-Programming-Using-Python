"""
The function polysum takes 2 arguments, n and s. This function sums the area and square of the perimeter of the regular
polygon. The function returns the sum, rounded to 4 decimal places.
"""
import math

def main():
    n = float(input("Number of sides = "))
    s = float(input("Length of sides = "))
    print("The sum of the area and the square of the perimeter of the regular polygon is", polysum(n, s))

def polysum(n, s):
    """
    :param n: Number of sides
    :param s:  Lenght of sides
    :return: sum of the area and the square of the perimeter of the regular polygon, rounded to 4 decimal places.
    """
    area = (0.25 * n * (s ** 2)) / (math.tan(math.pi / n))
    perimeter = n * s
    return round(area + perimeter ** 2, 4)

if __name__ == '__main__':
    main()
