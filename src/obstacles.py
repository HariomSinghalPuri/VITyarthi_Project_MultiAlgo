import json

class DynamicObstacles:
    def __init__(self, objects):
        self.objects = objects  # list of dicts

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            data = json.load(f)
        return cls(data)

    def positions_at(self, t):
        """Return set of (x,y) occupied at time t"""
        occupied = set()
        for obj in self.objects:
            if "path" in obj:
                # looping vehicle
                path = obj["path"]
                idx = (t - obj.get("start_t", 0)) % len(path) if obj.get("loop", False) else (t - obj.get("start_t", 0))
                if 0 <= idx < len(path):
                    occupied.add(tuple(path[idx]))
            elif "schedule" in obj:
                for entry in obj["schedule"]:
                    if entry["t"] == t:
                        occupied.add(tuple(entry["pos"]))
        return occupied
