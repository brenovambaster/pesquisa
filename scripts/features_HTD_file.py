import os
import cv2
import classes.htd as htd

# Specify the directory containing the images
image_dir = '../images/test/'
    
# Get all the image paths
image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith('.jpg') or img.endswith('.png')]

# Initialize the htd class
htd_obj = htd.HTD()

# For each image path, extract features and save them in a file
for img_path in image_paths:
    image = cv2.imread(img_path)
    features = htd_obj.extract_features(image)

    # Get the filename without the extension
    filename = os.path.basename(img_path).split('.')[0]

    with open(f'../output/{filename}_HTD', 'w') as arquivo:
        arquivo.write(str(features))
