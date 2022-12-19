cubes = []
f=open('input.txt', 'r')
lines = f.readlines()
for line in lines:
    x,y,z = line.replace('\n','').split(',')
    cubes.append((int(x),int(y),int(z)))

f.close()
#print(cubes)

def neighbours(cubes):
    num_neighbours = 0
    for i in range(len(cubes)):
        (x,y,z)=cubes[i]
        for j in [-1, 1]:
            if (x + j, y, z) in cubes:
                num_neighbours += 1
            if (x, y + j, z) in cubes:
                num_neighbours += 1
            if (x, y, z + j) in cubes:
                num_neighbours += 1

    return num_neighbours
print("part1:",len(cubes)*6-neighbours(cubes))


def is_neighbour(x,y,z, outside):
    flag = False

    for j in [-1, 1]:        
        if (x + j, y, z) in outside or  (x, y + j, z) in outside or \
           (x, y, z + j) in outside:
            flag = True
    return flag        

def inside_neighbours(cubes,inside):
    num_neighbours = 0
    for i in range(len(cubes)):
        (x,y,z)=cubes[i]
        for j in [-1, 1]:
            if (x + j, y, z) in inside:
                num_neighbours += 1
            if (x, y + j, z) in inside:
                num_neighbours += 1
            if (x, y, z + j) in inside:
                num_neighbours += 1

    return num_neighbours

#part 2
max_x = max((x for (x,y,z) in cubes))+1
max_y = max((y for (x,y,z) in cubes))+1
max_z = max((z for (x,y,z) in cubes))+1

queue = []
outside = [(0,0,0)]

for x in range(max_x):
    for y in range(max_y):
        for z in range(max_z):
            if (x,y,z) != (0,0,0): 
                queue.append((x,y,z))


while True:
    l=len(queue)
    delete =[]
    for i in range(l):
        if queue[i] in cubes:
            delete.append(queue[i])
        elif is_neighbour(*queue[i], outside) == True:
            outside.append(queue[i])
            delete.append(queue[i])
                

    for j in range(len(delete)):
        queue.remove(delete[j])
    if l == len(queue):
        break

inside = queue

print("part2:",len(cubes)*6-neighbours(cubes)-inside_neighbours(cubes,inside))    
            

