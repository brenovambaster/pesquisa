
from classes.ImageReader import ImageReader
from scripts.show_images import ShowImages
from classes.OperadorDeBusca import SearchOperator

# Read the image
image1 = ImageReader("query/31.jpg").read_image()

operador_de_busca = SearchOperator('output/databaseLBP.txt')
list_similar_imgs = operador_de_busca.all_knn(image1, 'LBP', k=9, distance_name=SearchOperator.EUCLIDEAN)

for obj in list_similar_imgs:
    print(obj['path_img'])

ShowImages("database").show(list_similar_imgs)

