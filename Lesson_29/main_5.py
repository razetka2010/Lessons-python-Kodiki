import cv2

image = cv2.imread("image.png")

media = cv2.medianBlur(image, 5)
cv2.imshow("MedianBlur", media)
cv2.waitKey(0)

cv2.destroyAllWindows()