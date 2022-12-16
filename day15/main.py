sensors = []
beacons = []
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","").split(":")
    s = [int(x) for x in line[0].replace("Sensor at x=","").split(", y=")]
    b = [int(x) for x in line[1].replace("closest beacon is at x=","").split(", y=")]
    sensors.append(s)
    beacons.append(b)    
f.close()

def mannhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

#part 1
num_line = 2_000_000
empty = set()
for k in range(len(sensors)):
    d = mannhattan(sensors[k],beacons[k])
    dist =   d - abs(num_line - sensors[k][1]) 
    if dist >= 0:
        for i in range(-dist, dist+1, 1):
            empty.add(sensors[k][0]+i)

for i in range(len(beacons)):
    if beacons[i][1] == num_line:
        empty.discard(beacons[i][0])
print("part1:",len(empty))
        
#part 2
def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
	# Check for overlapping interval,
	# if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
            
        
    return(stack)
maximum = 4_000_000#20

empty_dict={}
#

for i in range(0,maximum+1):
    empty_dict[i] =[]

for k in range(len(sensors)):
    d = mannhattan(sensors[k],beacons[k])
    
    for j in range(0, d+1):
        y_max= sensors[k][1] + d - j
        y_min= sensors[k][1] - d + j        
        x_max = sensors[k][0] + j 
        x_min = sensors[k][0] - j

        if y_max <=maximum:
            if x_min - 1 >= 0 and x_max +1 <= maximum:
                empty_dict[y_max].append([x_min,x_max+1])
            elif x_min - 1 >= 0 and x_max +1 > maximum:
                empty_dict[y_max].append([x_min,maximum])
            elif x_min - 1 < 0 and x_max +1 <= maximum:
                empty_dict[y_max].append([0,x_max+1])
                
        if y_min >= 0:
            if x_min - 1 >= 0 and x_max +1 <= maximum:
                empty_dict[y_min].append([x_min,x_max+1])
            elif x_min - 1 >= 0 and x_max +1 > maximum:
                empty_dict[y_min].append([x_min,maximum])
            elif x_min - 1 < 0 and x_max +1 <= maximum:
                empty_dict[y_min].append([0,x_max+1])
        
 
for key in empty_dict.keys():
    if len(empty_dict[key]) > 0:
        empty_dict[key] = mergeIntervals(empty_dict[key])       

for key in empty_dict.keys():
    if len(empty_dict[key]) > 1:
        print("part2:",empty_dict[key][0][1]*4_000_000 + key)
        break
