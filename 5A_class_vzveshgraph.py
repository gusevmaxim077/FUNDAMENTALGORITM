import heapq


class vzveshgraph:
    def __init__(self, graph, start = None, end = None):
        self.g = graph
        self.s = start
        self.e = end
    def rebra(self):
        r = []
        for i in self.g:
            for j in self.g[i]:
                r.append((i,j[0]))
        return r
    def count_vertices(self):
        edges = self.rebra()
        """Подсчет количества вершин в графе."""
        vertices = set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
        return len(vertices)
    def get_vertices(self):
        edges = self.rebra()
        """Получение списка вершин из списка ребер."""
        vertices = set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
        return list(vertices)
    def wave_algorithm(self): # конечная и начальная вершины должны быть в исходном графе.
        """Реализация волнового алгоритма."""
        vertices = self.get_vertices()
        num_vertices = self.count_vertices()
        edges = self.rebra()
    
        # Инициализация массива пройденных вершин
        visited = {v: 0 for v in vertices}
        visited[self.s] = 1
    
        # Инициализация массива предков для восстановления пути
        parent = {v: None for v in vertices}
    
        # Флаг для проверки, найдена ли конечная вершина
        found = False
    
        # Шаг волнового алгоритма
        step = 1
    
        while True:
            # Флаг для проверки, были ли найдены новые вершины на текущем шаге
            new_vertices_found = False
        
            # Проходим по всем вершинам, которые были посещены на предыдущем шаге
            for v in vertices:
                if visited[v] == step:
                    # Проходим по всем соседям текущей вершины
                    for edge in edges:

                        if edge[0] == v and visited[edge[1]] == 0:
                            visited[edge[1]] = step + 1
                            parent[edge[1]] = v
                            new_vertices_found = True
                        if edge[1] == v and visited[edge[0]] == 0:
                            visited[edge[0]] = step + 1
                            parent[edge[0]] = v
                            new_vertices_found = True
        
            # Если конечная вершина найдена, выходим из цикла
            if visited[self.e] != 0:
                found = True
                break
        
            # Если новые вершины не найдены, выходим из цикла
            if not new_vertices_found:
                break
        
            step += 1
    
        # Восстановление пути
        if found:
           path = []
           current = self.e
           while current is not None:
               path.append(current)
               current = parent[current]
               path.reverse()
           return path, visited
        else:
            return None, visited
    def dijkstra(self):
# Инициализация расстояний
        distances = {vertex: float('inf') for vertex in self.g}
        distances[self.s] = 0
        print(distances)
        priority_queue = [(0, self.s)] # Приоритетная очередь куча()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Если текущее расстояние больше известного, пропускаем
            if current_distance > distances[current_vertex]:
                continue

            # Обновляем расстояния до соседей
            for neighbor, weight in self.g[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

x = vzveshgraph({
    0: [(1, 1), (2, 4)], # Вершина 0 связана с вершиной 1 вес( 1) и вершиной 2 вес( 4)
    1: [(2, 2), (3, 5)], # Вершина 1 связана с вершиной 2 вес( 2) и вершиной 3 вес( 5)
    2: [(3, 1)], # Вершина 2 связана с вершиной 3 вес( 1)
    3: [] # Вершина 3 не имеет исходящих ребер
},0,2)
print(vzveshgraph.dijkstra(x))
