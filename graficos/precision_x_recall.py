from pprint import pprint

import matplotlib.pyplot as plt
from classes.ImageReader import ImageReader
from classes.OperadorDeBusca import SearchOperator
from scripts.extrair_precisao_revocacao import ExtraiPrecisaoRevocao

# Define constants
K_VIZINHOS = 32
CLASSE = '1'
EXTRACTOR = 'HTD'

PATH_IMGS_QUERY = '../base_imgs_teste_query/'
IMG_NAME_QUERY = f'{CLASSE}_r0.png'
PATH_DATABASE_IMGS = '../base_imgs_testes/'
PATH_DATABASE_FEATURES = f'../output/database{EXTRACTOR}.txt'



# Read the image
image1 = ImageReader(f"{PATH_IMGS_QUERY}{IMG_NAME_QUERY}").read_image()

# Create search operator
operador_de_busca = SearchOperator(PATH_DATABASE_FEATURES)

# Find similar images with Euclidean and Manhattan distances
list_similar_imgs_eucl = operador_de_busca.all_knn(image1, EXTRACTOR, k=K_VIZINHOS, distance_name=SearchOperator.EUCLIDEAN)
list_similar_imgs_manhattan = operador_de_busca.all_knn(image1, EXTRACTOR, k=K_VIZINHOS, distance_name=SearchOperator.MANHATTAN)

# Extract paths from similar image results
path_imgs_eucli = [obj['path_img'] for obj in list_similar_imgs_eucl]
path_imgs_manhattan = [obj['path_img'] for obj in list_similar_imgs_manhattan]

# Calculate precision and recall
precision_eucli, recall_eucli = ExtraiPrecisaoRevocao().compute(path_imgs_eucli, CLASSE, dir_base_imgs=PATH_DATABASE_IMGS)
precision_manhattan, recall_manhattan = ExtraiPrecisaoRevocao().compute(path_imgs_manhattan, CLASSE,dir_base_imgs=PATH_DATABASE_IMGS)
pprint(precision_eucli)

# Generate plot
plt.figure(figsize=(10, 10))
plt.plot(recall_eucli, precision_eucli, marker='o', label=f'{IMG_NAME_QUERY} - Euclidean')
plt.plot(recall_manhattan, precision_manhattan, marker='o', label=f'{IMG_NAME_QUERY} - Manhattan')
plt.legend(title="Precision-Recall Curve", loc="lower left")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(f'{EXTRACTOR}, k={K_VIZINHOS}')
plt.grid(True)
plt.figtext(0.5, 0.5, f'Query image: {IMG_NAME_QUERY}', wrap=True, horizontalalignment='center', fontsize=12)
# plt.savefig(f'../output/precision_recall_{IMG_NAME_QUERY}', dpi=300, bbox_inches='tight')
plt.show()

