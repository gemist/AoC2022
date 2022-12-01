#initialize variables
cal_sum=0
cal_list=[]

#open input file
f=open('input.txt', 'r')
lines = f.readlines()

#do calculation
for line in lines:
    if line.strip() == "":
        cal_list.append(cal_sum)
        cal_sum = 0
    else:
        cal_sum += int(line)
#append last element to list
cal_list.append(cal_sum)
f.close() 
cal_list.sort(reverse=True)

#output
print("part 1:", cal_list[0])
print("part 2:", sum(cal_list[:3]))
