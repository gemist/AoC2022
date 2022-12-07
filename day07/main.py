#initialize variables
paths = {'/':0} #dictionary 
cur_path = ['/']

f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","").split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                cur_path.pop()
            elif line[2] == "/":
                cur_path = ['/']
            else:
                cur_path.append("/"+line[2])
    elif line[0] == "dir":
        paths["".join(cur_path) + "/" + line[1]] = 0
    else:
        paths["".join(cur_path)] += int(line[0])
        for i in range(1,len(cur_path)):
            paths["".join(cur_path[:-i])] += int(line[0])

print("part1:", sum(value for value in paths.values() if value  <= 100_000))
print("part2:", min(value for value in paths.values() if value >= paths['/'] - 40_000_000))
    
f.close()
