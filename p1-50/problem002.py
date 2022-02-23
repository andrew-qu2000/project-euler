# Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def dynamic(n):
    fib_terms = {0:1, 1:2}
    even_sum = 0
    curr_key = 1
    curr_val = 2
    while curr_val <= n:
        if curr_val % 2 == 0:
            even_sum += curr_val
        curr_key += 1
        curr_val = fib_terms[curr_key-1] + fib_terms[curr_key-2]
        fib_terms[curr_key] = curr_val
    return even_sum

if __name__ == '__main__':
    print(dynamic(4000000))
