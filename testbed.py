# 시와 토마시 코너 검출 (corner_goodFeature.py)

import cv2
import numpy as np
from array_maker import visual_array
from test_dataset import *

img = np.array(test_data4, dtype=np.uint8)

# 시-토마스의 코너 검출 메서드
corners = cv2.goodFeaturesToTrack(img, 3, 0.01, 1)
# 실수 좌표를 정수 좌표로 변환
corners = np.int32(corners)


# 좌표에 동그라미 표시
for corner in corners:
    x, y = corner[0]
    cv2.circle(img, (x, y), 5, (0,0,125), 1, cv2.LINE_AA)

result = np.array(img)
visual_array(result)
