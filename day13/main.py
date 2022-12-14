def compare(p1,p2):
        if isinstance(p1,int) and isinstance(p2,int):
                if p1 < p2:
                        return 1
                elif p1 == p2:
                        return 0
                else:
                        return -1
                        
        elif isinstance(p1,list) and isinstance(p2,list):
                i = 0
                while i < len(p1) and i < len(p2):
                        v = compare(p1[i], p2[i])
                        if v == 1:
                                return 1
                        if v == -1:
                                return -1
                        i += 1
                if i == len(p1) and i < len(p2):
                        return 1
                elif i == len(p2) and i< len(p1):
                        return -1
                else:
                        return 0
               
        elif isinstance(p1, int) and isinstance(p2, list):
                return compare([p1], p2)
        else:
                return compare(p1, [p2])
        
                

#read packets
packets=[]
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
        if line =="\n":
                continue
        packets.append(eval(line.replace("\n","")))        
f.close()

#part 1
pair_num = 1
sum=0
for i in range(0,len(packets),2):
        v = compare(packets[i],packets[i+1])
        if v == 1:
                sum += pair_num
        pair_num +=1        
print("part1:", sum)

#part 2
packets.append([[2]])
packets.append([[6]])
#order packets
j=0
while j < len(packets) -1:
        if compare(packets[j], packets[j+1])==-1:
                tmp = packets[j]
                packets[j] = packets[j+1]
                packets[j+1] = tmp

                j = -1
        j += 1
#find indexes of [[2]] and [[6]]        
for j in range(len(packets)):
        if packets[j] == [[2]]:
                ind1= j + 1
        if packets[j] == [[6]]:
                ind2 = j + 1
        
print("part2:",ind1*ind2)
