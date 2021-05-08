""" a scanner """
import argparse
import cv2
import imutils
from skimage.filters import threshold_local
from transform import four_point_transform

def buildAppWeixin():
    
    image = cv2.imread("/Users/sqlxx/Downloads/reimburseqr2.png")
    detector = cv2.wechat_qrcode_WeChatQRCode()
    val, points = detector.detectAndDecode(image)
    print(val, points);

def buildApp():
    ''' entrance of the application '''
    image = cv2.imread("/Users/sqlxx/Downloads/reimburseqr2.png")
    detector = cv2.QRCodeDetector()
    
    val, decodedText, points, _ = detector.detectAndDecodeMulti(image)
    print(val, decodedText);

    if val: 
        for rect in points:
            drawRect(image, rect);    


    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows();

def drawRect(image, points):
    nrOfPoints = len(points)
    for i in range(nrOfPoints):
        print(points[i])
        cv2.line(image, tuple(points[i]), tuple(points[(i+1)%nrOfPoints]), (255, 0, 0), 3)

def findContour(image, originalImage):
    ''' find contour '''

    cnts = cv2.findContours(image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    print("STEP 2: Find contours of paper", screenCnt)
    cv2.drawContours(originalImage, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", originalImage)

    return screenCnt.reshape(4, 2)


if __name__ == '__main__':
    # buildApp()
    buildAppWeixin()
