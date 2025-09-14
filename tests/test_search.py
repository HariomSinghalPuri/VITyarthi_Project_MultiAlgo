from src import grid, search, heuristics

def test_bfs_path():
    g = grid.Grid.from_file("maps/small.txt")
    path, stats = search.bfs(g, (0,0), (4,4))
    assert path[0] == (0,0)
    assert path[-1] == (4,4)
    assert stats["nodes_expanded"] > 0

def test_astar_path():
    g = grid.Grid.from_file("maps/small.txt")
    path, stats = search.astar(g, (0,0), (4,4), heuristics.manhattan)
    assert path[0] == (0,0)
    assert path[-1] == (4,4)
    assert stats["path_cost"] >= 0
