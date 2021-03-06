import numpy as np
from pprint import pprint
import timeit


def lu_factorization(matrix):
    # fazer type hinting depois
    dimensions = matrix.shape
    n = dimensions[0]
    lower_matrix = np.eye(n)

    for i in range(n-1):
        for k in range(i+1, n):
            lower_matrix[k][i] = matrix[k][i]/matrix[i][i]
            for j in range(i+1, n):
                matrix[k][j] = matrix[k][j] - lower_matrix[k][i]*matrix[i][j]
    upper_matrix = np.triu(matrix)

    result = []
    result.append(lower_matrix)
    result.append(upper_matrix)
    return result


def exibe_testes(matrix, name_matrix):
    inicio = timeit.default_timer()
    lu_factorization_matrix = lu_factorization(matrix)
    fim = timeit.default_timer()
    print(f'matriz {name_matrix}:')
    pprint(matrix)
    print(f'matriz triangular inferior da fatoração LU de {name_matrix}:')
    pprint(lu_factorization_matrix[0])
    print(f'matriz triangular superior da fatoração LU de {name_matrix}:')
    pprint(lu_factorization_matrix[1])
    print(f'tempo decorrido: {fim-inicio}')
    print()


if __name__ == "__main__":
    # fazer mais testes e melhores (e automatizados)
    identity = np.eye(3)
    A = np.array([[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]])
    B = np.array([[2, 2, 2], [4, 7, 7], [6, 18, 22]])
    exibe_testes(A, 'A')
    exibe_testes(B, 'B')
    exibe_testes(identity, 'I')
