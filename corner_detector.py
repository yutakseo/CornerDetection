import cv2
import numpy as np
from array_maker import *
from test_dataset import *


def harris_corner(src, block_size, ksize, k):
    matrix = np.array(src, dtype=np.uint8)
    dst = cv2.cornerHarris(matrix, block_size, ksize, k)
    
    visual_array("src",src)
    visual_array("harris result", dst)
    
    plt.imshow(dst, cmap='jet')  # jet colormap을 사용하여 색상을 조정
    plt.colorbar()
    plt.show()
    
    return dst
