import networkx as nx
import matplotlib.pyplot as plt

# Create a 3*3 lattice graph (you can test it with other dimensions as well)
G = nx.grid_graph(dim=(3, 3))

# Draw graph
nx.draw_networkx(G, with_labels=True)

# Set title to plot and show it
plt.title("Lattice")
plt.show()
