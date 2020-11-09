import numpy as np
from pprint import pprint
import timeit


def lu_factorization_partial_pivoting(matrix):
    # fazer type hinting depois
    dimensions = matrix.shape
    n = dimensions[0]
    lower_matrix = np.eye(n)
    permutation_matrix = np.eye(n)

    for i in range(n-1):
        # Pivoteamento parcial
        max_coluna = np.max(np.absolute(matrix[i:, i]))
        indice_max_coluna = np.argmax(np.absolute(matrix[i:, i]))+i
        if max_coluna == 0:
            print('matriz singular, não pode ser feito a eliminação gaussiana')
            return ['', '', '']
        if indice_max_coluna != i:
            indice_subida = np.argmax(permutation_matrix[indice_max_coluna, :])
            indice_descida = np.argmax(permutation_matrix[i, :])
            permutation_matrix[i, indice_descida] = 0
            permutation_matrix[i, indice_subida] = 1
            permutation_matrix[indice_max_coluna, indice_descida] = 1
            permutation_matrix[indice_max_coluna, indice_subida] = 0
            permutation_matrix.dot(matrix)

        for k in range(i+1, n):
            lower_matrix[k][i] = matrix[k][i]/matrix[i][i]
            for j in range(i+1, n):
                matrix[k][j] = matrix[k][j] - lower_matrix[k][i]*matrix[i][j]
    upper_matrix = np.triu(matrix)

    result = []
    result.append(permutation_matrix)
    result.append(lower_matrix)
    result.append(upper_matrix)
    return result


def exibe_testes(matrix, name_matrix):
    inicio = timeit.default_timer()
    lu_factorization_matrix = lu_factorization_partial_pivoting(matrix)
    fim = timeit.default_timer()
    print(f'matriz {name_matrix}:')
    pprint(matrix)
    print(f'matriz de permutação de {name_matrix}:')
    pprint(lu_factorization_matrix[0])
    print(
        'matriz triangular inferior da fatoração LU com pivoteamneto'
        f' parcial de {name_matrix}:')
    pprint(lu_factorization_matrix[1])
    print(
        'matriz triangular superior da fatoração LU com pivoteamento'
        f'parcial de {name_matrix}:')
    pprint(lu_factorization_matrix[2])
    print(f'tempo decorrido: {fim-inicio}')
    print()


if __name__ == "__main__":
    # fazer mais testes e melhores (e automatizados)
    identity = np.eye(3)
    A = np.array([[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]])
    B = np.array([[2, 2, 2], [4, 7, 7], [6, 18, 22]])
    E = np.array([[0, 1], [0, 1]])
    P = np.array([[1E-4, 1], [1, 1]])
    exibe_testes(A, 'A')
    exibe_testes(B, 'B')
    exibe_testes(identity, 'I')
    exibe_testes(E, 'Erro')
    exibe_testes(P, 'Pivoteamento')
