import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def select_from_list(selection_prompt, selection_list):

    print(f"{selection_prompt}: ")

    for index, option in enumerate(selection_list, start=1):

        print(f"{index}. {option}")

    selection = input("Select a template number (or 'q' to quit): ")

    if selection == "q":
        return "Exiting template selection."

    try:
        selection_index = int(selection) - 1
        return selection_list[selection_index]

    except (ValueError, IndexError):
        return "Invalid selection."
