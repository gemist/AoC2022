from copy import deepcopy

#read file
with open('input.txt','r') as f:
    stacks, instructions = f.read().split("\n\n")

#create clean instructions
instr_clean=list(map(int,instructions.split()[1::2]))
instr_clean = [instr_clean[i:i+3] for i in range(0,len(instr_clean),3)]
    
#create lists from str for stacks    
stacks = stacks.splitlines()
#print("\n".join(stacks))
#transpose list
trans_list = list(map(list, zip(*stacks)))
#create clean stacks list
stacks_clean=[]
for i in range(1,len(trans_list),4):
    stacks_clean.append(list("".join(trans_list[i][len(trans_list[i])-2::-1]).strip()))

stacks_clean2 =deepcopy(stacks_clean)
#part 1
for instr in instr_clean:
    num_elements = instr[0]
    old = instr[1]-1
    new = instr[2]-1
    count = 0
    while count < num_elements:
        stacks_clean[new].append(stacks_clean[old].pop())
        count+=1

lst1=[]
for i in range(0,len(stacks_clean)):        
    lst1.append(stacks_clean[i].pop())

print("part1:", "".join(lst1))

#part2

for instr in instr_clean:
    num_elements = instr[0]
    old = instr[1]-1
    new = instr[2]-1
    count = 0
    lst=[]
    while count < num_elements:
        lst.append(stacks_clean2[old].pop())
        count+=1
    stacks_clean2[new].extend(lst[::-1])

lst2=[]
for i in range(0,len(stacks_clean2)):        
    lst2.append(stacks_clean2[i].pop())

print("part2:", "".join(lst2))
