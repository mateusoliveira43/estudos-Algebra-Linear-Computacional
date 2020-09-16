# Comandos NumPy

Comandos úteis da biblioteca [NumPy] para a disciplina.

Para todos os comandos deste resumo, considere:
```python
import numpy as np
```

## Criar Objetos

```python
A = np.zeros((m, n))
```
cria uma matriz de zeros de ordem `m` (linhas) por `n` (colunas).

```python
A = np.ones((m, n))
```
cria uma matriz de uns de ordem `m` (linhas) por `n` (colunas).

```python
A = np.eye(n)
```
cria a matriz identidade de ordem `n`.

```python
A = np.ramdom.rand((m, n))
```
cria uma matriz de entradas aleatórias (no intervalo [0,1)) de ordem `m` (linhas) por `n` (colunas).

```python
A = np.ramdom.randn((m, n))
```
cria uma matriz de entradas aleatórias (baseada na distribuição normal) de ordem `m` (linhas) por `n` (colunas).

```python
interval = np.linspace(a, b, n)
```
cria uma intervalo de `a` até `b` (incluindo os extremos) com `n` pontos.

## Operações

```python
A.T ou A.transpose()
```
transposta da matriz `A`.

```python
A.dot(B)
```
Produto matricial da matriz `A` pela matriz `B`.

## Funções

```python
A.shape
```
retorna as dimensões (linhas, colunas) da matriz `A`.

```python
np.trace(A)
```
retorna o traço da matriz `A`.

```python
np.linalg.cond(A)
```
retorna o número de condição da matriz `A`. Nesse caso, o padrão é norma 2. Para usar outro como `1`, `'inf'` ou `'fro'`, basta passar como segundo parâmetro.

[NumPy]: https://numpy.org/