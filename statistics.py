import matplotlib.pyplot as plt
import networkx as nx


def draw(G, new_edges, rightside_edges, rightside_nodes, nodes_to_connect, filename):
    plt.clf()
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    # nodes
    nx.draw_networkx_nodes(G, pos,
                           nodelist=list(G.nodes),
                           node_color='powderblue',
                           node_size=500,
                           alpha=0.8)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=rightside_nodes,
                           node_color='crimson',
                           node_size=500,
                           alpha=0.9)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=nodes_to_connect,
                           node_color='lawngreen',
                           node_size=500,
                           alpha=0.9)

    # edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(G, pos,
                           edgelist=new_edges,
                           width=8, alpha=0.5, edge_color='lawngreen')
    nx.draw_networkx_edges(G, pos,
                           edgelist=rightside_edges,
                           width=8, alpha=0.5, edge_color='crimson')
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    plt.axis("off")
    plt.draw()
    plt.savefig(filename, format="PNG", dpi=80)


# average degree of all nodes
def avg_degree_all(G):
    degs = nx.degree(G)
    deg = list(map((lambda tup: tup[1]), degs))
    return round(sum(deg) / len(deg), 2)


# average degree of non terminal nodes
def avg_degree_terminal(G):
    degs = nx.degree(G)
    lbls = dict(nx.get_node_attributes(G, 'label'))
    deg = []
    for d in degs:
        if lbls[d[0]] != 'Y' and lbls[d[0]] != 'X':
            deg.append(d[1])
    return round(sum(deg) / len(deg), 2)


def get_stats(G):
    nodes = nx.number_of_nodes(G)
    edges = nx.number_of_edges(G)
    con_comp = nx.number_connected_components(G)
    avg_deg_all = avg_degree_all(G)
    avg_deg_T = avg_degree_terminal(G)
    stats = "  Liczba wierzchołków: {} \n  Liczba krawędzi: {}\n  Liczba spójnych składowych: {}\n  Średni stopień " \
            "wierzchołków: {}\n  Średni stopień wierzchołków terminalnych: {}\n  Średni stopień wierzchołków w " \
            "spójnych składowych: {}".format(
             nodes, edges, con_comp, avg_deg_all, avg_deg_T, (avg_deg_all / con_comp))
    return stats


def nodes_gui(G):
    nodes = nx.number_of_nodes(G)
    return nodes
