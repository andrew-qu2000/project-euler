# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_common_multiple(n):
    # highest occurrences of each prime factor in numbers 2 to n
    prime_count_high = {}
    # prime factorize from 2 to n
    for i in range(2,n+1):
        factors = prime_factors(i)
        for f in factors:
            if f in prime_count_high:
                prime_count_high[f] = max(prime_count_high[f],factors[f])
            else:
                prime_count_high[f] = factors[f]
    prod = 1
    for p in prime_count_high:
        prod *= p**prime_count_high[p]
    return prod

def prime_factors(n):
    factors = {}
    i = 2
    dividend = n
    while i <= dividend:
        if dividend % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            dividend //= i
            i = 2
        else:
            i += 1
    return factors

if __name__ == '__main__':
    print( prime_factors(2520) )
    print( smallest_common_multiple(20) )
