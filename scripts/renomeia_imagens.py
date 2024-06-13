import os
import shutil


def rename_images(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out all non-image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    # Sort the images by their current names
    images.sort()

    # Rename each image to a temporary name first to avoid conflicts
    temp_names = []
    for i, image in enumerate(images, start=1):
        extension = os.path.splitext(image)[1]
        temp_name = f"temp_{i}{extension}"
        old_path = os.path.join(directory, image)
        temp_path = os.path.join(directory, temp_name)
        shutil.move(old_path, temp_path)
        temp_names.append(temp_name)

    # Rename from temporary names to final sequential names
    for i, temp_name in enumerate(temp_names, start=1):
        extension = os.path.splitext(temp_name)[1]
        new_name = f"{i}{extension}"
        temp_path = os.path.join(directory, temp_name)
        new_path = os.path.join(directory, new_name)
        shutil.move(temp_path, new_path)


# Call the function on your directory
rename_images("../base_imgs_testes/")
