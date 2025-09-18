## Algoritmo de Caminho Mais Longo em Grafo Acíclico Direcionado (DAG)
<ul>
  <li>Este projeto contém a implementação de um algoritmo para encontrar o caminho mais longo em um grafo acíclico direcionado com pesos nas arestas, que podem ser positivos ou negativos.</li>
</ul>

## Objetivo
<ul>
  <li>O objetivo principal foi implementar um algoritmo em Python que calcule o caminho mais longo entre dois vértices (origem e destino) em um grafo. O "comprimento" de um caminho é definido como a soma dos pesos de suas arestas. Um caminho é considerado "simples" se não repete nenhum vértice.</li>
</ul>

## Funcionalidades
<ul>
  <li>Ler grafos a partir de um arquivo de entrada (entrada.txt) para configurar o grafo;</li>
  <li>O grafo é representado por uma matriz de adjacência com os pesos das arestas;</li>
  <li>O algoritmo funciona mesmo com arestas de peso negativo;</li>
  <li>Encontra o caminho de maior peso total entre a origem e o destino especificados;</li>
  <li>Projetado especificamente para funcionar com Grafos Acíclicos Direcionados (DAGs).</li>
</ul>

## Como funciona o algoritmo
<ul>
  <li>Multiplica-se o peso de todas as arestas do grafo por -1;</li>
  <li>Com os pesos negativados, o problema de encontrar o caminho mais longo se transforma no problema de encontrar o caminho mais curto;</li>
  <li>Utiliza-se o algoritmo de Bellman-Ford para encontrar o caminho mais curto no grafo com os pesos modificados. Este algoritmo é adequado porque funciona com arestas de peso negativo.</li>
  <li>Resultado final: o caminho encontrado é o caminho mais longo no grafo original, e seu peso total é o peso encontrado pelo Bellman-Ford, multiplicado por -1 para voltar ao valor original.</li>
</ul>

