def test(src, tval):
    total_cell = 0
    true_cell = 0
    for i in range(len(src)):
        for j in range(len(src[0])):
            if src[i][j] == tval[i][j]:
                true_cell += 1
            total_cell += 1
    
    average = true_cell / total_cell * 100
    
    return average

