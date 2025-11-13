# User filtering module for processing user data from JSON files
import json
from curses.ascii import isalpha, isdigit


def filter_users_by_name(name):
    """Filter users by name from the users.json file."""
    # Load users from JSON file
    with open("users.json", "r") as file:
        users = json.load(file)

    # Filter users by name (case-insensitive)
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    # Print each filtered user
    for user in filtered_users:
        print(user)


def filter_by_age(age):
    """Filter users by age from the users.json file."""
    # Load users from JSON file
    with open("users.json", "r") as file:
        users = json.load(file)

    # Filter users by age
    filtered_users = [user for user in users if user["age"] == int(age)]

    # Print each filtered user
    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """Filter users by email from the users.json file."""
    # Load users from JSON file
    with open("users.json", "r") as file:
        users = json.load(file)

    # Filter users by email (case-insensitive)
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    # Print each filtered user
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    # Get filter option from user
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()

    # Main filtering loop
    while True:
        try:
            # Filter by name
            if filter_option == "name":
                name_to_search = input("Enter a name to filter users: ").strip()
                # Validate that name contains only alphabetic characters
                if any(char.isdigit() for char in name_to_search):
                    raise TypeError('Please enter alphabetic values, try again')
                filter_users_by_name(name_to_search)
                break

            # Filter by age
            elif filter_option == "age":
                age_to_search = int(input("Enter a age to filter users: ").strip())
                filter_by_age(age_to_search)
                break

            # Filter by email
            elif filter_option == "email":
                email_to_search = input("Enter a e-mail address to filter users: ").strip()
                filter_by_email(email_to_search)
                break

            # Handle unsupported filter options
            else:
                print("Filtering by that option is not yet supported.")

        # Handle value errors (e.g., invalid age input)
        except ValueError:
            print(f'ValueError: Please enter a numeric value, try again')
        # Handle type errors (e.g., numeric characters in name)
        except TypeError as e:
            print(f'ValueError: {e}')
