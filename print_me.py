def print_me(x):
    if isinstance(x, int):
        print(x)

    elif isinstance(x, str):
        print(len(x))

def test_0():
    assert print_me(0) == 0

def test_string():
    assert print_me("justice") == 7
