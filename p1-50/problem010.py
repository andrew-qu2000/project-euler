# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from problem007 import _primes, nth_prime

if __name__ == '__main__':
    cap = 2000000
    n = 1
    while _primes[n-1] < cap:
        # could double n to reduce the number of function calls
        # but that will calculate a lot of primes over the cap
        # should try adapting the method from problem007 to stop at a cap
        # instead of a nth term
        n += 1
        nth_prime(n)
    print(sum(_primes) - _primes[-1]) # about 8 seconds
