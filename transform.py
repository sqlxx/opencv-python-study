''' perspective transform by four points '''
import numpy as np
import cv2

def order_points(pts):
    ''' order the four points by top-left, top-right, bottom-right, bottom-left '''
    rect = np.zeros((4, 2), dtype= "float32")
    s = pts.sum(axis = 1)
    idx1 = np.argmin(s)
    idx2 = np.argmax(s)

    rect[0] = pts[idx1]
    rect[2] = pts[idx2]
    leftPts = np.delete(pts, [idx1, idx2], axis=0)
    print(leftPts)
    diff = np.diff(leftPts, axis=1)
    rect[1] = leftPts[np.argmin(diff)]
    rect[3] = leftPts[np.argmax(diff)]

    return rect

def four_point_transform(image, pts):
    ''' do the perspective transform '''
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt((br[0] - bl[0])**2 + (br[1] - bl[1])**2)
    widthB = np.sqrt((tr[0] - tl[0])**2 + (tr[1] - tr[0])**2)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt((br[0] - tr[0])**2 + (br[1] - tr[1])**2)
    heightB = np.sqrt((bl[0] - tl[0])**2 + (bl[1] - tl[1])**2)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
    print(dst)
    print(rect)
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
