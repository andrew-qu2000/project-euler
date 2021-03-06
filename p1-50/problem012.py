# Highly divisible triangular number
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

from problem005 import prime_factors

def n_divisors(p_factorization):
    n_combinations = 1
    for p in p_factorization:
        deg = p_factorization[p]
        n_combinations *= deg + 1 # include zeroth power
    return n_combinations

if __name__ == '__main__':
    curr_nat, curr_tri = 1, 1
    target_divisors = 500
    found = False
    while not found:
        curr_nat += 1
        curr_tri += curr_nat
        p_f = prime_factors(curr_tri)
        n_d = n_divisors(p_f)
        if n_d > target_divisors:
            found = True
    print(curr_tri) # about 1.8s
