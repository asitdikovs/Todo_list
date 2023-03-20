#!/usr/bin/python3

user_list = []


# output list to the terminal
def print_out_list(todo_list):
    print("ToDo List:")
    for item, value in enumerate(todo_list):
        print(f"{item + 1}. {value}")
    print()


# add item to the list
def add_value_to_list(value):
    user_list.append(value)


# remove an item from the list
def remove_value_from_list(num):
    user_list.pop(int(num) - 1)


def welcome_message():
    print("Please, pick an option:")
    print("1. Show my ToDo List\n"
          "2. Add item to the list\n"
          "3. Remove item from the list\n"
          "Type 'q' to quit")


def options(num):
    # check if user has provided a valid input
    if num.isdigit():
        converted_num = int(num)
        if converted_num == 1:
            print_out_list(user_list)
        elif converted_num == 2:
            add_value_to_list(input("Type here: "))
        elif converted_num == 3:
            # check if the number provided is not higher than number of items in a list
            while True:
                print_out_list(user_list)
                remove_value = input("Type a number (q to quit this option): ")
                if remove_value.capitalize() == "Q":
                    break
                elif remove_value.isdigit():
                    if int(remove_value) <= len(user_list):
                        remove_value_from_list(remove_value)
                        break
                    else:
                        print("Provided value is higher than number of items in the list")

        else:
            print("Provide a number between 1-3")
    else:
        print("Invalid input, please try again.")


def main():
    print("Welcome user!")
    while True:
        welcome_message()
        user_input = input(": ")
        if user_input.capitalize() == 'Q':
            break
        options(user_input)


if __name__ == "__main__":
    main()
