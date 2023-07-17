import cv2
import numpy as np
from test_dataset import *

src = np.array(test_data1, dtype=np.uint8)

corner = cv2.goodFeaturesToTrack(src, 100, 1, 2, blockSize=3, useHarrisDetector=True, k=0.03)

for i in src:
    cv2.circle(src, )