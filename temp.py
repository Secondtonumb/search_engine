import numpy as np
from numpy import newaxis
from pprint import pprint
# a = np.ones((3, 1, 2), dtype=np.int16)

# pprint(a)
# pprint(b)
# c = a + b
# a = np.array([4, 2])
# b = np.array([3, 1])
# c = np.hstack((a, b))
# d = np.vstack((a, b))
# a_ = a[:, newaxis]
# b_ = b[:, newaxis]
# e = np.column_stack((a, b))
# e = np.hstack((a_, b_))
# print(e)
a = np.linspace(1, 25, 25).reshape(5, 5)
j = np.array([[1, 3],[2, 4]])
print(a[j, j])
