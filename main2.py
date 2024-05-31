import cv2
from classes import htd, cld, csd, distances, descriptor

image1 = cv2.imread("images/test/6.jpg")
image2 = cv2.imread("images/test/15.jpg")
htd_instance = htd.HTD()
p2 = htd_instance.extract_features(image2)

descriptor_instance = descriptor.Descriptor(image1, "HTD", "euclidean", p2)

print("Distance: ", descriptor_instance.distance.calculated_distance)