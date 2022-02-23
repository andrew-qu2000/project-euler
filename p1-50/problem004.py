# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

if __name__=='__main__':
    # theres gotta be a more elegant way...
    res = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod = str(i * j)
            if prod == prod[-1::-1]:
                res = max(res, int(prod))
    print(res)
