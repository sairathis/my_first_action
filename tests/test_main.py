from src.main import add

def test_add():
    assert add(1, 2) == 3
    assert add(-2, 1) == -1
    assert add(0, 0) == 0