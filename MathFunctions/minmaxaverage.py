import math
import statistics as stats

# Input number of elements in list
count = int(input("How many numbers are in your list? "))

# Handle 0 count
while count <= 0:
    try:
        count = int(input("Please enter a positive number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Collecting numbers
listNum = []
for _ in range(count):  # Use '_' as a throwaway variable since 'i' isn't used in loop.
    while True:
        try:
            listNum.append(float(input("Enter number: ")))  # Accept floating-point numbers
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculations
lNum = max(listNum)
sNum = min(listNum)
average = sum(listNum) / count
median = stats.median(listNum)
variance = stats.variance(listNum)
stdDev = stats.stdev(listNum)

# Output
print(f"\nSorted list: {sorted(listNum)}")
print(f"The largest number is: {lNum}.")
print(f"The smallest number is: {sNum}.")
print(f"The average is: {average:.2f}.") # Rounded to 2 decimal places.
print(f"The median is: {median:.2f}.")
print(f"The variance is: {variance:.2f}.")
print(f"The standard deviation is: {stdDev:.2f}.")