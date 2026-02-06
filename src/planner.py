class RescuePlanner:
    def __init__(self, graph, ambulances):
        self.graph = graph
        self.ambulances = ambulances
    def select_best_ambulance(self, emergency_location):
        best_ambulance = None
        best_score = float('inf')

        for amb in self.ambulances:
            if amb.state == "idle":
                score = self.heuristic(amb.location, emergency_location)
                if score < best_score:
                    best_score = score
                    best_ambulance = amb

        return best_ambulance
    def heuristic(self, start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    def generate_plan(self, ambulance, emergency_location):
        plan = []

        plan.append("DISPATCH_AMBULANCE")
        plan.append("MOVE_TO_VICTIM")
        plan.append("PICK_VICTIM")
        plan.append("MOVE_TO_HOSPITAL")
        plan.append("RETURN_TO_BASE")

        return plan
    def execute_plan(self, ambulance, plan):
        for action in plan:
            print(f"Executing {action}")
            ambulance.update_status(action)
