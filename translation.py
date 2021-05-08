import numpy as np
import cv2

image = cv2.imread('./test.jpeg')
cv2.imshow("original", image)
cv2.waitKey(0)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("target", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -25], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("target", shifted)

cv2.waitKey(0)

(h, w) = image.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("target", rotated)
cv2.waitKey(0)