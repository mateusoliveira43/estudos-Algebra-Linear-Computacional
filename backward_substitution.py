import numpy as np


def backward_substitution(matrix, vector):
    # fazer type hinting depois
    dimensions = matrix.shape
    n = dimensions[0]
    solution = np.zeros(n)
    solution[n-1] = vector[n-1]/matrix[n-1][n-1]
    for i in range(n-2, -1, -1):
        matrix_indexes = matrix[i][i+1:]
        solution_indexes = solution[i+1:]
        loop_sum = matrix_indexes * solution_indexes  # inner product
        solution[i] = (vector[i] - sum(loop_sum))/matrix[i][i]
    return solution


if __name__ == "__main__":
    # fazer mais testes e melhores (e automatizados)
    identity = np.eye(3)
    A = np.array([[1, -2, 1], [0, 1, 6], [0, 0, 1]])
    b = np.array([4, -1, 2])
    A2 = np.array([[7, 2, 2], [0, -2, 3], [0, 0, 4]])
    b2 = np.array([21, 1, 12])
    solution1 = backward_substitution(identity, b)
    solution2 = backward_substitution(A, b)
    solution3 = backward_substitution(A2, b2)
    print(solution1, solution2, solution3)
