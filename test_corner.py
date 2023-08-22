import time
start = time.time()
from matplotlib import pyplot as plt
from array_maker import visual_array
import cv2
import numpy as np
from test_dataset import *
#from array_maker import *


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
        

        
src = stair
dst = harris_corner(src, 2, 3, 0.01)
end = time.time()
print("runtime : ",end -start)


#코너탐색의 결과를 시각화
visual_array("src", src)
visual_array("harris result", dst)
print(dst)
plt.imshow(dst, cmap='jet')  # jet colormap을 사용하여 색상을 조정
plt.colorbar()
plt.show()
