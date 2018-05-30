def bfs_paths(graph, start, goal):
	"""
	Перебор методом поиска в ширину
	"""
	queue = [(start, [start])]
	while queue:
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next[0] == goal or next[1] == goal:
				return path + [next]
			else:
				queue.append((next, path + [next]))

def dfs_paths(graph, start, goal):
	"""
	Перебор методом поиска в глубину
	"""
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next[0] == goal or next[1] == goal:
				return path + [next]
			else:
				stack.append((next, path + [next]))


def shortest_path(graph, start, goal, path = []):
	"""
	Поиск короткого пути (оптимальный алгоритм)
	"""
	path = path + [start]
	if start[0] == goal or start[1] == goal:
		return path
	if start not in graph:
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			newpath = shortest_path(graph, node, goal, path)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest

def find_path(graph, start, goal, path=[]):
	"""
	Полный перебор
	"""
	path = path + [start]
	if start[0] == goal or start[1] == goal:
		return path
	if start not in graph:
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, goal, path)
			if newpath: return newpath
	return None