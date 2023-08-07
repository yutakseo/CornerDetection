import cv2
import numpy as np
from array_maker import *
from test_dataset import *
from ribosome_module import ribosome


def harris_corner(src):
    matrix = np.array(src, dtype=np.uint8)
    corner1 = cv2.cornerHarris(matrix, 2, 3, 0.01)
    
        
    visual_array(src)
    visual_array(corner1)
    
    
    plt.imshow(corner1, cmap='jet')  # jet colormap을 사용하여 색상을 조정
    plt.colorbar()
    plt.show()
    
    
    return corner13


harris_corner(test_data2)

'''


coord = np.where(corner > 0.1* corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)

for x, y in coord:
    cv2.circle(src, (x,y), 5, (0,0,255), 1, cv2.LINE_AA)

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)
#merged = np.hstack((corner_norm, src))

# 이미지를 화면에 표시
cv2.imshow('Gray Image', corner)
cv2.waitKey(0)
cv2.destroyAllWindows()

#visual_array(corners)
'''