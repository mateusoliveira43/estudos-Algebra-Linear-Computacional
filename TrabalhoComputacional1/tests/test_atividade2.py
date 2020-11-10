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
from atividade1 import cholesky_equality
from backward_substitution import backward_substitution
from foward_substitution import foward_substitution


def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)


ordens = [11, 101, 1001]  # 1/h + 1
# Cálculo das soluções aproximadas
ponto_inicial = 0
ponto_final = 1
for ordem in ordens:
    particionamemto = np.linspace(ponto_inicial, ponto_final, ordem)
    uns = np.ones(ordem)
    # Matriz A
    low = np.ones(ordem-1)*-1
    mid = np.ones(ordem)*2
    high = np.ones(ordem-1)*-1
    A = tridiag(low, mid, high)
    G = cholesky_equality(A)
    b1 = np.multiply(np.power(particionamemto, 2), np.exp(particionamemto))
    b2 = 2*(np.divide(np.sin(math.pi*particionamemto), np.power(particionamemto, 3)) - math.pi*np.divide(np.cos(math.pi*particionamemto), np.power(particionamemto, 2))) - math.pi**2*np.divide(np.sin(math.pi*particionamemto), particionamemto)
    b3 = 3*np.power(particionamemto, 3) - 10*np.power(particionamemto, 2) + uns
    # Sistema trinagular inferior
    c1 = foward_substitution(G, b1)
    c2 = foward_substitution(G, b2)
    c3 = foward_substitution(G, b3)
    # Sistema trinagular superior
    y1 = backward_substitution(G.transpose(), c1)
    y2 = backward_substitution(G.transpose(), c2)
    y3 = backward_substitution(G.transpose(), c3)
    solucao_exata1 = np.multiply(np.exp(particionamemto), np.power(particionamemto, 2)-4*particionamemto+6*uns)+6*(particionamemto-uns)-3*math.exp(1)*particionamemto
    solucao_exata2 = math.pi*(particionamemto - uns) + np.divide(np.sin(math.pi*particionamemto), particionamemto)
    solucao_exata3 = np.multiply(particionamemto, (9*np.power(particionamemto, 4) - 50*np.power(particionamemto, 3) + 30*particionamemto + 11*uns))/60
    erro1 = np.linalg.norm(y1 - solucao_exata1)/np.linalg.norm(y1)
    erro2 = np.linalg.norm(y2 - solucao_exata2)/np.linalg.norm(y2)
    erro3 = np.linalg.norm(y3 - solucao_exata3)/np.linalg.norm(y3)
    print(f'Para ordem {ordem}')
    print(f'erro relativo do item 1 foi: {erro1}')
    print(f'erro relativo do item 2 foi: {erro2}')
    print(f'erro relativo do item 3 foi: {erro3}')
    numero_de_condicao = np.linalg.cond(A)
    print(f'número de condição de A é: {numero_de_condicao}')
