import networkx as nx
import pygraphviz
from networkx.drawing.nx_agraph import read_dot
import matplotlib.pyplot as plt

G = read_dot("graph.dot")
L = read_dot("L0.dot")
P = read_dot("P0.dot")
'''
nx.draw(G, with_labels=True)
plt.savefig('G.png')
nx.draw(L, with_labels=True)
plt.savefig('L.png')
nx.draw(P, with_labels=True)
plt.savefig('P.png')
'''
print(G.number_of_nodes())

print(list(G.nodes))