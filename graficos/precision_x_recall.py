import matplotlib.pyplot as plt

from classes.ImageReader import ImageReader
from classes.OperadorDeBusca import SearchOperator
from scripts.extrair_precisao_revocacao import extrai_precisao_revocao
K_VIZINHOS = 32
IMG_NAME_QUERY = '1_r0.png'
# Dados de exemplo img 1_r0

# Read the image
image1 = ImageReader(F"../base_imgs_teste_query/{IMG_NAME_QUERY}").read_image()

operador_de_busca = SearchOperator('../output/database.txt')
list_similar_imgs = operador_de_busca.all_knn(image1, 'HTD', k=K_VIZINHOS, distance_name=SearchOperator.EUCLIDEAN)

path_imgs = []
for obj in list_similar_imgs:
    path_imgs.append(obj['path_img'])

precision, recall = extrai_precisao_revocao().compute(path_imgs, '1')

print(precision)
print(recall)

plt.figure(figsize=(10, 10))
plt.plot(recall, precision, marker='o', label='1_r0')
plt.legend("Precision-Recall Curve")
plt.legend(loc='lower left')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(f'Extractor HTD, Distance Euclidean, k={K_VIZINHOS}')
plt.grid(True)
plt.figtext(0.5, 0.5, f'Query image: {IMG_NAME_QUERY}', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()
