try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise

import numpy as np
import math
from lu_factorization import lu_factorization as lu

# Eliminção Gaussiana


def cholesky_gaussian_elimination(matrix):
    LU = lu(matrix)
    D = np.diagflat(np.diag(LU[1]))
    result = []
    result.append(LU[0])
    result.append(D)
    result.append(LU[0].transpose())

    return result

#  A = GG^T


def cholesky_equality(matrix):
    dimensions = matrix.shape
    n = dimensions[0]
    G = np.zeros((n, n))
    G[0, 0] = math.sqrt(matrix[0, 0])
    for j in range(1, n):
        G[j, 0] = matrix[j, 0]/G[0, 0]
    for i in range(1, n):
        loop_sum_1 = G[i, 0:i] * G[i, 0:i]
        G[i, i] = math.sqrt(matrix[i, i] - sum(loop_sum_1))
        for j in range(2, n):
            loop_sum_2 = G[i, 0:i] * G[j, 0:i]
            G[j, i] = (matrix[j, i] - sum(loop_sum_2))/G[i, i]

    return G
