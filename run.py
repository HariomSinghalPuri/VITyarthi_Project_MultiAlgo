

import argparse
from src import grid, search, heuristics, utils

def main():
    parser = argparse.ArgumentParser(description="Pathfinding Project")
    parser.add_argument("--algo", choices=["bfs", "ucs", "astar"], required=True)
    parser.add_argument("--map", required=True)
    parser.add_argument("--start", required=True, help="format: x,y")
    parser.add_argument("--goal", required=True, help="format: x,y")
    parser.add_argument("--diagonals", type=int, default=0)
    parser.add_argument("--log", default="out/run.log")
    args = parser.parse_args()

    start = tuple(map(int, args.start.split(",")))
    goal = tuple(map(int, args.goal.split(",")))

    g = grid.Grid.from_file(args.map, diagonals=bool(args.diagonals))

    if args.algo == "bfs":
        path, stats = search.bfs(g, start, goal)
    elif args.algo == "ucs":
        path, stats = search.ucs(g, start, goal)
    else:
        h = heuristics.manhattan
        path, stats = search.astar(g, start, goal, h)

    utils.log_results(path, stats, args.log)
    print("Path:", path)
    print("Stats:", stats)

if __name__ == "__main__":
    main()
