#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program calculates the area of a triangle with 2 parameters


def area(base, height):
    # This'll calculate the area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("The area is " + str(area) + " units squared.")


def main():
    # This is asks for the base and height, then it  runs area()

    # variables
    base = 0
    height = 0

    # Welcomes
    input("Press Enter to start.")

    while True:
        try:
            base = int(input("What is the base: "))
            height = int(input("What is the height: "))

            # runs area()
            area(base, height)
            break
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main()
