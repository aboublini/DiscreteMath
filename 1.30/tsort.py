import networkx as nx
import matplotlib.pyplot as plt
import random

# Create directed graph
G = nx.DiGraph()

# Nodes from exercise 1.30
V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Edges from exercise 1.30
U = [(1, 8), (2, 6), (2, 9), (3, 8), (4, 9), (6, 1), (6, 8), (7, 5), (8, 7), (9, 8)]

# Adding nodes and edges to the graph
G.add_nodes_from(V)
G.add_edges_from(U)

# Implementation of topological sorting algorithm (from class notes)
# List that will store the topological sorting of the nodes of G
L = []
# Copy of G (we will work with it)
H = G.copy()

# In this loop we will "create" the topological sorting sequence
while len(H) != 0:

    # notfound = True means that no vertex has indegree 0
    notfound = True

    for i in H.nodes():
        # Add node to L list (i is the node)
        L.append(i)
        # Remove the node from the copy of G
        H.remove_node(i)

        # A vertex has indegree 0
        notfound = False
        break

    # If no vertex has indegree 0 (if notfound is equal to true)
    if notfound:
        break

# If lengths of L and G are equal, we have the topological sequence
if len(L) == len(G):
    print("A topological sorting of G is: ", L)
else:
    print("No topological sort found. G contains a cycle.")

# Order in line all vertices of G
# Initialize coordinates
x = 0
y = 0

# Initialize an empty dictionary
position = {}

# Coordinates handling
for j in L:
    x = x + 1
    y = random.uniform(-1, 1)

    # Coordinates of node j
    position[j] = [x, y]

# Draw the graph
plt.figure()
nx.draw_networkx(G, pos=position)
plt.show()

