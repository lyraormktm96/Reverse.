## unrev is unreversed

## unrev = "76542"
##if isinstance(unrev, str):
    ##print(unrev[4])
    ##print(unrev[3])
    ##print(unrev[2])
    ##print(unrev[1])
    ##print(unrev[0])
# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(revs_number))