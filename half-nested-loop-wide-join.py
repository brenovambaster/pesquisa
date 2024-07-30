import heapq
import string

import numpy as np
import classes.extract_info_file
from typing import List, Tuple, Callable, Dict

# Tipo de dados para representar um par e sua distância
Pair = Tuple[int, int, float, string]


# Função para calcular a distância entre dois vetores de características
def calculate_distance(features1: np.ndarray, features2: np.ndarray) -> float:
    # Exemplo de cálculo de distância euclidiana
    return np.linalg.norm(features1 - features2)


# Função para inserir um par na fila de prioridade
def insert_into_priority_queue(queue: List[Pair], pair: Pair, k: int):
    """
    Insere um par na fila de prioridade, garantindo que apenas os k pares mais próximos sejam mantidos.
    """
    if len(queue) < k:
        heapq.heappush(queue, pair)
    else:
        # Substitui o par mais distante, se o novo par for mais próximo
        if pair[2] < queue[0][2]:
            heapq.heapreplace(queue, pair)


# Função principal para o Half Nested-Loop Wide-Join
def half_nested_loop_wide_join(T: List[Dict], k: int, distance_func: Callable[[np.ndarray, np.ndarray], float],
                               threshold: float) -> Dict[int, List[Pair]]:
    """
    Executa o Half Nested-Loop Wide-Join para encontrar os k pares mais similares para cada elemento.

    :param T: Lista de elementos a serem comparados, cada elemento é um dicionário com 'id' e 'features'.
    :param k: Número de pares mais similares a serem retornados para cada elemento.
    :param distance_func: Função para calcular a distância entre dois vetores de características.
    :param threshold: Limite de distância para considerar um par como similar.
    :return: Dicionário onde a chave é o id do elemento e o valor é uma lista de k pares mais similares, cada um como (id, id, distância).
    """
    results = {}

    for t1 in T:
        queue = []
        for t2 in T:
            if t1['id'] != t2['id']:
                distance = distance_func(t1['features'], t2['features'])
                path_img = t2['path_img']
                if distance <= threshold:
                    pair = (t1['id'], t2['id'], distance, path_img)
                    insert_into_priority_queue(queue, pair, k)
        results[t1['id']] = queue

    return results


# Exemplo de uso
def main():
    # Lista de elementos com suas características
    data = classes.extract_info_file.FileProcessor('./output/databaseHTD.txt').process_file()

    # Transform the data into a list of dictionaries
    elements = []

    for i in data:
        h2 = np.array(i['features'], dtype=np.float32)
        result = {
            'id': i['id'],
            'features': h2,
            'path_img': i['path']
        }
        elements.append(result)

    # Parâmetros
    k = 3  # Número de pares mais similares a serem retornados para cada elemento
    threshold = 1  # Limite de distância

    # Executa o algoritmo
    result = half_nested_loop_wide_join(elements[:200], k, calculate_distance, threshold)

    # Exibe os resultados
    for id, neighbors in result.items():
        print(f"Os {k} pares mais similares para o elemento com id {id} são:")
        for pair in neighbors:
            print(pair)


if __name__ == "__main__":
    main()
