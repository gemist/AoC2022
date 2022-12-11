import math
from copy import deepcopy

#read file
monkeys = {}
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","").lstrip().split(":")
#    print(line)
    if line[0].startswith("Monkey"):
        monkey_num = int(line[0].split()[1])
    if line[0].startswith("Starting items"):        
        items = [eval(i) for i in line[1].strip().split(',')]

    if line[0].startswith("Operation"):
        expression = line[1].strip().split("=")[1]
    if line[0].startswith("Test"):
        divisible = int(line[1].split('by')[1])
    if line[0].startswith("If true"):
        true_num = int(line[1].split()[3])
    if line[0].startswith("If false"):
        false_num = int(line[1].split()[3])

    if line[0] == '':
        monkeys[monkey_num] = {"items": items,
                               "expr": expression,
                               "div" : divisible,
                               "outcome" : [true_num, false_num],
                               "inspect_num": 0 }

#read last monkey
monkeys[monkey_num] = {"items": items,
                       "expr": expression,
                       "div" : divisible,
                       "outcome" : [true_num, false_num],
                       "inspect_num": 0}
f.close()
#create deepcopy for part2
monkeys2 = deepcopy(monkeys)

def monkey_business(monkeys,nrounds,worry_division, modulo):

    if modulo == True:
        mod_list = []
        for n in range(len(monkeys)):
            mod_list.append(monkeys[n]["div"])
        lcm=math.lcm(*map(int,mod_list))

    
    for i in range(nrounds):
        for m in range(len(monkeys)):
            num_items = len(monkeys[m]["items"])
            for l in range(num_items):
                if num_items == 0:
                    break
                old = monkeys[m]["items"][l]
                new = int(eval(monkeys[m]["expr"])/worry_division)
                if new%monkeys[m]["div"] == 0:
                    m_num = monkeys[m]["outcome"][0]
                else:
                    m_num  =  monkeys[m]["outcome"][1]
                if modulo == True:
                    monkeys[m_num]["items"].append(new%lcm)
                else:
                    monkeys[m_num]["items"].append(new)

            monkeys[m]["items"] =[]
            monkeys[m]["inspect_num"] += num_items     
 
    inspect = []
    for n in range(len(monkeys)):
        inspect.append(monkeys[n]["inspect_num"])
    inspect.sort(reverse=True)
    return inspect[0]*inspect[1]


print("part1:",monkey_business(monkeys,nrounds=20,worry_division=3,modulo=False))
print("part2:",monkey_business(monkeys2,nrounds=10_000,worry_division=1,modulo=True))



