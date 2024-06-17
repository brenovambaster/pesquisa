import matplotlib.pyplot as plt
from classes.ImageReader import ImageReader
from classes.OperadorDeBusca import SearchOperator
from scripts.extrair_precisao_revocacao import ExtraiPrecisaoRevocao

# Define constants
K_VIZINHOS = 32
IMG_NAME_QUERY = '3_r0.png'
CLASSE = '3'
EXTRACTOR = 'CLD'
PATH_DATABASE = '../output/databaseCLD.txt'


# Read the image
image1 = ImageReader(f"../base_imgs_teste_query/{IMG_NAME_QUERY}").read_image()

# Create search operator
operador_de_busca = SearchOperator(PATH_DATABASE)

# Find similar images with Euclidean and Manhattan distances
list_similar_imgs_eucl = operador_de_busca.all_knn(image1, EXTRACTOR, k=K_VIZINHOS, distance_name=SearchOperator.EUCLIDEAN)
list_similar_imgs_manhattan = operador_de_busca.all_knn(image1, EXTRACTOR, k=K_VIZINHOS, distance_name=SearchOperator.MANHATTAN)

# Extract paths from similar image results
path_imgs_eucli = [obj['path_img'] for obj in list_similar_imgs_eucl]
path_imgs_manhattan = [obj['path_img'] for obj in list_similar_imgs_manhattan]

# Calculate precision and recall
precision, recall = ExtraiPrecisaoRevocao().compute(path_imgs_eucli, CLASSE)
precision_manhattan, recall_manhattan = ExtraiPrecisaoRevocao().compute(path_imgs_manhattan, CLASSE)

# Generate plot
plt.figure(figsize=(10, 10))
plt.plot(recall, precision, marker='o', label=f'{IMG_NAME_QUERY} - Euclidean')
plt.plot(recall_manhattan, precision_manhattan, marker='o', label=f'{IMG_NAME_QUERY} - Manhattan')
plt.legend(title="Precision-Recall Curve", loc="lower left")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(f'{EXTRACTOR} HTD, k={K_VIZINHOS}')
plt.grid(True)
plt.figtext(0.5, 0.5, f'Query image: {IMG_NAME_QUERY}', wrap=True, horizontalalignment='center', fontsize=12)
plt.savefig(f'../output/precision_recall_{IMG_NAME_QUERY}', dpi=300, bbox_inches='tight')
plt.show()

