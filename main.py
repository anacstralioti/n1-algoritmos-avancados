def ler_arquivo_entrada(nome_arquivo):
    ## ignora comentários e linhas em branco
    with open(nome_arquivo, 'r') as f:
        linhas_validas = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

    num_vertices = int(linhas_validas[0])

    matriz_adj = []
    for i in range(1, num_vertices + 1):
        linha_matriz = list(map(int, linhas_validas[i].split()))
        matriz_adj.append(linha_matriz)

    origem, destino = map(int, linhas_validas[num_vertices + 1].split())

    return num_vertices, matriz_adj, origem, destino

def bellman_ford_caminho_longo(num_vertices, matriz_adj, origem, destino):
    arestas = []
    for u in range(num_vertices):
        for v in range(num_vertices):
            if matriz_adj[u][v] != 0:
                arestas.append((u, v, -matriz_adj[u][v]))

    distancias = {i: float('inf') for i in range(num_vertices)}
    predecessores = {i: None for i in range(num_vertices)}
    distancias[origem] = 0

    for _ in range(num_vertices - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u

    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = predecessores.get(atual) 

    if caminho and caminho[0] == origem and distancias[destino] != float('inf'):
        peso_total = -distancias[destino]
        return caminho, peso_total
    else:
        return None, float('-inf')


if __name__ == "__main__":
    arquivo_entrada = 'entrada.txt'
    
    try:
        num_v, matriz, o, d = ler_arquivo_entrada(arquivo_entrada)
        
        caminho_max, peso_max = bellman_ford_caminho_longo(num_v, matriz, o, d)
        
        if caminho_max:
            print("Resultado:")
            print(f"Caminho máximo: {caminho_max}")
            print(f"Peso total: {peso_max}")
        else:
            print(f"Não existe caminho da origem {o} até o destino {d}.")

            
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except (ValueError, IndexError):
        print(f"Erro: O arquivo '{arquivo_entrada}' está mal formatado.")