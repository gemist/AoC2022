#initialize variables
cyclenum = 0
regvalue = 1
step = 20
sum1 = 0

#read instructions
instr = []
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","").split()
    instr.append(line)
f.close()

#part 1
for i in range(len(instr)):
    cyclenum += 1

    if cyclenum%step == 0 and cyclenum < 221:
        sum1 += cyclenum*regvalue
        step += 40
    
    if instr[i][0] == 'addx':
        addnum = int(instr[i][1])
        cyclenum += 1
    
        if cyclenum%step == 0 and cyclenum < 221:
            sum1 += cyclenum*regvalue
            step += 40
        regvalue += addnum
        
print("part 1:",sum1)

#part 2
cyclenum = 0
regvalue = 1
step = 40

def CRT_plot(lst,indx,regvalue):
    if indx >= regvalue-1 and indx <= regvalue + 1:
        lst.append("#")
    else:
        lst.append(".")
    return lst


lst = []
indx = 0
CRTlst =[]
for i in range(len(instr)):
    cyclenum += 1
    CRT_plot(lst,indx,regvalue)
    indx += 1
   
    if cyclenum%step == 0 and cyclenum < 241:
        CRTlst.append(lst)
        lst = []
        indx=0        
        step += 40

    if instr[i][0] == 'addx':
        addnum = int(instr[i][1])
        cyclenum += 1       

        CRT_plot(lst,indx,regvalue)
        indx += 1

        if cyclenum%step == 0 and cyclenum < 241:
            CRTlst.append(lst)
            lst = []
            indx=0
            step += 40
        regvalue += addnum

for k in range(len(CRTlst)):
    print("".join(CRTlst[k]))

