# Trabalho Computacional 1

é mostrado como inicializar o projeto nesse trabalho.



## Sumário

- [Pré-requisitos](#Pré-requisitos)
- [Configuração](#Configuração)
- [Atividade 1](#Atividade-1)
- [Atividade 2](#Atividade-2)



## Pré-requisitos

Listagem de pré-requisitos que devem já estar instalados em sua máquina para o projeto ser inicializado:

- [Python 3]



## Configuração

Nesta seção, execute todos os comandos que serão apresentandos na linha de comando de sua máquina (podendo ser o terminal pra usuários Linux ou o PowerShell para usuários Windows).

Para rodar o projeto, primeiro abra a pasta baixada ou execute o comando
```bash
cd caminho_para_pasta
```
em que `caminho_para_pasta` é o caminho para a pasta baixada (por exemplo: `Downloads/...`), para abrir a pasta na linha de comando.

crie um ambiete virtual do projeto (para não instalar as depêndencias globalmente em sua máquina) executando o comando
```bash
python -m venv .env
```
em que `python` é o comando [Python 3] da sua máquina (podendo ser `python3`, dependendo do seu OS). Isso criará uma pasta chamada `.env` que irá armazenar as depências do projeto.

Para ativar seu ambiente virtual, execute o comando
```bash
source .env/bin/activate
```
para o ambiente virtual ser utilizado.

Execute o comando 
```bash
pip install -r requisitos-trabalho-computacional-1.txt
```
para instalar as dependências do projeto.

Por fim, execute o comando
```bash
python TrabalhoComputacional1/tests/test_atividade1.py 
```
e
```bash
python TrabalhoComputacional1/tests/test_atividade2.py 
```
para rodar os testes do projeto.

Para desativar o ambiente virtual, execute o comando
```bash
deactivate
```



## Atividade 1
 
- Mostre que uma matriz A = LDL^T, com L uma matriz triangular inferior com 1's na diagonal (aleatória) e D uma matriz diagonal com os elementos da diagonal todos positivos (fatoração LDL^T de A) é de fato simétrica definida positiva. 

    * Basta manipular a equação A = LDL^T. Seja x pertencente ao R^n, com x diferente do vetor nulo, temos x^TLDL^Tx = (L^Tx)^TD(L^Tx) = y^TDy = y_1^2D_1 + y_2^2D_2 + ... + y_n^2D_n > 0, visto que ao menos um y_i é diferente de zero e D_i são positivos. Portanto, A é simétrica definida positiva.

- Faça uma implementação da fatoração **Choleski** para uma matriz simétrica definida positiva, de duas maneiras diferentes: a primeira usando eliminação Gaussiana e a segunda usando a igualdade A = GG^T.

    * Usando a eliminação Gaussiana Utilizei o algoritmo de fatoração LU, o que me entrega A = LU. Fazendo U = DM^T temos A = LDL^T (M = L, visto que A é sinétrica). Aqui não usei o algoritmo de fatoração LU com pivoteamento parcial, para manter a estrutura de L ser triangular inferior e D diagonal (mas bastaria fazer A = P^TLDL^T).

    * Usando a igualdade A = GG^T, o algoritmo foi direto.

- Para validar seu algoritmo, crie matrizes simétricas definidas positivas fazendo A = LDL^T, com L uma matriz triangular inferior com 1's na diagonal (aleatória) e D uma matriz diagonal com os elementos da diagonal todos positivos. Compare o tempo das duas estratégias para calcular a fatoração Choleski em matrizes de ordem 1000, pelo menos. Interprete o resultado.

    * Para os testes, utilizei a matriz de exemplo da apostila (ordem 4) e criei 5 matrizes aletórias de ordem 1000 (demoraram um tempo significativo). Os resultados foram melhores para o algoritmo usando a igualdade. Acho que era o esperado, visto que o trabalho desse algoritmo foi calcular a matriz G. Já no outro, são calculadas as matrizes L e U.




## Atividade 2

Considere o Problema de valor de contorno (PVC):

y''(t) = f(t), s.a. y(0) = y(1) = 0

em que f:[0, 1] → R é C^4[0, 1]. Escreva o problema acima discretizado, usando o método de diferença finitas. Use o espaçamento do intervalo [0, 1] igual a h > 0 (conforme encontra-se na apostila). Ache os autovalores e autovetores da matriz resultante da discretizaçẽo e verifique que esta matriz é simétrica definida positiva. Use o método que teve melhor desempenho na Questão 1 para resolver o sistema linear para as três funções f abaixo (despreze os termos y^(iv) e encontre a solução aproximada) e compare a qualidade da solução com a solução exata (graficamente e analiticamente pelo erro relativo). Faça os testes para valores de h = 0.1, h=0.01 e h=0.001. Calcule o número de condição da matriz para cada valor de h usado.

Para obter as soluções exatas, utilizei [Wolfram|Alpha].

1. f(t) = t^2e^t

    solução exata: y(t) = e^t(t^2 - 4t + 6) 6(t - 1) -3et

2. f(t) = 2[sen(πt)/t^3 − πcos(πt)/t^2] − π^2sen(πt)/t


    solução exata: y(t) = π(t - 1) + sen(πt)/t

3. f(t) = 3t^3 − 10t^2 + 1


    solução exata: y(t) = t/60(9t^4 - 50t^3 + 30t + 11)

[Wolfram|Alpha]: https://www.wolframalpha.com/
[Python 3]: https://www.python.org/downloads/