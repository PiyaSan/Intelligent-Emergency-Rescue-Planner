from collections import deque

def bfs_search(G, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

import heapq

def ucs_search(G, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, cost

        if current not in visited:
            visited.add(current)

            for neighbor in G.neighbors(current):
                edge_cost = G.edges[current, neighbor]['weight']
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    return None, float('inf')

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star_search(G, start, goal):
    priority_queue = [(0, start, [start], 0)]
    visited = set()

    while priority_queue:
        f_cost, current, path, g_cost = heapq.heappop(priority_queue)

        if current == goal:
            return path, g_cost

        if current not in visited:
            visited.add(current)

            for neighbor in G.neighbors(current):
                edge_cost = G.edges[current, neighbor]['weight']
                new_g = g_cost + edge_cost
                h = heuristic(neighbor, goal)
                new_f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    return None, float('inf')
