import cv2

image = cv2.imread("image.png")

blured = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("GaussianBlur", blured)
cv2.waitKey(0)

cv2.destroyAllWindows()