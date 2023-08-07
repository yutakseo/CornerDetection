from ribosome_module import ribosome
from test_dataset import *
from array_maker import visual_array


visual_array(ribosome(test_data4))

'''
visual_array(src)
visual_array(corner1)

plt.imshow(corner1, cmap='jet')  # jet colormap을 사용하여 색상을 조정
plt.colorbar()
plt.show()'''