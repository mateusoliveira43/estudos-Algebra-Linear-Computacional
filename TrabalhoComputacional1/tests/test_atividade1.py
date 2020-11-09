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

import timeit
import numpy as np
from atividade1 import cholesky_gaussian_elimination, cholesky_equality

A = np.array([[1, -2, 1, 1], [-2, 8, -4, -6], [1, -4, 6, 5], [1, -6, 5, 7]])
lista_teste = [A]
for i in range(5):
    lista_teste.append(np.eye(1000))
# Testes com a eliminação Gaussiana


def test_gaussian_elimination(matrix):
    LDLT = cholesky_gaussian_elimination(matrix)
    raiz_D = np.sqrt(LDLT[1])
    G = LDLT[0].dot(raiz_D)
    return G

# Testes com A = GG^T


def test_equality(matrix):
    G = cholesky_equality(matrix)
    return G


if __name__ == "__main__":

    inicio2 = timeit.default_timer()
    for teste in lista_teste:
        test_equality(teste)
    fim2 = timeit.default_timer()
    print(f'tempo decorrido usando igualdade A = GG^T: {fim2-inicio2}')

    inicio = timeit.default_timer()
    for teste in lista_teste:
        test_gaussian_elimination(teste)
    fim = timeit.default_timer()
    print(f'tempo decorrido usando eliminação gaussiana: {fim-inicio}')
