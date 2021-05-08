import numpy as np
import cv2

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w//2, h//2)
    
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

def translate(image, dx, dy):
    M = [[1, 0, dx], [0, 1, dy]]
    translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image[:2]

    if (width is None and height is None):
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation = inter)
    