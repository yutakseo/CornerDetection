import time
from matplotlib import pyplot as plt


from TEST_DATASET import *
from TEST_DATASET_ANSWER import *
from createArray import *
from cornerDetector import harris_corner
from modelEvaluation import evaluation


start = time.time()
src = stair_10by10_ans
dst = harris_corner(src, 2, 3, 0.01)
end = time.time()

print("Runtime : ",end -start)
#코너탐색의 결과를 시각화
visual_array("src", src)
visual_array("dst", dst)

plt.imshow(dst, cmap='jet')  # jet colormap을 사용하여 색상을 조정
#plt.colorbar()
plt.show()

visual_array("bin",binary_corner(dst))

#evaluation(test_data1_answer, binary_corner(dst))
#visual_array(create_padding(truncated))
#visual_array("",rule5)