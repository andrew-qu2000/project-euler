# Maximum path sum 1
# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# NOTE: As there are only 16384 routes,
# it is possible to solve this problem by trying every route. However, Problem 67,
# is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)

if __name__ == '__main__':
    triangle = []
    with open('p067_triangle.txt', 'r') as f:
        for line in f:
            triangle.append([int(k) for k in line.split()])
    # starting at 2nd to last row, increment each number by the greater of
    # its two children. (If you reach this number in a route, you will always
    # take the greater child. Add the child's value and consider this the
    # parent's implicit value).
    # move up a row and repeat
    row_ind = len(triangle) - 2
    while row_ind >= 0:
        row = triangle[row_ind]
        below = triangle[row_ind + 1]
        for i in range(len(row)):
            row[i] += max(below[i], below[i+1])
        row_ind -= 1
    print(triangle[0][0])
