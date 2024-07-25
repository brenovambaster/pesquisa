
import numpy as np

import classes.extract_info_file
from scripts.customHeap import CustomHeap
from scripts.customHeap import Element


def distance(p1, p2):
    return np.linalg.norm(p1 - p2)


def half_nested_loop_wide_join(relation_t, k, xi) -> CustomHeap:
    """
    :param relation_t: Relation
    :param k: k-nearest neighbors
    :param xi: (ξ) Similarity threshold
    :return:
    """
    q = CustomHeap()
    counter_j = 0

    for i in range(len(relation_t) - 1):
        a1 = Element(relation_t[i]['id'], relation_t[i]['features'], relation_t[i]['path_img'])

        for j in range(i + 1, len(relation_t)):
            a2 = Element(relation_t[j]['id'], relation_t[j]['features'], relation_t[j]['path_img'])
            dist = distance(a1.features, a2.features)
            # print(j)
            if dist <= xi:
                if len(q.heap) < k:
                    q.add_item(a1, a2, dist)
                else:
                    q = q.heap[0]  # get the element with the smallest distance
                    if dist < q[1][2]:
                        q.pop_item()
                        q.add_item(a1, a2, dist)

        # ------- Mostrar apenas 7 iterações para teste. Remover para obter o resultado completo
        if counter_j == 7:
            return q
        counter_j += 1
        # --------
        return q


# Leitura e processamento dos dados de entrada

data = classes.extract_info_file.FileProcessor('./output/databaseHTD.txt').process_file()

# Transformar os dados em uma lista de dicionários
T = []
for i in data:
    h2 = np.array(i['features'], dtype=np.float32)
    result = {
        'id': i['id'],
        'features': h2,
        'path_img': i['path']
    }
    T.append(result)

resultado = half_nested_loop_wide_join(T, 5, 0.5)

print(resultado)
