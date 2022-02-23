# Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# brute force
def foo(n):
    result = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print(n, ':', result)

# sum of multiples of k less than n
def sum_multiples(k, n):
    # find largest multiple of k less than n (exclude n)
    max_mult = (n-1) - (n-1) % k
    # find how many of k is in this multiple
    num_mults = max_mult // k
    # use summation formula on num_mult
    # find total number of k's in summation
    num_k = num_mults * (num_mults + 1) // 2
    return num_k * k

if __name__ == '__main__':
    # add multiples of 3 and 5
    # subtract multiples of 15 once (double counted)
    print(sum_multiples(3,1000) + sum_multiples(5,1000) - sum_multiples(15,1000))
