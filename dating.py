#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 17, 2021
# This program asks the user to input their age
# and displays whether they are eligible to date
# some grandparents' grandchild.

def main():
    try:
        # get the user's age
        user_age_as_string = input("Enter your age: ")
        user_age_as_int = int(user_age_as_string)

    except ValueError:
        # error message
        print("{} is not a valid number.". format(user_age_as_string))

    else:
        # display whether they are eligible to date or not
        if user_age_as_int > 25 and user_age_as_int < 40:
            print("You are allowed to date our grandchild.")
        elif user_age_as_int > 40:
            print("You are too old for our grandchild.")
        elif user_age_as_int < 0:
            print("Age cannot be a negative number.")
        else:
            print("You are too young for our grandchild.")


if __name__ == "__main__":
    main()
