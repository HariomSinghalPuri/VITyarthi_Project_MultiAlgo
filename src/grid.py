class Grid:
    def __init__(self, width, height, costs, diagonals=False):
        self.width = width
        self.height = height
        self.costs = costs  # 2D list of ints
        self.diagonals = diagonals

    @classmethod
    def from_file(cls, filename, diagonals=False):
        with open(filename) as f:
            w, h = map(int, f.readline().split())
            costs = []
            for _ in range(h):
                row = list(map(int, f.readline().split()))
                costs.append(row)
        return cls(w, h, costs, diagonals)

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos):
        x, y = pos
        return self.costs[y][x] != -1

    def neighbors(self, pos):
        x, y = pos
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        if self.diagonals:
            steps += [(1,1),(-1,-1),(1,-1),(-1,1)]
        for dx, dy in steps:
            nxt = (x+dx, y+dy)
            if self.in_bounds(nxt) and self.passable(nxt):
                yield nxt

    def cost(self, pos):
        x, y = pos
        return max(1, self.costs[y][x])
