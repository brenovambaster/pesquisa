import os
import shutil

def rename_images(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out all non-image files
    images = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]

    # Sort the images by their current names
    images.sort()

    # Rename each image to a sequential number
    for i, image in enumerate(images, start=1):
        # Construct the new name for the image
        extension = os.path.splitext(image)[1]
        new_name = f"{i}{extension}"

        # Construct the full paths for the old and new names
        old_path = os.path.join(directory, image)
        new_path = os.path.join(directory, new_name)

        # Rename the image
        shutil.move(old_path, new_path)

# Call the function on your directory
rename_images("../base_imgs_testes/")