class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, start):
        distances = [float('inf')] * self.V
        distances[start] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        return distances

# Example usage
V = 5  # Number of vertices
graph = Graph(V)

# Add edges (u, v, weight)
graph.add_edge(0, 1, 6)
graph.add_edge(0, 3, 7)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, -4)
graph.add_edge(2, 1, -2)
graph.add_edge(3, 2, -3)
graph.add_edge(3, 4, 9)
graph.add_edge(4, 0, 2)
graph.add_edge(4, 2, 7)

start_vertex = 0
shortest_distances = graph.bellman_ford(start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in enumerate(shortest_distances):
    print("Vertex", vertex, ":", distance)