# Dijkstra
# Steps:
    # Ask input source (s) and target (t)
    # Return shortest path to move from (s) to (t) in (G)
    # Return weighted sum of shortest path above 

import heapq

def create_adjacency_matrix(edges, num_nodes):
    """Creates an adjacency matrix from a list of edges."""
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for src, dest, weight in edges:
        matrix[src][dest] = weight
        matrix[dest][src] = weight  # Assuming an undirected graph
    return matrix

def dijkstra(graph, src, tgt, node_map):
    """Finds the shortest path and its weight sum using Dijkstra's algorithm."""
    reverse_map = {v: k for k, v in node_map.items()}

    if src not in reverse_map or tgt not in reverse_map:
        return float('inf'), []

    src_idx, tgt_idx = reverse_map[src], reverse_map[tgt]
    num_nodes = len(graph)

    distances = [float('inf')] * num_nodes
    distances[src_idx] = 0
    previous = [-1] * num_nodes

    pq = [(0, src_idx)]  # Min-heap (distance, node)
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == tgt_idx:
            break  # Stop early if target is reached

        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0 and neighbor not in visited:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

    # Reconstruct shortest path
    path = []
    node = tgt_idx
    while node != -1:
        path.append(node_map[node])
        node = previous[node]
    path.reverse()

    return distances[tgt_idx], path if distances[tgt_idx] != float('inf') else []

if __name__ == '__main__':
    # Define edges (source, destination, weight)
    edges = [
        (0, 1, 4), (0, 2, 1), (1, 5, 3), (2, 3, 8), (2, 5, 7),
        (3, 7, 5), (4, 5, 1), (4, 7, 2), (4, 8, 2), (5, 7, 1),
        (6, 7, 3), (6, 8, 4), (6, 9, 4), (7, 8, 6), (7, 9, 7),
        (8, 9, 1)
    ]

    num_nodes = 10
    node_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
                5: 'F', 6: 'G', 7: 'H', 8: 'L', 9: 'M'}

    adjacency_matrix = create_adjacency_matrix(edges, num_nodes)

    # Get user input
    s = input('Enter source node: ').upper()
    t = input('Enter target node: ').upper()

    shortest_distance, shortest_path = dijkstra(adjacency_matrix, s, t, node_map)

    if shortest_distance != float('inf'):
        print(f"The shortest distance from {s} to {t} is {shortest_distance}")
        print(f"The shortest path is: {' -> '.join(shortest_path)}")
    else:
        print(f"There is no path from {s} to {t}")
