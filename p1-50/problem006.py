# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2 ^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... +10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is,
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_sqr_dif(n):
    # Is there a more mathematical approach?
    sum_of_sqr = sum([k**2 for k in range(1,n+1)])
    sqr_of_sum = (n * (n+1)//2)**2
    return abs(sum_of_sqr - sqr_of_sum)

if __name__ == '__main__':
    print(sum_sqr_dif(100))
