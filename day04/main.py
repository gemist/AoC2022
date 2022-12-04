#initialize variables
sum0 = 0
sum1 = 0
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    lst = line.replace('\n','').split(',')
    pair0 = [eval(i) for i in lst[0].split('-')]
    pair1 = [eval(i) for i in lst[1].split('-')]
    #part 1
    if (pair0[0] <= pair1[0] and pair0[1] >= pair1[1]) or \
       (pair0[0]>=pair1[0] and pair0[1] <= pair1[1]):
        sum0+=1
    #part 2
    elif (pair0[0] >= pair1[0] and pair0[0] <= pair1[1]) or \
       (pair0[1] >= pair1[0] and pair0[1] <= pair1[1]):
        sum1+=1
    
print("part1:", sum0)
print("part2:", sum0+sum1)
    
f.close()
