import math

while True:
    while True:  # Inner loop to ensure valid radius input
        try:
            radius = float(input("What is the radius of your circle? "))
            if radius > 0:  # Valid radius: exit the loop
                break
            else:  # Handle zero or negative radius
                print("Please enter a positive number.")
        except ValueError:  # Handle non-numeric input
            print("Invalid input. Please enter a number.")

# Calculation
    area = math.pi * (radius ** 2)
    print(f"\nThe area of your circle is: {area:.2f}.")

# Loop or exit
    again = input("Do you want to calculate another circle? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break
