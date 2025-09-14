from collections import deque
import heapq

def bfs(grid, start, goal):
    frontier = deque([start])
    came_from = {start: None}
    nodes_expanded = 0

    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1
        if current == goal:
            break
        for nxt in grid.neighbors(current):
            if nxt not in came_from:
                frontier.append(nxt)
                came_from[nxt] = current

    path = reconstruct_path(came_from, start, goal)
    stats = {"nodes_expanded": nodes_expanded, "path_cost": len(path)-1}
    return path, stats

def ucs(grid, start, goal):
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while frontier:
        current_cost, current = heapq.heappop(frontier)
        nodes_expanded += 1
        if current == goal:
            break
        for nxt in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, nxt))
                came_from[nxt] = current

    path = reconstruct_path(came_from, start, goal)
    stats = {"nodes_expanded": nodes_expanded, "path_cost": cost_so_far.get(goal, float("inf"))}
    return path, stats

def astar(grid, start, goal, heuristic):
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while frontier:
        _, current = heapq.heappop(frontier)
        nodes_expanded += 1
        if current == goal:
            break
        for nxt in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(nxt, goal)
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current

    path = reconstruct_path(came_from, start, goal)
    stats = {"nodes_expanded": nodes_expanded, "path_cost": cost_so_far.get(goal, float("inf"))}
    return path, stats

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
