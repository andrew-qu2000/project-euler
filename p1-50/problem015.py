# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Represent movement as a sequence of Rights and Downs
# ex. R-R-D-D
# 4! ways to order a string of 4 chars, but order of same char does not matter
# So, for 2x2 grid, 4!/2!/2! = 6 routes

from math import factorial

def n_paths(width, height):
    steps = width + height
    return factorial(steps) // factorial(width) // factorial(height)

if __name__ == '__main__':
    print( n_paths(20,20))
