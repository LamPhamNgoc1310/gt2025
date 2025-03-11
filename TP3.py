# Construct adjacent matrix for G
# Write Inorder algorithm to exploit the tree G which obeys behavior:
#   Input node lable (x)
#   Print out all nodes of subtree (x) in (Inorder)
from collections import defaultdict

def create_adjacency_matrix(edges, num_nodes):
    """Creates an adjacency matrix representation of a graph."""
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for start, end in edges:
        matrix[start - 1][end - 1] = 1
    return matrix

def perform_inorder_traversal(tree, node):
    """Performs an inorder traversal on the given tree."""
    if node not in tree:
        return []
    
    left, right = tree.get(node, [None, None]) + [None, None]  # Ensure two elements
    return perform_inorder_traversal(tree, left) + [node] + perform_inorder_traversal(tree, right)

# Graph Representation
edge_list = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
num_nodes = 8

# Construct and display adjacency matrix
adj_matrix = create_adjacency_matrix(edge_list, num_nodes)
print("Adjacency Matrix of Graph G:")
for row in adj_matrix:
    print(" ".join(map(str, row)))

# Tree Representation
tree_structure = defaultdict(list, {
    1: [3, 2], 
    2: [6, 5], 
    3: [4], 
    4: [8], 
    5: [7],          
    6: [],       
    7: [],           
    8: []    
})

# Inorder Traversal
node_label = int(input("\nEnter the node label (x) for inorder traversal: "))
inorder_output = perform_inorder_traversal(tree_structure, node_label)
print(f"Inorder traversal of subtree rooted at node {node_label}: {inorder_output}")

