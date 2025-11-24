# Personal Expense Tracker

## Project Summary
This is a simple, Python-based command-line application designed to help users track their daily financial expenses. It allows users to input spending details, view a history of transactions, calculate the total amount spent, and visualize their spending habits through a dynamic line graph using Matplotlib.

## Key Features
* **Add Expenses:** Input amount and description for new expenses.
* **View History:** Display a numbered list of all recorded transactions with the Indian Rupee (₹) symbol.
* **Calculate Total:** Instantly view the sum of all expenses entered in the current session.
* **Data Visualization:** Generate a line graph to visually analyze expense variations (requires Matplotlib).
* **Dynamic Graphing:** The graph automatically adjusts its width based on the number of entries to ensure readability.

## Dependencies
To run this project, you need to have **Python 3.x** installed.

The project requires one external library for plotting graphs:
* **matplotlib**

## Installation & Setup

1.  **Save the code:**
    Save the Python script as `expense_tracker.py` (or any name you prefer).

2.  **Install the dependency:**
    Open your terminal or command prompt and run the following command to install `matplotlib`:

    ```bash
    pip install matplotlib
    ```

## How to Run the Code
1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the file.
3.  Run the script using Python:

    ```bash
    python expense_tracker.py
    ```

## Instructions for Usage
Once the application is running, you will see a menu with the following options:

1.  **Add Expense (Option 1):**
    * Enter the amount spent (e.g., `500`).
    * Enter a description (e.g., `Lunch`).
2.  **View Expenses (Option 2):**
    * Displays a list of all expenses you have added in the current session.
3.  **Show Total Spent (Option 3):**
    * Calculates and prints the grand total of your spending.
4.  **Plot Expenses Graph (Option 4):**
    * Opens a window displaying a line graph of your expenses.
    * *Note: You must add at least one expense before plotting.*
5.  **Exit (Option 5):**
    * Closes the application.
