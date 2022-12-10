#initialize variables
knots_pos = [(0,0) ]*10 
instructions =  {"R": (1,0), "L": (-1,0), "U": (0,1), "D":(0,-1)}
s1 = set()
s2 = set()

def knots_move(h, t):
    dist = abs(t[0] - h[0]) + abs(t[1] - h[1])
    if h[0] == t[0] and dist == 2:
        t = (t[0], h[1]-1 if h[1] > t[1] else h[1] + 1)
    if h[1] == t[1] and dist == 2:
        t = (h[0] - 1 if h[0] > t[0] else h[0] + 1,t[1])
    if dist > 2:
        if h[0] > t[0]:
            t = (t[0] + 1, t[1] + 1 if h[1] > t[1] else t[1] - 1)
        if h[0] < t[0]:
            t = (t[0] - 1, t[1] + 1 if h[1] > t[1] else t[1] - 1)
    return t

    
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","").split()
    for i in range(int(line[1])):
        knots_pos[0]=tuple(map(lambda i,j: i+j, knots_pos[0],instructions[line[0]]))
        for k in range(1,10):
            head_pos = knots_pos[k-1]
            knots_pos[k] = knots_move(head_pos,knots_pos[k])
            if k ==1:
                s1.add(knots_pos[k])
            if k ==9:
                s2.add(knots_pos[k])    
f.close()

print("part 1:",len(s1))
print("part 2:",len(s2))
