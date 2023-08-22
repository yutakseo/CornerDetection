import numpy as np
import matplotlib.pyplot as plt


def make_array(data):
    matrix = np.array(data)
    return matrix

def visual_array(title:str, data):
    matrix = np.array(data)
    rows, cols = matrix.shape
    #사용할 컬러는 회색과 흰색
    cmap_custom = plt.cm.colors.ListedColormap(['gray', 'white'])

    #행렬을 이미지(그래프)로 표시
    plt.imshow(matrix, cmap=cmap_custom, interpolation='nearest', extent=[0, cols, rows, 0], origin='upper')
    plt.title(title)
    
    #격자를 설정, 간격은 1
    plt.xticks(np.arange(0, cols, step=1))
    plt.yticks(np.arange(0, rows, step=1))
    #x축을 상단에 고정
    plt.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)
    #격자의 스타일
    plt.grid(which='both', color='black', linestyle='-', linewidth=0.5)
    
    plt.show()


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
        
    
