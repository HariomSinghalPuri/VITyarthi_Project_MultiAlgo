from src.grid import Grid

def test_grid_load():
    g = Grid.from_file("maps/small.txt")
    assert g.width == 5
    assert g.height == 5
    assert g.passable((0,0)) is True
    assert g.passable((1,1)) is False
