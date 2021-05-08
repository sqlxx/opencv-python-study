import numpy as np
import argparse
import cv2

image = cv2.imread("test.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

image = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 50, 150)
cv2.imshow("Canny", canny)


(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow("After", image1)
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Contours", image2)
cv2.waitKey(0)
