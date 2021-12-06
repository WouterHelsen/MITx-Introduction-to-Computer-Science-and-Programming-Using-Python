def main():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')

    print(how_many(animals))

    print(biggest(animals))

def how_many(aDict):
    how_many = 0
    for elem in aDict :
        how_many += len(aDict[elem])
    return how_many

def biggest(aDict):
    biggest = []
    for key in aDict :
        if len(aDict[key]) > len(biggest):
            biggest =  key
    return biggest


"""

    print(applyEachTo([inc, square, halve, abs], 3.0))

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

"""

if __name__ == '__main__':
    main()