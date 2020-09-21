import numpy as np


def foward_substitution(matrix, vector):
    # fazer type hinting depois
    dimensions = matrix.shape
    n = dimensions[0]
    solution = np.zeros(n, 1)
    solution[0] = vector[0]/matrix[0][0]
    for i in range(1, n-1):
        vector_sum = np.zeros(i, 1)  # evitar fazer outro for
        solution[i] = (vector[i] - sum(vector_sum))/matrix[i][i]
    return solution

# Fazer testes
