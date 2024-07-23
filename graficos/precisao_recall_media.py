from pprint import pprint

import matplotlib.pyplot as plt
from classes.ImageReader import ImageReader
from classes.OperadorDeBusca import SearchOperator
from scripts.extrair_precisao_revocacao import ExtraiPrecisaoRevocao

# Define constants
K_NEIGHBORS = 4000
CLASS = '1'
EXTRACTOR = 'HTD'
TOTAL_DE_IMG_NO_DIR_QUERY = 20

PATH_IMGS_QUERY = '../base_imgs_teste_query/'

PATH_DATABASE_IMGS = '../base_imgs_testes/'
PATH_DATABASE_FEATURES = f'../output/database{EXTRACTOR}.txt'

# Create search operator
searchOperator = SearchOperator(PATH_DATABASE_FEATURES)
allPrecisions = []
allRecalls = []
for i in range(1, TOTAL_DE_IMG_NO_DIR_QUERY + 1):
    IMG_NAME_QUERY = f'{CLASS}_r0.png'

    # Read the image
    image1 = ImageReader(f"{PATH_IMGS_QUERY}{IMG_NAME_QUERY}").read_image()

    # Find similar images with Euclidean and Manhattan distances
    list_similar_imgs_eucl = searchOperator.all_knn(image1, EXTRACTOR, k=K_NEIGHBORS,
                                                    distance_name=SearchOperator.EUCLIDEAN)

    # Extract paths from similar image results
    path_imgs_eucli = [obj['path_img'] for obj in list_similar_imgs_eucl]

    # Calculate precision and recall
    precision_eucli, recall_eucli = ExtraiPrecisaoRevocao().compute(path_imgs_eucli, CLASS,
                                                                    dir_base_imgs=PATH_DATABASE_IMGS)
    # pprint(precision_eucli)
    CLASS = str(i + 1)
    allPrecisions.append(precision_eucli)
    allRecalls.append(recall_eucli)

# GENERATE SUM OF PRECISIONS AND RECALLS FOR EACH CLASS AND CALCULATE THE MEAN
Precisions = []
Recalls = []
countPrecision = 0
countRecall = 0
for i in range(K_NEIGHBORS):
    for j in range(TOTAL_DE_IMG_NO_DIR_QUERY):
        countPrecision += allPrecisions[j][i]
        countRecall += allRecalls[j][i]
    Precisions.append(countPrecision / TOTAL_DE_IMG_NO_DIR_QUERY)
    Recalls.append(countRecall / TOTAL_DE_IMG_NO_DIR_QUERY)
    countPrecision = 0
    countRecall = 0

# plot the mean precision and recall
plt.figure(figsize=(10, 10))
plt.axis([0.9, 1.1, 0, 1.1])
plt.plot(Recalls, Precisions, marker='o', label=f'Average  Precision-Recall Curve')
plt.legend(title="Precision-Recall Curve", loc="lower left")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(f'{EXTRACTOR}, k={K_NEIGHBORS}')
plt.grid(True)
plt.savefig(f'../output/precision_recall_average_{EXTRACTOR}', dpi=400, bbox_inches='tight')
plt.show()
