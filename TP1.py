edges = [
    (1, 2), (2, 5), (1, 5), (3, 6), (6, 4), (4, 7), (7, 6)
]

def create_graph(edges):
    graph = {}
    for start, end in edges:
        graph.setdefault(start, []).append(end)
        graph.setdefault(end, []).append(start)

    # Sort adjacency lists to maintain numerical order
    for node in graph:
        graph[node].sort()

    return graph

def print_graph(graph):
    for vertex in sorted(graph):  # Sort keys to print in numerical order
        print(f"{vertex}: {graph[vertex]}")

def path_existence(graph, start, end):
    if start not in graph or end not in graph:
        return False

    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return False

if __name__ == "__main__":
    graph = create_graph(edges)
    print_graph(graph)

    start = int(input("Enter a starting node: "))
    end = int(input("Enter a destination node: "))

    print(path_existence(graph, start, end))
