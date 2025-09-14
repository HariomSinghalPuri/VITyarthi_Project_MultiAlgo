# Pathfinding Project --- Using Multi Algorithm

A Python toolkit for simulating smart GPS navigation in grid-based maps, supporting static and dynamic obstacles, multiple search algorithms, and extensible heuristics.

## Features

- **Search Algorithms:** Breadth-First Search (BFS), Uniform Cost Search (UCS), and A*.
- **Heuristics:** Admissible heuristics (e.g., Manhattan distance).
- **Map Support:** Easily switch between small, medium, large, and dynamic maps.
- **Dynamic Obstacles:** Vehicles and objects with deterministic or scheduled movement ([`DynamicObstacles`](src/obstacles.py)).
- **Extensible:** Add new search strategies or heuristics.
- **Logging:** Save run results for analysis ([`log_results`](src/utils.py)).
- **Unit Tests:** Coverage for grid loading and search algorithms.

## Project Structure

```
├── run.py                # Main entry point
├── requirements.txt      # Dependencies
├── src/
│   ├── grid.py           # Grid and map handling
│   ├── heuristics.py     # Heuristic functions
│   ├── localsearch.py    # Local search (future)
│   ├── obstacles.py      # Dynamic obstacle logic
│   ├── search.py         # BFS, UCS, A* implementations
│   └── utils.py          # Logging and utilities
├── maps/                 # Map files (static & dynamic)
├── tests/                # Unit tests
└── report/               # Reports and analysis
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run a search:**
   ```bash
   python run.py --algo astar --map maps/small.txt --start 0,0 --goal 4,4
   ```

   - `--algo`: `bfs`, `ucs`, or `astar`
   - `--map`: Path to map file (e.g., `maps/medium.txt`)
   - `--start`/`--goal`: Coordinates (e.g., `0,0`)
   - `--diagonals`: Allow diagonal moves (`1` for True)
   - `--log`: Output log file (default: `out/run.log`)

3. **Example output:**
   ```
   Path: [(0, 0), (1, 0), ..., (4, 4)]
   Stats: {'nodes_expanded': 13, 'path_cost': 8}
   ```

## Maps

- **Format:** First line: width height. Next lines: grid costs (`-1` for obstacles).
- **Dynamic obstacles:** See [`maps/dynamic.json`](maps/dynamic.json).

## Testing

Run all tests:
```bash
pytest
```

## Extending

- Add new heuristics in [`src/heuristics.py`](src/heuristics.py).
- Implement new search strategies in [`src/search.py`](src/search.py).
- Add new map files in [`maps/`](maps/).

## License

MIT License.