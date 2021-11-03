num = int(input("enter the number of rows:"))
row_1 = 0
while row_1 < num:
    asterisk = row_1 + 1
    while asterisk > 0:
        print("*",end="")
        asterisk = asterisk - 1
    row_1 = row_1 + 1
    print()

for row_2 in reversed(range(0,5)):
    asterisk = row_2
    while asterisk > 0:
        print("*",end="")
        asterisk = asterisk - 1
    row_2 = row_2 + 1
    print()