import numpy as np

A = np.random.randn(3, 3)
B = np.random.randn(3, 3)
C = np.random.randn(3, 1)
print(type(A), A.shape, type(A.shape))
print(C, C[0])
print()
print(A, A[0], A[0][0])
print()
print(A, np.linalg.cond(A), np.linalg.cond(A, 'fro'))
print(B, np.linalg.cond(B), np.linalg.cond(B, 'fro'))
print()
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
print(x1)
print(x2)
print(np.multiply(x1, x2))
print()
