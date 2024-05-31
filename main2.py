import cv2
from classes import htd, cld, csd, distances, descriptor


image1 = cv2.imread("images/test/6.jpg")
image2 = cv2.imread("images/test/15.jpg")

descriptor_instance = descriptor.Descriptor(image1, "HTD", "euclidean")
print("Distance: ", descriptor_instance.distance.calculated_distance)