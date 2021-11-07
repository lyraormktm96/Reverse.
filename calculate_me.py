def calculate_me(x, y):

    if isinstance(x, int):
        if isinstance(y, int):
            for x in range(20):
                for y in range(20):
                    sum = x + y
                    difference = x - y
                    return [sum, difference]

    elif isinstance(x, float) & isinstance(y, float):
        return "input error"

    elif isinstance(x, list) & isinstance(y, list):
        return "input error"

def calculate_me_int():
    assert calculate_me(14, 15) == [29, -1]

def calculate_me_float():
    assert calculate_me(2.0, 4.0) == "input error"

def test_list():
    assert calculate_me([1, 2], [8, 10]) == "input error"
