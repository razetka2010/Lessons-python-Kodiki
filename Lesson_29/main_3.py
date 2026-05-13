import cv2

image = cv2.imread("image.png")

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)

cv2.destroyAllWindows()