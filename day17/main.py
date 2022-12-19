#plot function
def plot(rocks,block,min_x,max_x):

    if len(rocks) == 0:
        max_yr = 4
    else:
        max_yr = max([y for (x, y) in rocks]) + 4
    if len(block) == 0:
        max_yb = 4
    else:
        max_yb = max([y for (x, y) in block]) + 4

    max_y = max_yr if max_yr > max_yb else max_yb
       
    print("")
    for j in range(max_y, 0, -1):
        plt_lst =["|"]
        for i in range(min_x+1,max_x):
            if (i,j) in rocks:                
                plt_lst.append("#")
            elif (i,j) in block:
                plt_lst.append("@")
            else:
                plt_lst.append(".")
        plt_lst.append("|")
        plt_lst.append(str(j))
        print("".join(plt_lst))
    #plot bottom
    plt_lst =["+"]
    for j in range(min_x+1, max_x):
        plt_lst.append("-")
    plt_lst.append("+")
    print("".join(plt_lst))
    print("")

c = []
f=open('input.txt', 'r')
while True:
    char = f.read(1)
    #break when no more characters
    if not char or char == "\n":
        break
    c.append(char)
f.close()

#initialize variables
rocks = set()
min_x = 0
max_x = 8
max_y = 0
blocks = [[(0,0), (1,0), (2,0), (3,0)], [(0,1),(1,0), (1,1), (1,2),(2,1)], \
          [(0,0),(1,0),(2,0),(2,1),(2,2)], [(0,0),(0,1),(0,2),(0,3)], \
           [(0,0),(0,1),(1,0),(1,1)]] 

#starting variables
block = [(x+3, y+4) for x, y in blocks[0]]        
num_rocks = 0
block_num = 0
jet_num = 0
step = 0


#while block_num < 1_000_000_000_000-1: #2022:
while True:
#while block_num < 2022:
    
    if num_rocks < len(rocks): # add new block
        block_num += 1
        max_y = max([y for (x, y) in rocks]) + 4
        ind=block_num % len(blocks)        
        block = [(x+3, y+max_y) for x, y in blocks[ind]]                
        num_rocks = len(rocks)


#    plot(rocks, block, min_x, max_x)
    jet_move = True
    direction = c[jet_num % len(c)]
    if direction == "<": #left
        for (x,y) in block:
            if (x-1,y) in rocks or x-1 == min_x:
                jet_move = False
    else: #right
        for (x,y) in block:
            if (x+1,y) in rocks or x+1 == max_x:
                jet_move = False
    if jet_move and direction == "<":
        block = [(x - 1, y) for x, y in block]
    elif jet_move and direction == ">":
        block = [(x + 1, y) for x, y in block]
    jet_num += 1

#    plot(rocks, block, min_x, max_x)    
        
    block_hit = False
    for (x,y) in block:
        if (x , y - 1) in rocks or y - 1 == 0: 
            block_hit = True
            
    if block_hit == True:
        for (x,y) in block:        
            rocks.add((x,y))
        
    else:
        block = [(x, y - 1) for x, y in block]
    step += 1

    if block_num == 2022:
      print("part1", max([y for (x, y) in rocks]))
      break

#plot(rocks, block, min_x, max_x)

