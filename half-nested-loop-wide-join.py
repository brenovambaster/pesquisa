import classes.extract_info_file
import numpy as np
import classes.extract_info_file
from scripts import customHeap


def distance(p1, p2):
    return np.linalg.norm(p1 - p2)


def half_nested_loop_wide_join(T, k, xi):
    """
    :param T: Relation
    :param k: k-nearest neighbors
    :param xi: (ξ) Similarity threshold
    :return:
    """
    Q = customHeap.CustomHeap()

    for i in range(len(T) - 1):
        a1 = customHeap.Element(T[i]['id'], T[i]['features'], T[i]['path_img'])

        for j in range(i + 1, len(T)):
            a2 = customHeap.Element(T[j]['id'], T[j]['features'], T[j]['path_img'])
            dist = distance(a1.features, a2.features)

            if dist <= xi:
                if len(Q.heap) < k:
                    Q.add_item(a1, a2, dist)
                else:
                    q = Q.heap[0]  # get the element with the smallest distance
                    if dist < q[1][2]:
                        Q.pop_item()
                        Q.add_item(a1, a2, dist)

    return Q


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

# Executar o algoritmo half_nested_loop_wide_join
resultado = half_nested_loop_wide_join(T, 5, 0.5)

# Printar o resultado
print(resultado)
