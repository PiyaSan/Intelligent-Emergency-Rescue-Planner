import networkx as nx
import random
from src.bayesian_model import estimate_blockage_probability

def create_city_graph(size=10):
    G = nx.grid_2d_graph(size, size)

    for u, v in G.edges():
        G.edges[u, v]['distance'] = 1  # uniform distance
        G.edges[u, v]['traffic'] = random.randint(1, 5)
        G.edges[u, v]['risk'] = round(random.uniform(0.0, 0.3), 2)

    return G
# AI agents don't think in raw distance. They think in utility / cost.
# The cost function combines distance, traffic congestion, and risk using weighted parameters.
def compute_edge_cost(G, u, v, alpha=1.0, beta=1.5, gamma=2.0):
    distance = G.edges[u, v]['distance']
    traffic = G.edges[u, v]['traffic']
    risk = G.edges[u, v]['risk']

    cost = alpha * distance + beta * traffic + gamma * risk
    return cost
# Assign costs to all edges in the graph based on the cost function.
def assign_costs(G):
    for u, v in G.edges():
        distance = random.randint(1, 10)
        traffic = random.randint(1, 5)

        # Bayesian risk estimation
        risk = estimate_blockage_probability(rain=1)

        G[u][v]['distance'] = distance
        G[u][v]['traffic'] = traffic
        G[u][v]['risk'] = risk

        # Final edge weight combines everything
        G[u][v]['weight'] = distance + traffic + (risk * 10)

