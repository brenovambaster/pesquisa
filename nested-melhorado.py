import heapq
import string
import timeit
from multiprocessing import Pool, cpu_count
import numpy as np
from typing import List, Tuple, Callable, Dict
import classes.extract_info_file

# Tipo de dados para representar um par e sua distância
Pair = Tuple[int, int, float, string]


# Função para calcular a distância entre dois vetores de características
def calculate_distance(features1: np.ndarray, features2: np.ndarray) -> float:
    """
    Calcula a distância Euclidiana entre dois vetores de características.

    Args:
        features1 (np.ndarray): O vetor de características do primeiro elemento.
        features2 (np.ndarray): O vetor de características do segundo elemento.

    Returns:
        float: A distância Euclidiana entre os dois vetores de características.
    """
    return np.linalg.norm(features1 - features2)


# Função para inserir um par na fila de prioridade
def insert_into_priority_queue(queue: List[Pair], pair: Pair, k: int):
    """
    Insere um par na fila de prioridade, garantindo que apenas os k pares mais próximos sejam mantidos.

    Args:
        queue (List[Pair]): A fila de prioridade.
        pair (Pair): O par a ser inserido na fila.
        k (int): O número máximo de pares a serem mantidos na fila.
    """
    if len(queue) < k:
        heapq.heappush(queue, pair)
    else:
        # Substitui o par mais distante, se o novo par for mais próximo
        if pair[2] < queue[0][2]:
            heapq.heapreplace(queue, pair)


# Função auxiliar para calcular os pares para um elemento
def compute_pairs_for_element(args):
    """
    Calcula os k pares mais similares para um único elemento.

    Args:
        args (Tuple): Uma tupla contendo (t1, T, k, threshold, distance_func).

    Returns:
        Tuple[int, List[Pair]]: O ID do elemento e uma lista dos k pares mais similares.
    """
    t1, T, k, threshold, distance_func = args
    queue = []
    for t2 in T:
        if t1['id'] != t2['id']:
            distance = distance_func(t1['features'], t2['features'])
            path_img = t2['path_img']
            if distance <= threshold:
                pair = (t1['id'], t2['id'], distance, path_img)
                insert_into_priority_queue(queue, pair, k)

    # Ordena a fila de prioridade (queue) por distância
    queue_sorted = sorted(queue, key=lambda x: x[2])
    return t1['id'], queue_sorted


# Função principal para o Half Nested-Loop Wide-Join
def half_nested_loop_wide_join(T: List[Dict], k: int, distance_func: Callable[[np.ndarray, np.ndarray], float],
                               threshold: float) -> Dict[int, List[Pair]]:
    """
    Executa o Half Nested-Loop Wide-Join para encontrar os k pares mais similares para cada elemento.

    Args:
        T (List[Dict]): Lista de elementos a serem comparados, cada elemento é um dicionário com 'id' e 'features'.
        k (int): Número de pares mais similares a serem retornados para cada elemento.
        distance_func (Callable[[np.ndarray, np.ndarray], float]): Função para calcular a distância entre dois vetores de características.
        threshold (float): Limite de distância para considerar um par como similar.

    Returns:
        Dict[int, List[Pair]]: Dicionário onde a chave é o id do elemento e o valor é uma lista de k pares mais similares.
    """
    with Pool(cpu_count()) as pool:
        results_list = pool.map(compute_pairs_for_element, [(t1, T, k, threshold, distance_func) for t1 in T])

    return {id: neighbors for id, neighbors in results_list}


# Exemplo de uso
def main(k: int = 3, threshold: float = 0.3):
    """

    :param k: K-vizinhos mais próximos
    :param threshold: limiar de distância
    :return:
    """
    print(f"Setup: k={k}, threshold={threshold}")

    # Lista de elementos com suas características
    data = classes.extract_info_file.FileProcessor('./output/databaseHTD.txt').process_file()

    # Transforma os dados em uma lista de dicionários
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
    main(k=3, threshold=0.3)
    print("The difference of time is:", timeit.default_timer() - start)
