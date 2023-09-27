import numpy
import scipy

mat = numpy.array([[1, 2], [3, 4]])
print(mat)
invert_mat = numpy.linalg.inv(mat)
print(invert_mat)
print(mat @ invert_mat)

