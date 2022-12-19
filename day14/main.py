#plot function
def plot(sands,rocks):
    max_y = max([y for (x, y) in rocks]) + 2
    max_rocks_x = max([x for (x, y) in rocks])
    min_rocks_x = min([x for (x, y) in rocks])
    max_sands_x = max([x for (x, y) in sands])
    min_sands_x = min([x for (x, y) in sands])

    min_x = min_rocks_x if min_rocks_x < min_sands_x else min_sands_x
    max_x = max_rocks_x if max_rocks_x > max_sands_x else max_sands_x
    
    print("")
    for j in range(0, max_y):
        plt_lst =[]
        for i in range(min_x,max_x + 1):
            if (i,j) in rocks:                
                plt_lst.append("#")
            elif (i,j) in sands:
                plt_lst.append("o")
            else:
                plt_lst.append(".")
        print("".join(plt_lst))
    #plot bottom
    plt_lst =[]
    for j in range(min_x, max_x +1):
        plt_lst.append("#")
    print("".join(plt_lst))
    print("")

#read file
rockpaths = []
f=open('input.txt', 'r')
lines = f.readlines()
for line in lines:
    pathstr = line.strip().replace('->',' ').split()
    path = []
    for pair in pathstr:
        xy = pair.split(',')
        path.append((int(xy[0]), int(xy[1])))
    rockpaths.append(path)
f.close()
rocks = set()
for i in range(len(rockpaths)):
    for j in range(len(rockpaths[i])-1):
        t1 = rockpaths[i][j]
        t2 = rockpaths[i][j+1]
        xr = range(min(t1[0], t2[0]), max(t1[0], t2[0]) + 1)
        yr = range(min(t1[1], t2[1]), max(t1[1], t2[1]) + 1)
        rocks.update({(x, y) for x in xr for y in yr})


#initialize variables
sands = set()
x, y = 500, 0   
step = 0
part1 = 0 
max_y = max([y for (x, y) in rocks])

#while step < 22:
while True:
    if (x,y) in sands:
        (x,y) = (500,0)
    if y > max_y and part1 == 0:
        part1 = 1
        print("part1:", len(sands))
    #sand falling down
    if ((x, y + 1) not in rocks and (x, y + 1) not in sands) \
       and y < max_y + 1: 
        y += 1
 #       print("a", x, y, sands)
    #sand move left
    elif (x-1 ,y+1) not in rocks and (x - 1, y + 1) not in sands \
         and y < max_y + 1:
        x -= 1
        y += 1
    #sand move right
    elif (x + 1 ,y + 1) not in rocks and (x + 1, y + 1) not in sands \
         and y < max_y + 1:
        x += 1
        y += 1
    else:
        step += 1
        sands.add((x,y))
#        plot(sands,rocks)
    if (x,y) == (500,0):
        print("part2:", len(sands))
        break
