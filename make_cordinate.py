from test_dataset import *

def make_cordinate(data):
    grid = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                grid.append("("+str(j+1)+","+str(i+1)+")")
    return grid

print(make_cordinate(test_data4))