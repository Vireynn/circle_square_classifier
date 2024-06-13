import cv2
import glob


class Figure:
    def __init__(self, filepath: str, coords):
        self.images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in glob.glob(filepath)]
        self.coords = coords

    def bin_attr_fern(self, image, coords):
        """ Создает бинарный признак на основании яркости двух пикселей """
        fern = ''
        for index, elem in enumerate(coords):
            if image[elem[0][0], elem[0][1]] > image[elem[1][0], elem[1][1]]:
                fern += '1'
            else:
                fern += '0'
        return fern
