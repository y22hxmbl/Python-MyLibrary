# /src/MyLibrary.py

import argparse
import os
import time

import pygradientify

# Create the argument parser and add the --no-intro flag
parser = argparse.ArgumentParser()
parser.add_argument("--no-intro", action="store_true")
# parser.add_argument("--example", action="store_int") <-- Integrate later

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


# Add examples as we go


class examples:
    def calc():
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
                "5": ("power", operation.power),
                "6": ("sqrt", operation.sqrt),
                "7": ("remainder", operation.remainder),
                "x": ("exit", None),
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
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.add(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "subtract" or choice == "2":
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.subtract(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "multiply" or choice == "3":
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.multiply(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "divide" or choice == "4":
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.divide(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "power" or choice == "5":
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.power(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "sqrt" or choice == "6":
                input_1 = float(input(pygradientify.Colors.mystic("Number: ")))
                result = operation.sqrt(input_1)
                print(f"Result: {result}")

            elif choice == "remainder" or choice == "7":
                input_1 = float(input(pygradientify.Colors.mystic("First number: ")))
                input_2 = float(input(pygradientify.Colors.mystic("Second number: ")))
                result = operation.remainder(input_1, input_2)
                print(f"Result: {result}")

            elif choice == "exit" or choice == "x":
                return

            else:
                print(pygradientify.Colors.mystic("Invalid choice.", dir="h"))

            input("\nPress any key to return to the example selection...")
            clear()

    def example_2():
        clear()
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("Example 2")
        time.sleep(2)

        return

    def example_3():
        clear()
        print(pygradientify.Colors.mystic("=" * 50, dir="h"))
        print("Example 3")
        time.sleep(2)

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
            "2": ("example_2", examples.example_2),
            "3": ("example_3", examples.example_3),
        }

        print(f"""
        - 1 {choices["1"][0]}
        - 2 {choices["2"][0]}
        - 3 {choices["3"][0]}
        - x exit
        """)

        choice = input("Number of the example you want to run: ")

        time.sleep(1)

        if choice in choices:
            choices[choice][1]()

        elif choice.lower() == "x":
            print("Exiting...")
            time.sleep(0.2)
            exit(0)  # Exit with a success code
        else:
            print("Invalid choice, exiting.")
            time.sleep(1)
            exit(1)  # Exit with an error code, not return.


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
        exit(0)  # Exit with a success code, not an error.
