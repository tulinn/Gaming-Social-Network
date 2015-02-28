from ds import Queue

def BFS(network, originUser):
	neighbors = {}
	visited = {}
	for user in network:
		visited[user] = False
		neighbors[user] = []
	visited[originUser] = True
	queue = Queue()
	queue.enqueue(originUser)
	while not queue.isEmpty():
		u = queue.dequeue()
		for v in network[u]['connections']:
			if not visited[v]:
				visited[v] = True
				queue.enqueue(v)
				neighbors[u].append(v)
	return neighbors

#def DFS():