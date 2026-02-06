class Ambulance:
    def __init__(self, amb_id, location):
        self.id = amb_id
        self.location = location
        self.state = "idle"
        self.route = []
        self.target = None

    def assign_emergency(self, target, route):
        self.target = target
        self.route = route
        self.state = "moving"

    def move_step(self):
        if self.state == "moving" and self.route:
            self.location = self.route.pop(0)

            if self.location == self.target:
                self.state = "busy"

    def complete_rescue(self):
        if self.state == "busy":
            self.target = None
            self.route = []
            self.state = "idle"
    def update_status(self, action):
        if action == "DISPATCH_AMBULANCE":
            self.status = "moving"
        elif action == "PICK_VICTIM":
            self.status = "busy"
        elif action == "RETURN_TO_BASE":
            self.status = "idle"
