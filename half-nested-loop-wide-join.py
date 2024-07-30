import heapq
import string
import timeit

import numpy as np
import classes.extract_info_file
from typing import List, Tuple, Callable, Dict

# Tipo de dados para representar um par e sua distância
# Tuple[id, id, distancia, path_img]
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

        # Ordena a fila de prioridade (queue) por distância x[2] (índice 2) é a distância no par (id1, id2, distância)
        queue_sorted = sorted(queue, key=lambda x: x[2])
        results[t1['id']] = queue_sorted
    return results


# Exemplo de uso
def main(k: int = 1, threshold: float = 0.3):
    """

    :param k: Numero de vizinhos próximos
    :param threshold: Limiar de distância
    :return:
    """
    print(f"Setup: k={k}, threshold={threshold}")

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

    # Executa o algoritmo
    result = half_nested_loop_wide_join(elements, k, calculate_distance, threshold)

    # Exibe os resultados
    for id, neighbors in result.items():
        print(f"Os {k} pares mais similares para o elemento com id {id} são:")
        for pair in neighbors:
            print(pair)


if __name__ == "__main__":
    start = timeit.default_timer()
    main(k=3, threshold=0.4)
    print("The difference of time is :", timeit.default_timer() - start)
