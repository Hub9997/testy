from itertools import count, islice
primes = (n for n in count(2) if all(n % d for d in range(2, n)))
print("100th prime is %d" % next(islice(primes, 99, 100)))