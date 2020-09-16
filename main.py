import numpy as np

A = np.random.randn(3, 3)
B = np.random.randn(3, 3)
print(A, np.linalg.cond(A), np.linalg.cond(A, 'fro'))
print(B, np.linalg.cond(B), np.linalg.cond(B, 'fro'))
