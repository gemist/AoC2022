#initialize variables
sum0 = 0
sum1 = 0
counter = 0

#priority num function
def priority(ascii_num):
    if ascii_num < 97:
        p = ascii_num - 38
    else:
        p = ascii_num - 96
    return p

f=open('input.txt','r')
lines = f.readlines()
for lin in lines:
    #part 1
    line=lin.replace("\n","")
    ind = int(len(line)/2)
    ascii_num =ord(set.intersection(set(line[:ind]),set(line[ind:])).pop())
    num=priority(ascii_num)
    sum0 += num

    #part 2
    if counter % 3 == 0:
        line0= line
    elif counter % 3 == 1:
        line1 = line
    else:
        line2 = line
        ascii_num = ord(set.intersection(set(line0), set(line1), set(line2)).pop())
        num=priority(ascii_num)
        sum1 += num

    counter+=1
    
print("part1:", sum0)
print("part2:", sum1)
    
f.close()
