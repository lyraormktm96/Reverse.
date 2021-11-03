def fibonacci(n):
    if isinstance(n, int):
        if n = 3:
            fib = 0 + 1 + fibonacci(n-1)
            ## calculate fibonacci of group of 3 integers
        elif n <= 0:
            return "cannot be determined"
        else:
            return "input error"

def test_float():
    assert fibonacci(1.1) == "input error"
