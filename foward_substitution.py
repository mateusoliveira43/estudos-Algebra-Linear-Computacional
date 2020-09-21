import numpy as np


def foward_substitution(matrix, vector):
    # fazer type hinting depois
    dimensions = matrix.shape
    n = dimensions[0]
    solution = np.zeros(n)
    solution[0] = vector[0]/matrix[0][0]
    for i in range(1, n):
        matrix_indexes = matrix[i][:i]
        solution_indexes = solution[:i]
        loop_sum = matrix_indexes * solution_indexes  # inner product
        solution[i] = (vector[i] - sum(loop_sum))/matrix[i][i]
    return solution


if __name__ == "__main__":
    # fazer mais testes e melhores (e automatizados)
    identity = np.eye(3)
    A = np.array([[-1, 0, 0], [2, 3, 0], [-1, 4, -5]])
    b = np.array([-1, 8, -8])
    solution1 = foward_substitution(identity, b)
    solution2 = foward_substitution(A, b)
    print(solution1, solution2)
