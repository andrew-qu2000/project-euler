# Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

if __name__ == '__main__':
    # calculation is still trivial for computers
    # perhaps look for patterns in how digits double
    # ex. 1 -> 2 -> 4 -> 8 -> 1 + 6 (but where do we place the carrier 1?)
    # dictionary of digit:count

    num_str = str(2**1000)
    dig_sum = 0
    for c in num_str:
        dig_sum += int(c)
    print(dig_sum) # <1s
