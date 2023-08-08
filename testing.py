def test(src, tval):
    for i in src:
        for j in src[i]:
            if src[i][j] == tval[i][j]:
                right +=1
            total += 1
            