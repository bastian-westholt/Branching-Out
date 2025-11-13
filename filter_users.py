import json
from curses.ascii import isalpha, isdigit


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()

    while True:
        try:
            if filter_option == "name":
                name_to_search = input("Enter a name to filter users: ").strip()
                if any(char.isdigit() for char in name_to_search):
                    raise TypeError('Please enter alphabetic values, try again')
                filter_users_by_name(name_to_search)
                break

            elif filter_option == "age":
                age_to_search = int(input("Enter a age to filter users: ").strip())
                filter_by_age(age_to_search)
                break

            elif filter_option == "email":
                email_to_search = input("Enter a e-mail address to filter users: ").strip()
                filter_by_email(email_to_search)
                break


            else:
                print("Filtering by that option is not yet supported.")


        except ValueError:
            print(f'ValueError: Please enter a numeric value, try again')
        except TypeError as e:
            print(f'ValueError: {e}')
