from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])  # очередь для BFS
    visited = set()  # множество посещённых вершин

    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)

        # Если достигли цели, возвращаем путь
        if current_node == goal:
            return path

        # Проходим по соседям текущей вершины
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # если путь не найден

# Ввод данных
def input_graph():
    graph = {}
    num_edges = int(input("Введите количество рёбер в графе: "))
    
    for _ in range(num_edges):
        u, v = input("Введите рёбра в формате 'u v': ").split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # для невзвешенного графа добавляем обратно

    return graph

graph = input_graph()
start_node = input("Введите начальную вершину: ")
goal_node = input("Введите конечную вершину: ")

path = bfs_shortest_path(graph, start_node, goal_node)

if path:
    print("Кратчайший путь:", " -> ".join(path))
else:
    print("Путь не найден.")
