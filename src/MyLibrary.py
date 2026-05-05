# /src/MyLibrary.py

import argparse
import os
import time

import pygradientify  # <-- Going to migrate to github.com/purectl pystyle fork, soon,

"""
# Remove what you need and keep what you need.
from pystyle import (
    Colors, Colorate, Anime, Banner, Box, System, Cursor, Write, Center,
    RainbowCycle, RainbowTime, Table, Progress, Menu, Tree, Columns, Figlet,
    Gradient, Confirm, Input, Select, Slider, SelectionGroup, RadioGroup, CheckboxGroup, Panel, Form, Theme, Loading, Icons, Badge, badge_success, badge_danger, badge_warning, badge_info, badge_primary, Divider, Sparkline, JsonViewer, Grid, hstack, vstack, LineChart, _sleep, Logger
)
"""

# Create the argument parser and add the --no-intro flag
parser = argparse.ArgumentParser()
parser.add_argument("--no-intro", action="store_true")

# Straight to example selection if the flag is provided.
# parser.add_argument("--example", action="store_int") <-- Integrate later

# if args.example:
#     # If an example is provided, skip the intro and go straight to the example selection.
#     args.no_intro = True  # Set no_intro to True if an example is provided
#     # Set the example selection to the provided example number
#     example_selection(args.example)


args = parser.parse_args()


clear = lambda: os.system("cls" if os.name == "nt" else "clear")


def intro():
    # Clear the screen and print the intro message
    clear()

    print(pygradientify.Colors.mystic("=" * 50, dir="h"))
    print("Welcome to My Skill Library!")
    print(pygradientify.Colors.mystic("=" * 50, dir="h"))

    time.sleep(2)
    return


def about_me():
    # Clear the screen and print the about me message
    clear()

    print(pygradientify.Colors.mystic("=" * 50, dir="h"))
    print("About Me")
    print(pygradientify.Colors.mystic("=" * 50, dir="h"))

    time.sleep(1)

    print("I'm a beginner programmer, inside a school.\n")

    print(
        pygradientify.Colors.mystic(
            """
         ░██         ░██
        ░██      ░██  ░██
       ░██      ░██    ░██
      ░██      ░██      ░██
       ░██    ░██      ░██
        ░██  ░██      ░██
            ░██
    """,
            dir="h",
        )
    )

    print("""
    - Name: Hxmbl
    - Github:
        - Personal: https://github.com/Hxmbl
        - School: https://github.com/y22Hxmbl

    - Country: United Kingdom
        """)

    time.sleep(5)


# Calc ban
calc_banned = False


