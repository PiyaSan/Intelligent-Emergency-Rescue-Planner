import matplotlib.pyplot as plt
import networkx as nx
import time

def draw_graph(G, path=None, blocked_threshold=0.6):
    pos = {node: node for node in G.nodes()}
    
    plt.figure(figsize=(6, 6))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='lightblue')

    # Draw edges
    safe_edges = []
    risky_edges = []

    for u, v in G.edges():
        if G[u][v]['risk'] > blocked_threshold:
            risky_edges.append((u, v))
        else:
            safe_edges.append((u, v))

    nx.draw_networkx_edges(G, pos, edgelist=safe_edges, edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=risky_edges, edge_color='red', width=2)

    # Highlight path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)

    plt.axis('off')
    plt.show()

def animate_ambulance(G, path, delay=0.5):
    pos = {node: node for node in G.nodes()}

    for i in range(len(path)):
        plt.figure(figsize=(6, 6))

        nx.draw(G, pos, node_size=200, node_color='lightblue', edge_color='gray')

        # Draw path so far
        if i > 0:
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=list(zip(path[:i], path[1:i+1])),
                edge_color='green',
                width=3
            )

        # Draw ambulance
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=[path[i]],
            node_color='orange',
            node_size=300
        )

        plt.title(f"Ambulance moving to {path[-1]}")
        plt.axis('off')
        plt.show()
        time.sleep(delay)
