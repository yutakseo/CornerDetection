import time
from matplotlib import pyplot as plt
from ribosome_module import ribosome
from test_dataset import *
from test_dataset_answer import *
from array_maker import *
from corner_detector import harris_corner
from evaluation import evaluation



src = truncated
dst = harris_corner(src, 2, 3, 0.01)



#코너탐색의 결과를 시각화
visual_array("src", src)
visual_array("harris result", dst)

plt.imshow(dst, cmap='jet')  # jet colormap을 사용하여 색상을 조정
#plt.colorbar()
plt.show()

visual_array("bin",binary_corner(dst))


evaluation(test_data1_answer, binary_corner(dst))
