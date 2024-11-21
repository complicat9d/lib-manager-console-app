import os


def clear_terminal():
    """Clear the terminal screen based on the operating system."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
