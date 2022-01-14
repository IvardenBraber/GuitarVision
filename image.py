import numpy as np
from matplotlib import pyplot as plt
import cv2
from skimage import io
from skimage import color
import matplotlib.pyplot as plt


class Image:

    """
    This Image object was made at the beginning to simplify the code by packaging every common
    image processing treatment in a single object
    """
    def __init__(self, path=None, img=None):
        if img is None:
            self.image = cv2.imread(path)
        elif path is None:
            self.image = img
        else:
            print("")

        image_1 = self.image
        image_1 = color.rgb2gray(image_1)
        self.gray = image_1

    def __str__(self):
        return self.image

    def set_image(self, img):
        self.image = img

    def set_gray(self, grayscale):
        self.gray = grayscale

    def print_cv2(self, is_gray=True):
        if is_gray:
            cv2.imshow('image', self.gray)
        else:
            cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def print_plt(self, is_gray=True):
        if is_gray:
            plt.imshow(self.gray, cmap='gray')
        else:
            plt.imshow(self.image)
        plt.show()

    def edges_canny(self, min_val=100, max_val=200, aperture=3):
        return cv2.Canny(self.gray, min_val, max_val, aperture)

    def edges_laplacian(self, ksize=3):
        return cv2.Laplacian(self.gray, cv2.CV_8U, ksize)

    def edges_sobelx(self, ksize=3):
        return cv2.Sobel(self.gray, cv2.CV_8U, 1, 0, ksize)

    def edges_sobely(self, ksize=3):
        return cv2.Sobel(self.gray, cv2.CV_8U, 0, 1, ksize)

    def lines_hough_transform(self, edges, min_line_length, max_line_gap, threshold=15):
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold, min_line_length, max_line_gap)
        return lines