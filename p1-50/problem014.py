# Longest Collatz Sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# store calculated Collatz sequence lengths
# _chain_lengths[n] = Collatz sequence length with n as starting number
_chain_lengths = {1:1}

def solve_chain(n):
    if n in _chain_lengths:
        return _chain_lengths[n]
    if n % 2 == 0:
        _chain_lengths[n] = 1 + solve_chain(n//2)
    else:
        _chain_lengths[n] = 1 + solve_chain(3*n + 1)
    return _chain_lengths[n]

if __name__ == '__main__':
    num = 1
    cap = 1000000
    max_len, max_start = 1, 1
    while num < cap:
        num += 1
        chain_len = solve_chain(num)
        if chain_len > max_len:
            max_len = chain_len
            max_start = num
    print(max_start) # about 1.4s
