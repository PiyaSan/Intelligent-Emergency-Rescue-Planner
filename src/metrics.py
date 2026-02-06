import time
def compute_path_cost(G, path):
    total_cost = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        total_cost += G.edges[u, v]['weight']
    return total_cost
def compute_execution_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    
    exec_time_ms = (end - start) * 1000  # convert to milliseconds
    return result, exec_time_ms

def compare_algorithms(G, start, goal, algorithms):
    results = {}

    for name, algo in algorithms.items():
        result, exec_time = compute_execution_time(algo, G, start, goal)
        # Handle both return formats: (path, cost) or just path
        if isinstance(result, tuple):
            path, cost = result
        else:
            path = result
            cost = compute_path_cost(G, path) if path else 0
        
        results[name] = {
            "path_length": len(path) if path else 0,
            "path_cost": cost,
            "execution_time": exec_time
        }

    return results
