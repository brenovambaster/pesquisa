import cv2

class ImageReader:
    """
    A class used to read images using OpenCV

    ...

    Attributes
    ----------
    path : str
        a string representing the path of the image file

    Methods
    -------
    read_image():
        Attempts to read the image file at the specified path
    """

    def __init__(self, path):
        """
        Constructs all the necessary attributes for the image reader object.

        Parameters
        ----------
            path : str
                a string representing the path of the image file
        """
        self.path = path

    def read_image(self):
        """
        Attempts to read the image file at the specified path.

        Returns
        -------
        image : np.ndarray
            The image data if the file could be read, None otherwise.
        """
        try:
            image = cv2.imread(self.path)
            if image is None:
                print(f"Error: Unable to open image file at {self.path}")
                return None
            return image
        except Exception as e:
            print(f"Error: An error occurred while trying to read the image file at {self.path}")
            print(str(e))
            return None