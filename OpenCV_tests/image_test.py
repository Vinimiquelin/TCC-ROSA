import cv2

img = cv2.imread("test.jpg", 1)
print(img)
cv2.imshow("image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()