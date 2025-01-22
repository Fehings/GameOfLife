# A Basic Game of Life in Python

import numpy as np


# Create a matrix. Initially hard code, ideally later add user input for size and initial conditons.
# This should be boolean

matrix = py.random.rand((10, 10))
matrix = matrix<mean(matrix) # convert to boolean matrix


# Now implement rules as a function

# If cell == 1, and sum(adjacent cells)< 2, the cell = 0

# If cell == 1, and sum(adjacent cells)>=2 and <=3, cell = 1

# If cell == 1, and sum(adjacent cells)>3, cell = 0

# If cell == 0 and sum(adjacent cells)==3, cell = 1



# main: For loop, this can be passed as an argument, start with 7 hard coded.
# For each generation pass the matrix to the function with above rules, return new matrix
# Ideally display graphically in a plot and (spy?) and update each loop (need to check how to get python to render this so we can see it)
# time delay?
