import cv2
import numpy as np
from matplotlib import pyplot as plt
from test_dataset import *

src = np.array(test_data11, dtype=np.uint8)

corners = cv2.goodFeaturesToTrack(src, 3, 0.01, 10)
corners = np.int0(corners)




for i in corners:
    x, y = i.ravel()
    cv2.circle(src, (x,y), 3, 255, -1)
    
plt.imshow(src)
plt.show()
    


'''
corner = cv2.cornerHarris(src, 5, 3, 0.3)
ret, dst = cv2.threshold(corner, 0.1*corner.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(corner,np.float32(centroids),(5,5),(-1,-1),criteria)
for i in range(1, len(corners)):
    print(corners[i])
'''