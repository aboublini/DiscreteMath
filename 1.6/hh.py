import matplotlib.pyplot as plt
import networkx as nx
import numpy


# Method that creates a simple graph using the Havel-Hakimi algorithm
def graph_exists(sequence):
    if nx.is_valid_degree_sequence_havel_hakimi(sequence):
        print("The sequence ", sequence, " can be realized by a simple graph.")

        # Create a random, simple graph G from given degree sequence
        G = nx.random_degree_sequence_graph(sequence, seed=numpy.random)

        # In case we want a circular layout
        # nx.draw_circular(G, with_labels = True)

        # Draw the graph G
        nx.draw_networkx(G, with_labels=True)

        # Set title to plot and show it
        plt.title("Sequence: " + str(sequence))
        plt.show()

        return True
    else:
        print("The sequence ", sequence, " cannot be realized by a simple graph.")
        return False


# Initialize sequences of exercise 1.6
Seq1 = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
Seq2 = [6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]


# Calling graph_exists() method
graph_exists(Seq1)
graph_exists(Seq2)
