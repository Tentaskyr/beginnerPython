import re
import os
import json

def name_file():
        while True:
                user_file_input = input("Name your file: ").strip()
                if re.match(r"^[\w\-. ]+$", user_file_input):
                        file_name = f"{user_file_input}.json"
                        try:
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
                        return file_name
                else:
                        print("Invalid file name. Please use only valid characters.")

def delete_file(file_name):
        if os.path.exists(file_name):
                os.remove(file_name)
                print(f"File '{file_name}' deleted.")
        else:
                print(f"File '{file_name}' does not exist.")

def save_user_data(file_name):
        # Load existing data or initialize as empty
        try:
                with open(file_name, "r") as file:
                        data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                data = []

        # Get user input
        while True:
                try:
                        name = input("Enter name: ")
                        age = int(input("Enter age: "))
                        color = input("Enter favourite colour: ")
                        break
                except ValueError:
                        print("Invalid input. Please input correct values.")

        # Append new data
        data.append({"name": name, "age": age, "favourite_color": color})

        # Save updated data back to file
        with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

def read_user_data(file_name):
        try:
                with open(file_name, "r") as file:
                        data = json.load(file)
                        print("\nSaved user data:")
                        for entry in data:
                                print(f"Name: {entry['name']}, Age: {entry['age']}, Favourite Colour: {entry['favourite_color']}")
        except (FileNotFoundError, json.JSONDecodeError):
                print("No data found or file is empty.")

def summarize_data(file_name):
        try:
                with open(file_name, "r") as file:
                        data = json.load(file)
                        total_users = len(data)
                        total_age = sum(user["age"] for user in data)
                        average_age = total_age / total_users if total_users > 0 else 0

                        # Count favorite colors
                        color_count = {}
                        for user in data:
                                color = user["favourite_color"]
                                color_count[color] = color_count.get(color, 0) + 1

                        # Print summary
                        print("\nSummary of Data:")
                        print(f"Total Users: {total_users}")
                        print(f"Average Age: {average_age:.2f}")

                        # Most popular color, youngest and oldest users
                        most_popular_color = max(color_count, key=color_count.get)
                        youngest_user = min(data, key=lambda x: x["age"])
                        oldest_user = max(data, key=lambda x: x["age"])
                        print(f"Most Popular Color: {most_popular_color}")
                        print(f"Youngest User: {youngest_user['name']} ({youngest_user['age']} years)")
                        print(f"Oldest User: {oldest_user['name']} ({oldest_user['age']} years)")

        except (FileNotFoundError, json.JSONDecodeError):
                print("No data found or file is empty.")

# Main program
file_name = name_file()

# Save data
save_user_data(file_name)

# Loop for additional data
while True:
        read_user_data(file_name)
        again = input("Do you have more data to input? (y/n): ").strip().lower()
        if again != "y":
                break
        save_user_data(file_name)

# Summarize data
summarize_data(file_name)
