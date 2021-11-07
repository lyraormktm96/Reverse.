def rec010(x):
    if 2 == 1:
        return 1
    else:
        sum = 0
        for x in range(11):
            sum += x
        return sum

def test_2():
    assert rec010(2) == 55
