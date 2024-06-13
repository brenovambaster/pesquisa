
from classes.ImageReader import ImageReader
from scripts.show_images import ShowImages
from classes.OperadorDeBusca import SearchOperator

# Read the image
image1 = ImageReader("base_imgs_testes/980_r.png").read_image()

operador_de_busca = SearchOperator('output/databaseCLD.txt')
list_similar_imgs = operador_de_busca.all_knn(image1, 'CLD', k=9, distance_name='euclidean')

for obj in list_similar_imgs:
    print(obj['path_img'])

ShowImages("base_imgs_testes").show(list_similar_imgs)

