import re
import os

def name_file():
    while True:
        user_file_input = input("Name your file: ").strip()
        if re.match(r"^[\w\-. ]+$", user_file_input):  # Allow alphanumeric, dashes, underscores, and spaces
            file_name = f"{user_file_input}.txt"
            try:
                # Check if the file already exists
                with open(file_name, "r"):
                    overwrite = input(f"File '{file_name}' already exists. Overwrite? (y/n): ").strip().lower()
                    if overwrite != "y":
                        delete = input(f"Do you want to delete all data in '{file_name}'? (y/n): ").strip().lower()
                        if delete == "y":
                            delete_file(file_name)
                        else:
                            print("Exiting to avoid overwriting.")
                            exit()

            except FileNotFoundError:
                pass  # File does not exist, so it's safe to create
            return file_name  # Return the file name after validation
        else:
            print("Invalid file name. Please use only letters, numbers, spaces, dashes, and underscores.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    else:
        print(f"File '{file_name}' does not exist.")

def save_user_data(file_name, mode):
    while True:
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            color = input("Enter favourite colour: ")
            break
        except ValueError:
            print("Invalid input. Please input correct values.")
    with open(file_name, mode) as file:
        file.write(f"{name}, {age}, {color}\n")

def read_user_data(file_name):
    print("\nCurrent saved user data:")
    print(f"{'Name':<20}{'Age':<10}{'Favourite Colour':<20}")
    print("-" * 50)
    with open(file_name, "r") as file:
        for line in file:
            name, age, color = line.strip().split(", ")
            print(f"{name:<20}{age:<10}{color:<20}")

def search_user(file_name):
    search_name = input("Enter the name to search for: ").strip()
    found = False
    with open(file_name, "r") as file:
        for line in file:
            if search_name.lower() in line.lower():
                print(f"Found: {line.strip()}")
                found = True
    if not found:
        print(f"No records found for '{search_name}'.")
        
def summarize_data(file_name):
    total_users = 0
    total_age = 0

    with open(file_name, "r") as file:
        for line in file:
            total_users += 1
            _, age, _ = line.strip().split(", ")
            total_age += int(age)

    print(f"\nSummary:")
    print(f"Total users: {total_users}")
    print(f"Average age: {total_age / total_users:.2f}" if total_users > 0 else "No data available.")

        
# Main program
file_name = name_file()

# First write to the file (overwrite if exists)
save_user_data(file_name, "w")  # Open in write mode

# Then switch to append mode for additional data
while True:
    read_user_data(file_name)
    again = input("Do you have more data to input? (y/n): ").strip().lower()
    if again != "y":
        break
    else:
        save_user_data(file_name, "a")  # Open in append mode

summarize_data(file_name)