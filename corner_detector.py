import cv2
import numpy as np
from array_maker import *
from test_dataset import *


def harris_corner(src, block_size, ksize, k):
    matrix = np.array(src, dtype=np.uint8)
    dst = cv2.cornerHarris(matrix, block_size, ksize, k)    
    return dst
