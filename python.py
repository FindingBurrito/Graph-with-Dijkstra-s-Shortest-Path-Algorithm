import heapq
import random


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].append((node2, weight))
        self.nodes[node2].append((node1, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def generate_random_graph(self, num_nodes, num_edges):
        for i in range(num_nodes):
            self.add_node(i)

        for _ in range(num_edges):
            node1, node2 = random.sample(range(num_nodes), 2)
            weight = random.randint(1, 20)
            self.add_edge(node1, node2, weight)


def main():
    graph = Graph()
    graph.generate_random_graph(10, 15)
    start_node = random.randint(0, 9)
    distances = graph.dijkstra(start_node)
    print(f"Shortest distances from node {start_node}:")
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")


if __name__ == "__main__":
    main()
