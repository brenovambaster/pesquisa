import classes.htd as htd
import classes.cld as cld
import classes.scd as scd
import classes.dcd as dcd
import classes.csd as csd
import cv2


def main():
    # Create a new instance of the class
    htd_instance = htd.HTD()
    cld_instance = cld.CLD()
    scd_instance = scd.SCD()
    dcd_instance = dcd.DCD()
    csd_instance = csd.CSD()

    # Load the image
    image1 = cv2.imread("images/buraco1.jpg")
    image2 = cv2.imread("images/buraco2.jpg")


    # Input algorithm that you want to run
    print(""
          "HTD - Histogram of Texture Differences\n"
          "CLD - Color Layout Descriptor\n"
          "SCD - Scalable Color Descriptor\n"
          "DCD - Dominant Color Descriptor\n"
          "CSD - Color Structure Descriptor\n"
          "all - Run all algorithms\n"
          "q - Exit\n"
          )

    algorithm = input("Enter the algorithm you want to run: ")

    while True:
        if algorithm == "q":
            exit()
        if algorithm == "HTD":
            htd_instance.run(image1, image2)

        elif algorithm == "CLD":
            cld_instance.run(image1, image2)

        elif algorithm == "SCD":
            scd_instance.run(image1, image2)

        elif algorithm == "DCD":
            dcd_instance.run(image1, image2)

        elif algorithm == "CSD":
            csd_instance.run(image1, image2)

        elif algorithm == "all":
            htd_instance.run(image1, image2)
            cld_instance.run(image1, image2)
            scd_instance.run(image1, image2)
            dcd_instance.run(image1, image2)
            csd_instance.run(image1, image2)

        else:
            print("Invalid algorithm")

        algorithm = input("Enter the algorithm you want to run: ")


main()
