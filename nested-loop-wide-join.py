import copy
import numpy as np

import classes.extract_info_file
from classes.ImageReader import ImageReader
from scripts.customHeap import CustomHeap
from scripts.customHeap import Element


def distance(p1, p2):
    return np.linalg.norm(p1 - p2)


def nested_loop_wide_join(t1, t2, k:int, xi:float) -> CustomHeap:
    """
    :param t1: Relation T
    :param t2: Relation T (copy of T1)
    :param k: k-nearest neighbors
    :param xi: (ξ) Similarity threshold
    :return: q
    :rtype: CustomHeap
    """
    q = CustomHeap()

    counter_j = 0

    for i in range(1, len(t1)):
        a1 = Element(t1[i]['id'], t1[i]['features'], t1[i]['path_img'])

        for j in range(1, len(t2)):
            a2 = Element(t2[j]['id'], t2[j]['features'], t2[j]['path_img'])
            dist = distance(a1.features, a2.features)

            if a1.id != a2.id and dist <= xi:

                if len(q.heap) <= k:
                    q.add_item(a1, a2, dist)

                else:
                    q = q.heap[0]  # Get the element with the smallest distance
                    if dist < q[1][2]:
                        q.pop_item()
                        q.add_item(a1, a2, dist)

            # ------- Mostrar apenas 7 iterações para teste. Remover para obter o resultado completo
            if counter_j == 7:
                return q
            counter_j += 1
            # --------


# Read the image
image1 = ImageReader("base_imgs_testes/1_r40.png").read_image()

data = classes.extract_info_file.FileProcessor('./output/databaseHTD.txt').process_file()

# Transform the data into a list of dictionaries
T1 = []
T2 = []

# TODO: refactor this code to avoid repetition
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