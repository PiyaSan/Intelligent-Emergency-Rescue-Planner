from src.environment import create_city_graph, assign_costs
from src.search_algorithms import a_star_search, bfs_search, ucs_search
from src.agents import Ambulance
from src.bayesian_model import estimate_blockage_probability
from src.planner import RescuePlanner
from src.metrics import compare_algorithms
from ui.visualizer import draw_graph, animate_ambulance


def main():
    G = create_city_graph()
    assign_costs(G)

    ambulance = Ambulance(amb_id=1, location=(0, 0))
    emergency_location = (5, 5)
    start_location = ambulance.location
    goal_location = emergency_location

    route, cost = a_star_search(G, ambulance.location, emergency_location)
    draw_graph(G, route)
    animate_ambulance(G, route, delay=0.5)

    ambulance.assign_emergency(emergency_location, route)

    print("Initial State:", ambulance.state)

    while ambulance.state != "idle":
        ambulance.move_step()
        print("Location:", ambulance.location, "State:", ambulance.state)

        if ambulance.state == "busy":
            print("Rescue in progress...")
            ambulance.complete_rescue()
            print("Rescue completed")

    print("Final State:", ambulance.state)
    blockage_risk = estimate_blockage_probability(rain=1)
    print("Estimated blockage probability:", blockage_risk)
    planner = RescuePlanner(G, [ambulance])
    best_amb = planner.select_best_ambulance(emergency_location)

    plan = planner.generate_plan(best_amb, emergency_location)
    planner.execute_plan(best_amb, plan)

    algorithms = {
        "BFS": bfs_search,
        "UCS": ucs_search,
        "A*": a_star_search
    }

    metrics = compare_algorithms(G,start_location,goal_location,algorithms)

    for algo, data in metrics.items():
        print(f"\n{algo} Results:")
        for k, v in data.items():
            print(f"{k}: {v}")

    bfs_cost = metrics["BFS"]["path_cost"]
    astar_cost = metrics["A*"]["path_cost"]

    bfs_time = metrics["BFS"]["execution_time"]
    astar_time = metrics["A*"]["execution_time"]

    cost_improvement = ((bfs_cost - astar_cost) / bfs_cost) * 100 if bfs_cost else 0
    time_improvement = ((bfs_time - astar_time) / bfs_time) * 100 if bfs_time else 0
    time_difference = bfs_time - astar_time

    print("\n--- Performance Improvement ---")
    print(f"Cost Improvement (A* vs BFS): {round(cost_improvement, 2)} %")
    print(f"Time Improvement (A* vs BFS): {round(time_improvement, 2)} %")
    TIME_PER_COST_UNIT = 0.5  # minutes per unit cost (assumption)
    print(f"BFS Time : {round(bfs_time, 4)} ms")
    print(f"A* Time  : {round(astar_time, 4)} ms")
    print(f"Time Difference (BFS - A*): {round(time_difference, 4)} ms")

    print("\n--- Estimated Rescue Time ---")
    print(f"BFS Rescue Time : {round(bfs_cost * TIME_PER_COST_UNIT, 2)} minutes")
    print(f"A* Rescue Time  : {round(astar_cost * TIME_PER_COST_UNIT, 2)} minutes")

    planner.execute_plan(best_amb, plan)

if __name__ == "__main__":
    main()
