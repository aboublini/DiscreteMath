import networkx as nx
import matplotlib.pyplot as plt

# Create a cyclic graph with 5 edges (you can test it with other edge numbers as well)
G = nx.cycle_graph(5)

# Draw graph
nx.draw_networkx(G, with_labels=True)

# Set title to plot and show it
plt.title("Cycle")
plt.show()
