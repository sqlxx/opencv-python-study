""" a scanner """
import argparse
import cv2
import imutils
from skimage.filters import threshold_local
from transform import four_point_transform

def buildApp():
    ''' entrance of the application '''

    argp = argparse.ArgumentParser()
    argp.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
    argp.add_argument("-c", "--coords", help="comma seperated list of source points")
    args = vars(argp.parse_args())

    image = cv2.imread(args["image"])

    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    cnt = findContour(edged, image)

    print("Reshaped cnt", cnt)
    warped = four_point_transform(orig, cnt*ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    threshold = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > threshold).astype("uint8") * 255
    cv2.imshow("tranformed: ", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
    buildApp()
