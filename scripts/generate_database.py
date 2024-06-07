import os
import cv2
import classes.htd as htd

# Specify the directory containing the images
image_dir = '../images/'

# Get all the image paths
"""
 TODO: AS IMANGES CARREGADAS  SEGUEM A ORDEM QUE O OS.LISTDIR RETORNA, E não a ordem que o sistema operacional lista os arquivos (crescente)
 Faz se necessário mapear o id gerado para o nome da imagem.  
"""
image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if
               img.endswith('.jpg') or img.endswith('.png')]

# Initialize the htd class
htd_obj = htd.HTD()

# For each image path, extract features and save them in a file
id = 0 # id for each image in the database file

for img_path in image_paths:
    image = cv2.imread(img_path)
    features = htd_obj.extract_features(image)

    # Save the features in a file
    with open('../output/database.txt', 'a') as f:
        f.write(f'id={id}|features={features}|lat=123.32|long=-12.3231\n')
        f.close()


    # Map the id to the image name
    with open('../output/id_map.txt', 'a') as f:
        f.write(f'id={id}|image={img_path}\n')
        f.close()

    id += 1