import math

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        print("Goodbye!")
        break
    elif num < 0:
        print("The square root of a negative number is undefined in real numbers.")
    else:
        print(f"The square root of {num} is {math.sqrt(num)}.")