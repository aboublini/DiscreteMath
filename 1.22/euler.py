import networkx as nx
import matplotlib.pyplot as plt

# Get n from user
n = int(input("Please insert n: "))

# Create complete graph based on user input
G = nx.complete_graph(n)

# Illustrate graph
nx.draw(G, node_size = 700, with_labels=True)
plt.title("Complete Graph")
plt.show()

# Check if G is eulerian
if (nx.is_eulerian(G)):
    print("Graph G is Eulerian.")

    # If G is eulerian, print the eulerian circut sequence
    sequence = [u for u, v in nx.eulerian_circuit(G)]
    print(sequence)
else:
    print("Graph G is not Eulerian.")



