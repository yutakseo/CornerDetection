import cv2
import numpy as np
from array_maker import *
from test_dataset import *


def harris_corner(src, block_size, ksize, k):
    matrix = np.array(src, dtype=np.uint8)
    dst = cv2.cornerHarris(matrix, block_size, ksize, k)    
    return dst


def binary_corner(parameter):
    new_array = []
    new_row = []
    max_val = 0
    for i in range(len(parameter)):
        for j in range(len(parameter[i])):
            max_val = parameter[0][0]
            if parameter[i][j] < max_val:
                max_val = parameter[i][j]
    
    for i in range(len(parameter)):
        for j in range(len(parameter[i])):
            if max_val == parameter[i][j]:
                new_row.append(1)
            else:
                new_row.append(0)
        new_array.append(new_row)
        
             