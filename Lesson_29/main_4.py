import cv2

image = cv2.imread("image.png")

# cv2.imshow("stul", image)
# cv2.waitKey(0)

# resized = cv2.resize(image, (300, 200))
# cv2.imshow("Small", resized)
# cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Black and white", gray)
cv2.waitKey(0)

crop = image[50:200, 50:200]
cv2.imshow("resize", crop)
cv2.waitKey(0)

cv2.destroyAllWindows()