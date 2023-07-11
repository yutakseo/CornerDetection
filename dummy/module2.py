#route[y][x-1] route[y][x] route[y][x+1] 
route = [[1,1,1,1,1,1,1,1,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0]]

x=9
y=0


if route[y][x-1] != route[y][x]:
    route[y][x-1]+=1
    
print(route)




'''
while True:
    if route[y-1][x] == 1:                        
        y-= 1
    elif route[y-1][x+1] == 1:
        y-= 1
        x+= 1
    elif route[y][x+1] == 1:
        x+=1
    elif route[y+1][x+1] == 1:
        y+=1
        x+=1
    elif route[y+1][x] == 1:
        y+=1
    elif route[y+1][x-1] == 1:
        y+=1
        x-=1
    elif route[y][x-1] == 1:
        x-=1
    elif route[y-1][x-1] == 1:
    '''