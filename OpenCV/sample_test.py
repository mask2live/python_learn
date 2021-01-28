import cv2
import glob

images = glob.glob("sample_images/*.jpg")

print(images)

for image in images:
    img = cv2.imread(image,0)
    resize_img = cv2.resize(img, (100,100))
    cv2.imshow("image", resize_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # write the new image into specified directory
    cv2.imwrite("sample_images/resize_100_"+image, resize_img)