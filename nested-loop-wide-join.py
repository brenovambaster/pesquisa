import copy
import numpy as np

import classes.extract_info_file
from classes.ImageReader import ImageReader
from scripts import customHeap


def distance(p1, p2):
    return np.linalg.norm(p1 - p2)


def nested_loop_wide_join(T1, T2, k, xi):
    """
    :param t1: Relation 1
    :param t2: Relation 2
    :param k: k-nearest neighbors
    :param xi: (ξ) Similarity threshold
    :return:
    """
    Q = customHeap.CustomHeap()

    counterJ = 0

    for i in range(1, len(T1)):
        a1 = customHeap.Element(T1[i]['id'], T1[i]['features'], T1[i]['path_img'])

        for j in range(1, len(T2)):
            a2 = customHeap.Element(T2[j]['id'], T2[j]['features'], T2[j]['path_img'])
            dist = distance(a1.features, a2.features)

            if a1.id != a2.id and dist <= xi:

                if len(Q.heap) <= k:
                    Q.add_item(a1, a2, dist)

                else:
                    q = Q.heap[0]  # Get the element with the smallest distance
                    if dist < q[1][2]:
                        Q.pop_item()
                        Q.add_item(a1, a2, dist)

            # ------- Mostrar apenas 7 iterações para teste. Remover para obter o resultado completo
            if counterJ == 7:
                return Q
            counterJ += 1
            # --------


# Read the image
image1 = ImageReader("base_imgs_testes/1_r40.png").read_image()

data = classes.extract_info_file.FileProcessor('./output/databaseHTD.txt').process_file()

# Transform the data into a list of dictionaries
T1 = []
T2 = []
for i in data:
    h2 = np.array(i['features'], dtype=np.float32)
    result = {
        'id': i['id'],
        'features': h2,
        'path_img': i['path']
    }
    T1.append(result)

T2 = copy.deepcopy(T1)

Q_result = nested_loop_wide_join(T1, T2, 5, 0.5)
print(Q_result)
