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