class examples:
    # All examples go here!!

    def calc():

        global calc_banned

        if calc_banned:
            print(
                "You are banned from using the calculator. Please choose a different example."
            )
            time.sleep(2)
            return

        # Add error catching
        clear()
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("Welcome to the calculator!")
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))

        print(pygradientify.Colors.mystic("Initializing...", dir="h"))

        class operation:
            def add(a, b):
                return a + b

            def subtract(a, b):
                return a - b

            def multiply(a, b):
                return a * b

            def divide(a, b):
                return a / b

            def divide_with_remainder(a, b):
                full_division = a // b
                remainder = a % b
                return full_division, remainder

            def power(a, b):
                return a**b

            def sqrt(a):
                return a**0.5

            def remainder(a, b):
                return a % b

        def exit():
            print("Exiting...")
            time.sleep(1)
            return

        time.sleep(1)

        print("\nDone Initializing.")

        clear()

        while True:
            print(pygradientify.Colors.mystic("Available operations:", dir="h"))
            operations = {
                "1": ("add", operation.add),
                "2": ("subtract", operation.subtract),
                "3": ("multiply", operation.multiply),
                "4": ("divide", operation.divide),
                "5": ("divide with remainder", operation.divide_with_remainder),
                "6": ("power", operation.power),
                "7": ("remainder", operation.remainder),
                "8": ("sqrt", operation.sqrt),
                "x/q": ("exit", None),
            }

            for i in operations:
                print(f"- {i} {operations[i][0]}")

            # print(f"""
            # - 1 {operations["1"][0]}
            # - 2 {operations["2"][0]}
            # - 3 {operations["3"][0]}
            # """)

            print("")
            choice = input("Choose an operation: ")

            if choice == "add" or choice == "1":
                clear()
                try:
                    input_1 = float(
                        input(pygradientify.Colors.mystic("First number: "))
                    )
                    input_2 = float(
                        input(pygradientify.Colors.mystic("Second number: "))
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue
                result = operation.add(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "subtract" or choice == "2":
                try:
                    input_1 = float(
                        input(pygradientify.Colors.mystic("First number: "))
                    )
                    input_2 = float(
                        input(pygradientify.Colors.mystic("Second number: "))
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue
                result = operation.subtract(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "multiply" or choice == "3":
                try:
                    input_1 = float(
                        input(pygradientify.Colors.mystic("First number: "))
                    )
                    input_2 = float(
                        input(pygradientify.Colors.mystic("Second number: "))
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue
                result = operation.multiply(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "divide" or choice == "4":
                try:
                    input_1 = float(
                        input(pygradientify.Colors.mystic("First number: "))
                    )
                    input_2 = float(
                        input(pygradientify.Colors.mystic("Second number: "))
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue

                if input_2 == 0:
                    print("Cannot divide by zero. Nice try though.")
                    print("Type ok to return or type why to find out why.")

                    while True:
                        choice = input(
                            pygradientify.Colors.mystic("Your choice (ok/why): ")
                        )

                        if choice.lower() == "ok":
                            break
                        elif choice.lower() == "why":
                            clear()
                            print("""
Dividing by zero is undefined in mathematics because it leads to contradictions and breaks the fundamental properties of numbers.
You are trying to divide a number into zero parts. Technically you could say the result is 0 with a remainder of the original number. But this isn't how maths works.
It would break the properties of numbers. If you divide a number by another number, you should be able to multipy the result by the other number to get the original number back.
But if you divide by zero, you can't do that. It would break the properties of numbers and lead to contradictions.
So it's undefined.
It breaks the fundamental properties of maths, which is why it's undefined in mathematics.

Do you understand now? (y/n)
                            """)
                            while True:
                                choice = input(
                                    pygradientify.Colors.mystic("Your choice: ")
                                )

                                if choice.lower() == "y":
                                    print(
                                        "Great! Now don't touch the calculator ever again."
                                    )
                                    calc_banned = True
                                    time.sleep(3)
                                    return

                                elif choice.lower() == "n":
                                    print(
                                        "No worries, it can be a bit confusing. Ill repeat it 50 times."
                                    )
                                    time.sleep(2)
                                    for i in range(50):
                                        print("""
Dividing by zero is undefined in mathematics because it leads to contradictions and breaks the fundamental properties of numbers. You are trying to divide a number into zero parts. Technically you could say the result is 0 with a remainder of the original number. But this isn't how maths work. It would break the properties of numbers. If you divide a number by another number, you should be able to multipy the result by the other number to get the original number back. But if you divide by zero, you can't do that. It would break the properties of numbers and lead to contradictions. So it's undefined. It breaks the fundamental properties of maths, which is why it's undefined in mathematics.
                                        """)
                                        time.sleep(0.1)

                                else:
                                    print("Invalid choice. Please type y or n.")
                            break

                        else:
                            print("Invalid choice. Please type ok or why.")
                    continue

                result = operation.divide(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "divide with remainder" or choice == "5":
                try:
                    input_1 = float(
                        input(pygradientify.Colors.mystic("First number: "))
                    )
                    input_2 = float(
                        input(pygradientify.Colors.mystic("Second number: "))
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue

                result = operation.divide_with_remainder(input_1, input_2)
                full_division, remainder = result
                print(f"Result: {int(full_division)} remainder: {int(remainder)}")

            elif choice == "remainder" or choice == "7":
                try:
                    input_1 = float(input(pygradientify.Colors.mystic("Number: ")))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue
                result = operation.remainder(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "sqrt" or choice == "8":
                try:
                    input_1 = float(input(pygradientify.Colors.mystic("Number: ")))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(3)
                    clear()
                    continue
                result = operation.sqrt(input_1)
                print(f"Result: {result}")

            elif choice == "exit" or choice == "x" or choice == "q":
                print("Exiting...")
                time.sleep(1)
                clear()
                return

            else:
                print(pygradientify.Colors.mystic("Invalid choice.", dir="h"))

            input("\nPress any key to return to the example selection...")
            clear()

    def user_greeting():
        clear()
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("User Greeting")
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        time.sleep(1)
        name = input(pygradientify.Colors.mystic("Hi,") + " what's your name: ")
        print(f"\nHello, {pygradientify.Colors.mystic(name)}!")

        time.sleep(1)

        print(
            "\nThat was printed with an f-string, f strings allow you to embed expressions inside string literals."
        )

        time.sleep(4)

        print("\nLet's do it in a different way.")

        time.sleep(2)

        print("\nHello,", pygradientify.Colors.mystic(name) + "!")

        time.sleep(2)

        print(
            "\nThis was printed without an f-string. In this case, the name is simply concatenated with the string literal."
        )

        time.sleep(4)

        print("""

            The code for each:

            # f-string
            print(f"Hello, {name}!")

            # string concatenation
            print("Hello,", name + "!")


            """)

        input("Press Enter to continue...")

        return

    def example_3():
        clear()
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("Example 3")
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        time.sleep(1)

        return


# Add example functions above this line


def example_selection():
    while True:
        # Clear the screen and print the example selection message
        clear()

        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("Choose an example")
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))

        time.sleep(1)

        choices = {
            "1": ("calc", examples.calc),
            "2": ("user_greeting", examples.user_greeting),
            "3": ("example_3", examples.example_3),
        }

        print(f"""
        - 1 {choices["1"][0]}
        - 2 {choices["2"][0]}
        - 3 {choices["3"][0]}
        - x/q exit
        """)

        choice = input("Number of the example you want to run: ")

        time.sleep(1)

        if choice and choice[0] in choices:
            if len(choice) > 1:
                print(
                    "You entered more than one character, over here just take the first one."
                )
                time.sleep(1)
            choices[choice[0]][1]()

        elif choice.lower() == "x" or choice.lower() == "q":
            print("Exiting...")
            time.sleep(0.2)
            exit(0)  # Exit with a success code

        else:
            print("Invalid choice. Try again.")
            time.sleep(1)


def seq():
    # Call the functions sequentially
    if not args.no_intro:
        intro()

    if not args.no_intro:
        about_me()

    example_selection()


if __name__ == "__main__":
    try:
        seq()

    except KeyboardInterrupt:
        print("\nAborted by user!")
        exit(0)
