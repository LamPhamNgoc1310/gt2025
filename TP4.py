# Minimum Spanning Tree with Kruskal and Prim

class Graph:
    def __init__(self, graph):
        self.V = len(graph)
        self.graph = graph

    def prim(self, start_node):
        """Finds Minimum Spanning Tree with Prim"""
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        key[start_node] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v, weight in enumerate(self.graph[u]):
                if weight > 0 and not mst_set[v] and key[v] > weight:
                    key[v] = weight
                    parent[v] = u

        print("\nPrim:")
        print("Edge \tWeight")
        for i in range(1, self.V):
            if parent[i] != -1:
                print(f"{parent[i] + 1} - {i + 1}\t{self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        """Finds the vertex with the minimum key value."""
        min_index = -1
        min_value = float('inf')
        for v, value in enumerate(key):
            if not mst_set[v] and value < min_value:
                min_value, min_index = value, v
        return min_index

    # Kruskal's Algorithm
    def find(self, parent, i):
        """Finds set of an element i (Uses path compression)."""
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        """Performs union by rank."""
        x_root, y_root = self.find(parent, x), self.find(parent, y)
        if x_root != y_root:
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

    def kruskal(self):
        """Kruskal's algorithm."""
        edges = [(u, v, self.graph[u][v]) for u in range(self.V) for v in range(u + 1, self.V) if self.graph[u][v] > 0]
        edges.sort(key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V
        result = []

        for u, v, w in edges:
            x, y = self.find(parent, u), self.find(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
                if len(result) == self.V - 1:
                    break

        print("\nKruskal:")
        print("Edge \tWeight")
        for u, v, w in result:
            print(f"{u + 1} - {v + 1}\t{w}")


def main():
    adj_matrix = [
        [0, 4, 0, 0, 1, 0, 2, 0, 0],
        [4, 0, 7, 0, 0, 5, 0, 0, 0],
        [0, 7, 0, 1, 0, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 6, 4, 3, 0],
        [1, 0, 0, 0, 0, 9, 10, 0, 0],
        [0, 5, 8, 6, 9, 0, 0, 0, 2],
        [2, 0, 0, 4, 10, 0, 2, 0, 8],
        [0, 0, 0, 3, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 2, 8, 1, 0],
    ]

    g = Graph(adj_matrix)

    while True:
        try:
            start_node = int(input("Enter the starting node (1-based index) for Prim: "))
            if 1 <= start_node <= len(adj_matrix):
                break
            else:
                print("Invalid node! Please enter a value between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    g.prim(start_node - 1)
    g.kruskal()


if __name__ == "__main__":
    main()
