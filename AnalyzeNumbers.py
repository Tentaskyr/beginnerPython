def AnalyzeNumbers():
    count = int(input("How many numbers will you enter? "))
    numbers_list = []
    
    for _ in range(count):
        while True:
            try:
                numbers_list.append(int(input("Enter number: ")))
                break
            except ValueError:
                print("Invalid input. Please enter a correct integer.")
    
    def sumNumbers(numbers):            
        even_sum = 0
        even_count = 0
        odd_sum = 0
        odd_count = 0
    
        for num in numbers:
            if num % 2 == 0:    
                even_sum += num
                even_count += 1
            else:
                odd_sum += num
                odd_count += 1
        return even_sum, even_count, odd_sum, odd_count
    
    even_sum, even_count, odd_sum, odd_count = sumNumbers(numbers_list)
    print(f"The sum of {even_count} even numbers is {even_sum}.")
    print(f"The sum of {odd_count} odd numbers is {odd_sum}.")
    
    even_percentage = (even_count / count) * 100
    odd_percentage = (odd_count / count) * 100
    
    print(f"{even_percentage:.2f}% of the numbers were even.")
    print(f"{odd_percentage:.2f}% of the numbers were odd.")
    
    evens = [num for num in numbers_list if num % 2 == 0]
    odds = [num for num in numbers_list if num % 2 != 0]
    
    print(f"Even numbers: {evens}")
    print(f"Odd numbers: {odds}")

while True:
    AnalyzeNumbers()
    again = input("Do you want to run the program again? (y/n): ").strip().lower()
    if again != "y":
        break
    