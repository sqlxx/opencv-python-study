import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class OpenCvTutorial:
    def photoBasic(self):
        print("OpenCV version:")
        print(cv.__version__)
        img = cv.imread("test2.jpeg")
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # cv.imshow("Over the Clouds", img)
        # cv.imshow("Over the Clouds - gray", gray)

        # cv.waitKey(0)
        # cv.destroyAllWindows()
        print(img)
        b, g, r = cv.split(img)
        img2 = cv.merge([r, g, b])
        plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def videoBasic(self):
        cap = cv.VideoCapture(0)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame, exiting")
                break
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray = cv.flip(gray, 0)
            cv.imshow('frame', gray)
            out.write(gray)
            if cv.waitKey(25) == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    loader = OpenCvTutorial()
    # loader.videoBasic()
    loader.photoBasic()
