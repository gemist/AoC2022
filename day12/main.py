#https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/breadth-first-search-bfs-algorithm/
def bfs(graph, start_node, target_node):
	visited = []
	visited.append(start_node)
	queue = []
	queue.append(start_node)
	parent = {}
	parent[start_node] = None

	path_found = False
	while queue:
		current_node = queue.pop(0)
		if current_node == target_node:
			path_found = True
			break

		for next_node in graph[current_node]:
			if next_node not in visited:
				visited.append(next_node)
				queue.append(next_node)
				parent[next_node] = current_node

	path = []
	if path_found:
		path.append(target_node)
		while parent[target_node] is not None:
			path.append(parent[target_node])
			target_node = parent[target_node]
		path.reverse()
	return path

#find element in matrix  with value/height = 0  
def bfs_traversal(graph, start_node):
        global matrix
        visited = []
        visited.append(start_node)
        queue = []
        queue.append(start_node)
        parent={}
        parent[start_node] = None

        path_found = False
        while queue:
                current_node = queue.pop(0)
                if matrix[current_node[0]][current_node[1]] == 0:
                        path_found = True
                        target_node = current_node
                        break

                
                for next_node in graph[current_node]:
                        if next_node not in visited:
                                queue.append(next_node)
                                visited.append(next_node)
                                parent[next_node] = current_node

        path = []
        if path_found:
                path.append(target_node)
                while parent[target_node] is not None:
                        path.append(parent[target_node])
                        target_node = parent[target_node]
                path.reverse()
        return path
                                    
#initialize variables
matrix = []
start_pos = []
goal_pos = []
visited_nodes = []
graph = dict()
a_positions = []

f=open('input.txt','r')

data=f.read().strip().split('\n')
f.close()

ncol=len(data[0])
nrow=len(data)

for i in range(nrow):
    line = data[i]
    lst = []

    for j in range(ncol):
        char = line[j]
        if char == 'S':
            start_pos = (i,j)
            char = 'a'
        elif char == 'E':
            goal_pos = (i,j)
            char = 'z'
        lst.append(ord(char)-ord('a'))
    matrix.append(lst)



#part 1
for i in range(nrow):
    for j in range(ncol):
        visitable_nodes = []
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if 0 <= i+m < nrow and 0 <= j+n < ncol and abs(n)+abs(m) == 1:
                    if matrix[i+m][j+n] - matrix[i][j] <= 1:
                        visitable_nodes.append((i+m, j+n))
        graph[(i, j)] = visitable_nodes
        
path = bfs(graph, start_pos, goal_pos)
print("part1:", len(path) - 1)


#part 2
for i in range(nrow):
    for j in range(ncol):
        visitable_nodes = []
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if 0 <= i+m < nrow and 0 <= j+n < ncol and abs(n)+abs(m) == 1:
                    if matrix[i+m][j+n] - matrix[i][j] >= -1:
                        visitable_nodes.append((i+m, j+n))
        graph[(i, j)] = visitable_nodes

path = bfs_traversal(graph, goal_pos)    
print("part2:",len(path)-1)
