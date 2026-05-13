import cv2

image = cv2.imread("image.png")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)

cv2.destroyAllWindows()