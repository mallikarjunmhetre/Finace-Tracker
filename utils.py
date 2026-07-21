"""
utils.py - Utility Functions for Personal Finance Tracker
==========================================================
This module contains helper/utility functions used across the application.
These include formatting, date validation, color output, and display helpers.
Author : Mallikarjun Arjun
License: MIT
"""
import os
import datetime
# ─────────────────────────────────────────────
# ANSI Color Codes for Terminal Styling
# ─────────────────────────────────────────────
class Colors:
    """A simple class to hold ANSI color escape codes for terminal output."""
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
def colored(text: str, color: str) -> str:
    """
    Wrap a string with an ANSI color code.
    Args:
        text  (str): The text to colorize.
        color (str): The color code from the Colors class.
    Returns:
        str: The colorized string.
    """
    return f"{color}{text}{Colors.RESET}"
def clear_screen() -> None:
    """Clear the terminal screen (works on Windows, macOS, and Linux)."""
    os.system("cls" if os.name == "nt" else "clear")
def print_divider(char: str = "─", width: int = 60, color: str = Colors.CYAN) -> None:
    """
    Print a styled horizontal divider line.
    Args:
        char  (str): The character to use for the divider. Default is '─'.
        width (int): The width of the divider. Default is 60.
        color (str): ANSI color code. Default is cyan.
    """
    print(colored(char * width, color))
def print_header(title: str, width: int = 60) -> None:
    """
    Print a formatted section header with borders.
    Args:
        title (str): The title text to display inside the header.
        width (int): The total width of the header box. Default is 60.
    """
    print()
    print_divider("═", width, Colors.MAGENTA)
    print(colored(f"  💰  {title.upper()}", Colors.BOLD + Colors.YELLOW))
    print_divider("═", width, Colors.MAGENTA)
    print()
def get_current_date() -> str:
    """
    Return today's date as a formatted string (YYYY-MM-DD).
    Returns:
        str: Today's date in ISO format.
    """
    return datetime.date.today().isoformat()
def validate_date(date_string: str) -> bool:
    """
    Validate whether a string matches the YYYY-MM-DD date format.
    Args:
        date_string (str): The date string to validate.
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.date.fromisoformat(date_string)
        return True
    except ValueError:
        return False
def format_currency(amount: float) -> str:
    """
    Format a float amount as a currency string with two decimal places.
    Args:
        amount (float): The monetary amount to format.
    Returns:
        str: A formatted currency string, e.g., '₹1,234.56'.
    """
    return f"Rs.{amount:,.2f}"
def get_valid_float(prompt: str, allow_negative: bool = False) -> float:
    """
    Prompt the user for a valid floating-point number, with retry on error.
    Args:
        prompt        (str) : The input prompt to display to the user.
        allow_negative(bool): If False, only positive values are accepted.
    Returns:
        float: A validated float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if not allow_negative and value <= 0:
                print(colored("  ⚠  Amount must be a positive number. Try again.", Colors.YELLOW))
                continue
            return value
        except ValueError:
            print(colored("  ✗  Invalid input. Please enter a numeric value.", Colors.RED))
def get_valid_date(prompt: str) -> str:
    """
    Prompt the user for a valid date string (YYYY-MM-DD), with retry on error.
    Args:
        prompt (str): The input prompt to display to the user.
    Returns:
        str: A validated date string in YYYY-MM-DD format.
    """
    while True:
        date_input = input(prompt).strip()
        # Allow the user to press Enter to use today's date
        if date_input == "":
            return get_current_date()
        if validate_date(date_input):
            return date_input
        print(colored("  ✗  Invalid date format. Use YYYY-MM-DD or press Enter for today.", Colors.RED))
def get_non_empty_string(prompt: str) -> str:
    """
    Prompt the user for a non-empty string, with retry if blank.
    Args:
        prompt (str): The input prompt to display to the user.
    Returns:
        str: A non-empty, stripped string from the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(colored("  ✗  This field cannot be empty. Please enter a value.", Colors.RED))
def print_success(message: str) -> None:
    """Print a success message in green with a checkmark."""
    print(colored(f"\n  ✓  {message}", Colors.GREEN))
def print_error(message: str) -> None:
    """Print an error message in red with an X."""
    print(colored(f"\n  ✗  {message}", Colors.RED))
def print_info(message: str) -> None:
    """Print an informational message in cyan."""
    print(colored(f"\n  ℹ  {message}", Colors.CYAN))
def press_enter_to_continue() -> None:
    """Pause execution until the user presses Enter."""
    print()
    input(colored("  Press Enter to continue...", Colors.CYAN))
