import cv2

img = cv2.imread("galaxy.jpg")

print(img)
print(type(img))
print(img.shape)  # output (height, width)
print(img.ndim)

# resize image (width, height)
resized_image = cv2.resize(img,(2000,1000))

# show image 5s
cv2.imshow('galaxy', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()