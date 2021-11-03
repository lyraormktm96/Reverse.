##def fibonacci(n):
    ##if isinstance(n, int):
        ##if n = 3:
            ##fib = 0 + 1 + fibonacci(n-1)
            ## calculate fibonacci of group of 3 integers
        ##elif n <= 0:
            ##return "cannot be determined"
        ##else:
            ##return "input error"

##def test_float():
    ##assert fibonacci(1.1) == "input error"

# 0 1 1 2 3 5 8 13

# alternative would be to print a series starting at x and go to kth number
# x = 12
# 12 13 25 38 63 101

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    two_last = [0, 1]

    for i in range(2, n + 1):
        curr = two_last[0] + two_last[1]
        two_last[0] = two_last[1]
        two_last[1] = curr

    return two_last[1]

for i in range(0, 100):
    print(fib(i))