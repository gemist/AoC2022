class TreeNode:
    def __init__(self, name, value,left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
            return f"TreeNode({self.name}): {self.left} {self.value} {self.right}"
        

    def evaluate(self):
        #leaf node
        if self.right is None and self.left is None:
            return int(self.value)


        #check which operation to apply
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        else:
            return self.left.evaluate() / self.right.evaluate()


nodes = {}
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    tmp = line.replace('\n','').split(':')
    name = tmp[0]
    lst = tmp[1].split()
    if len(lst) == 3:
        left = lst[0]
        right = lst[2]
        value = lst[1]
    else:
        value = lst[0]
        right=None
        left = None
    nodes[name] = TreeNode(name,value,left,right)
    

lft= nodes['root'].left
rgt=nodes['root'].right

for node in nodes.values():
    if node.left is not None and node.right is not None:
        node.left = nodes[node.left]
        node.right = nodes[node.right]
#    print(node)
print("part1", int(nodes['root'].evaluate()))

#part 2
#bisection
low = 1
nodes['humn'].value=low
low_val = nodes[rgt].evaluate()-nodes[lft].evaluate()
high =100_000_000_000_000
nodes['humn'].value=high
high_val = nodes[rgt].evaluate()-nodes[lft].evaluate()

while True:    
    new=(low+high)//2
    nodes['humn'].value=new
    tmp_val = nodes[rgt].evaluate()-nodes[lft].evaluate()
    if low_val*tmp_val < 0:
        high = new
    else:
        low = new
    if abs(tmp_val) < 1E-6:
        break
    
print("part2", nodes['humn'].value)
