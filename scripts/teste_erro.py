import os
import cv2
import classes.htd as htd

# Função para obter o caminho absoluto
def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)


# Specify the directory containing the images
image_dir = '../images/299.jpg'
htd_obj = htd.HTD()
absolute_image_path = get_absolute_path(image_dir)

print(f"Path absoluto da imagem: {absolute_image_path}")

# Verifique se a imagem foi carregada corretamente
img = cv2.imread(absolute_image_path)
if img is None:
    raise ValueError(F"Falha ao carregar a imagem em {absolute_image_path}")

# Extraia as características usando o HTD
feat = htd_obj.extract_features(img)
print(feat)
