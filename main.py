"""
main.py - Personal Finance Tracker
====================================
Entry point for the Personal Finance Tracker application.
This is a menu-driven command-line app that helps you manage
your personal income and expenses with ease.
Features:
  - Add income and expense transactions
  - View all / filtered transactions
  - Financial summary with category breakdown
  - Delete transactions
  - Export reports to text file
Run this file to launch the app:
  $ python main.py
Author : Mallikarjun Arjun
GitHub : https://github.com/yourusername
License: MIT
"""
import sys
import io
# ── Force UTF-8 output on Windows terminals ─────────────────
# This ensures box-drawing chars and icons display correctly.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
# ─────────────────────────────────────────────
# Import Core Modules
# ─────────────────────────────────────────────
from src.utils import (
    Colors,
    colored,
    clear_screen,
    print_header,
    print_divider,
    press_enter_to_continue,
    print_error,
)
from src.functions import (
    initialize_data_file,
    add_transaction,
    view_all_transactions,
    view_transactions_by_type,
    view_transactions_by_month,
    view_summary,
    delete_transaction,
    export_report,
)
# ─────────────────────────────────────────────
# Menu Display Functions
# ─────────────────────────────────────────────
def display_welcome_banner() -> None:
    """Display the application's welcome banner on startup."""
    clear_screen()
    print()
    print(colored("  ╔══════════════════════════════════════════════════════╗", Colors.MAGENTA))
    print(colored("  ║                                                      ║", Colors.MAGENTA))
    print(colored("  ║     💰  PERSONAL FINANCE TRACKER  💰                ║", Colors.BOLD + Colors.YELLOW))
    print(colored("  ║         Track. Save. Grow.                           ║", Colors.CYAN))
    print(colored("  ║                                                      ║", Colors.MAGENTA))
    print(colored("  ╚══════════════════════════════════════════════════════╝", Colors.MAGENTA))
    print()
    print(colored("  Built with Python 🐍  |  v1.0.0  |  MIT License", Colors.WHITE))
    print()
def display_main_menu() -> None:
    """Display the main navigation menu."""
    print_header("Main Menu")
    menu_items = [
        ("1", "➕", "Add Income"),
        ("2", "➖", "Add Expense"),
        ("3", "📋", "View All Transactions"),
        ("4", "🔍", "View Income Transactions"),
        ("5", "🔍", "View Expense Transactions"),
        ("6", "📅", "View by Month"),
        ("7", "📊", "Financial Summary"),
        ("8", "🗑 ", "Delete a Transaction"),
        ("9", "📤", "Export Report"),
        ("0", "🚪", "Exit"),
    ]
    for number, icon, label in menu_items:
        num_colored   = colored(f"  [{number}]", Colors.BOLD + Colors.CYAN)
        icon_colored  = colored(icon, Colors.YELLOW)
        label_colored = colored(label, Colors.WHITE)
        print(f"{num_colored} {icon_colored}  {label_colored}")
    print()
    print_divider()
def display_view_submenu() -> None:
    """Display the sub-menu for viewing transactions (not used directly; inline)."""
    pass
# ─────────────────────────────────────────────
# Input Handler
# ─────────────────────────────────────────────
def get_menu_choice() -> str:
    """
    Prompt the user to enter their menu selection.
    Returns:
        str: The user's input (stripped of whitespace).
    """
    return input(colored("  Enter your choice: ", Colors.BOLD + Colors.YELLOW)).strip()
# ─────────────────────────────────────────────
# Menu Action Router
# ─────────────────────────────────────────────
def handle_choice(choice: str) -> bool:
    """
    Execute the action that corresponds to the user's menu choice.
    Args:
        choice (str): The menu option selected by the user.
    Returns:
        bool: False if the user chose to exit, True otherwise.
    """
    clear_screen()
    if choice == "1":
        # ── Add Income ──
        print_header("Add Income")
        add_transaction("income")
    elif choice == "2":
        # ── Add Expense ──
        print_header("Add Expense")
        add_transaction("expense")
    elif choice == "3":
        # ── View All Transactions ──
        print_header("All Transactions")
        view_all_transactions()
    elif choice == "4":
        # ── View Income Only ──
        print_header("Income Transactions")
        view_transactions_by_type("income")
    elif choice == "5":
        # ── View Expenses Only ──
        print_header("Expense Transactions")
        view_transactions_by_type("expense")
    elif choice == "6":
        # ── View by Month ──
        print_header("Monthly View")
        view_transactions_by_month()
    elif choice == "7":
        # ── Financial Summary ──
        print_header("Financial Summary")
        view_summary()
    elif choice == "8":
        # ── Delete Transaction ──
        print_header("Delete Transaction")
        delete_transaction()
    elif choice == "9":
        # ── Export Report ──
        print_header("Export Report")
        export_report()
    elif choice == "0":
        # ── Exit ──
        clear_screen()
        print()
        print(colored("  ╔═════════════════════════════════════╗", Colors.MAGENTA))
        print(colored("  ║   Thanks for using Finance Tracker! ║", Colors.YELLOW))
        print(colored("  ║   Keep saving, keep growing! 💪      ║", Colors.CYAN))
        print(colored("  ╚═════════════════════════════════════╝", Colors.MAGENTA))
        print()
        return False  # Signal the main loop to exit
    else:
        # ── Invalid Choice ──
        print_error("Invalid choice. Please select a valid option from the menu.")
    press_enter_to_continue()
    return True  # Stay in the main loop
# ─────────────────────────────────────────────
# Application Entry Point
# ─────────────────────────────────────────────
def main() -> None:
    """
    Main function — entry point of the application.
    Initializes data, shows the welcome screen, and runs the menu loop.
    """
    # Set up data storage on first run
    initialize_data_file()
    # Show the welcome banner
    display_welcome_banner()
    press_enter_to_continue()
    # Main application loop
    running = True
    while running:
        clear_screen()
        display_main_menu()
        choice  = get_menu_choice()
        running = handle_choice(choice)
# ─────────────────────────────────────────────
# Run the app
# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print()
        print(colored("\n  👋  Interrupted. Goodbye!", Colors.YELLOW))
        print()
        sys.exit(0)
