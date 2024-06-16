import cv2
import glob
import os

class Figure:
    def __init__(self, filepath: str, coords: list):
        self.filepath = filepath
        self.images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in glob.glob(self.filepath)]
        self.coords = coords
        self.num_of_parts = 3

    @staticmethod
    def bin_attr_fern(image, coords):
        """ Creating a binary feature based on the brightness of two pixels. """
        fern = ''
        for elem in coords:
            if image[elem[0][0], elem[0][1]] > image[elem[1][0], elem[1][1]]:
                fern += '1'
            else:
                fern += '0'
        return fern

    @staticmethod
    def fern_split(sequence: str, num_of_parts: int):
        """ Partitioning a vector into several groups. """
        return [sequence[i * len(sequence) // num_of_parts: (i + 1) * len(sequence) // num_of_parts]
                for i in range(num_of_parts)]

    def create_fern(self):
        """ Creation of fern descriptors and conversion to decimal system. """
        fern = [self.bin_attr_fern(image, self.coords) for image in self.images]
        return [list(map(lambda x: int(x, 2), self.fern_split(seq, self.num_of_parts))) for seq in fern]

    def prob_table(self, fern):
        """ Creating a probability table. """
        p_table = [[0 for i in range(2 ** self.num_of_parts)]
                   for j in range(self.num_of_parts)]
        for elem in fern:
            for index, string in enumerate(p_table):
                string[elem[index]] += 1

        for string in p_table:
            for i in range(len(string)):
                string[i] = round(string[i] / len(glob.glob(self.filepath)), 2)
        return p_table
