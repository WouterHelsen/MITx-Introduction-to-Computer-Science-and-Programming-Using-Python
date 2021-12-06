def generate_n(s):
    yield s
    yield from generate_n(s+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n != 0)

p = sieve(generate_n(2))
primes = []
for i in range(100): #WATCH OUT: RecursionError: maximum recursion depth exceeded
    prime = next(p)
    primes.append(prime)

print(primes)