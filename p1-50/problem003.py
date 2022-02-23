# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def largest_prime(n):
    if n < 2:
        return None
    for i in range(2,n):
        if n % i == 0: # is a factor
            return largest_prime(n//i)
    return n

if __name__=='__main__':
    print(largest_prime(27473))
