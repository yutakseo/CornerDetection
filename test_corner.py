import time
start = time.time()
import cv2
from matplotlib import pyplot as plt
from array_maker import *
import numpy as np
from test_dataset import *
#from array_maker import *


def harris_corner(src, block_size, ksize, k):
    matrix = np.array(src, dtype=np.uint8)
    dst = cv2.cornerHarris(matrix, block_size, ksize, k)    
    return dst

        
        
src = test_data3
dst = harris_corner(src, 2, 3, 0.01)
end = time.time()
print("runtime : ",end -start)



#코너탐색의 결과를 시각화
visual_array("src", src)
visual_array("harris result", dst)
#plt.imshow(dst, cmap='jet')  # jet colormap을 사용하여 색상을 조정
#plt.show()

visual_array("bin",binary_corner(dst))