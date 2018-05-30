"""
Программа ищет оптимальное решение для задачи про два кувшина
Для работы требуется Python 3
"""
from enumerations import *

def calc_gcd(a, b):
	"""
	Считаем наибольший общий делитель
	"""
	while b:
		a, b = b, a % b
	return a

def make_edges(i, j, i_max, j_max):
	"""
	Создаем ребра для графа
	"""
	edges = []
	# Если кувшины не пусты, их можно опустошить
	if i != 0:
		edges.append((0, j))
	if j != 0:
		edges.append((i, 0))

	# Если кувшины не полные, их можно наполнить
	if i != i_max:
		edges.append((i_max, j))
	if j != j_max:
		edges.append((i, j_max))

	# Из непустого кувшина можно перелить в неполный
	if i != 0 and j_max-j >= i:
		edges.append((0, j+i))
	if j != 0 and i_max-i >= j:
		edges.append((i+j, 0))

	# Причем, если в неполном не хватит места,
	# то оба кувшина останутся непустыми
	if j != 0 and 0 < i_max-i < j:
		edges.append((i_max, j - (i_max-i)))
	if i != 0 and 0 < j_max-j < i:
		edges.append((i - (j_max-j), j_max))
	
	return edges

def create_graph(N, M):
	"""
	Строим граф
	"""
	graph = dict()
	# считаем наибольший общий делитель для оптимизации
	gcd = calc_gcd(N, M)
	print("gcd: ", gcd)
	for i in range(0, int(N/gcd + 1)):
		for j in range(0, int(M/gcd + 1)):
			graph[(i*gcd,j*gcd)] = set(make_edges(i, j, N, M))
	return graph

def show_res(path, target):
	"""
	Выводит результат
	"""
	if path is not None:
		print("Требуется шагов: ", len(path)-1)
		for node in path:
			print(node)
	else:
		print ("Нельзя с такими кувшинами получить", target, "л.")

def main():
	"""
	Главная функция
	"""
	print("Введите емкость N кувшина с водой:")
	N = int(input())
	print("Введите емкость M пустого кувшина:")
	M = int(input())
	print("Введите требуемую емкость L кувшина:")
	L = int(input())
	print("N: ", N, ", M: ", M, ", L: ", L)
	
	start = (0,0)
	graph = create_graph(N, M)
	print(graph)

	print("\nРезультат:")
	print("Brute Force (Полный перебор): ")
	path = find_path(graph, start, L)
	show_res(path, L)

	print("BFS (Поиск в ширину): ")
	path = bfs_paths(graph, start, L)
	show_res(path, L)

	print("DFS (Поиск в глубину): ")
	path = dfs_paths(graph, start, L)
	show_res(path, L)

	print("Optimal (Поиск кратчайшего пути): ")
	path = shortest_path(graph, start, L)
	show_res(path, L)

if __name__ == '__main__':
	main()