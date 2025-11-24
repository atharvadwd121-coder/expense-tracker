# Personal Expense Tracker

## Project Summary
This is a simple Python based program that helps users track their daily financial expenses. It lets users enter spending details, view a history of transactions, calculate the total amount spent, and show their spending habits with a simple  graph using Matplotlib.

## Key Features
* **Add Expenses:** Enter the amount and description for new expenses.
* **View History:** Show a list of all recorded transactions .
* **Calculate Total:** Instantly see the total of all expenses entered currently .
* **Data Visualization:** Creates a line graph for vissualization of spendding analysis .
* **dynammically adjusted Graphs:** The graph automatically adjusts its width depending on the number of entries to keep it readable.

## Dependencies
To use this project, you need **Python 3.x** installed.

The project needs one external library for plotting graphs:
* **matplotlib**

## Installation & Setup

1.  **Save the code:**
    Save the Python script as `expense_tracker.py` (or any name you like).

2.  **Install the dependency:**
    Open your terminal or command prompt and run the following command to install `matplotlib`:

    ```
    pip install matplotlib
    ```

## Running the Code
1.  Open your terminal or command prompt.
2.  Go to the directory where you saved the file.
3.  Run the script using Python:

    ```
    python expense_tracker.py
    ```

## Instructions for Usage
Once the code is started  being run, you will see a menu with below listed options:

1.  **Add Expense (Option 1):**
    * Enter the amount spent (like `500`).
    * Enter a description (such as `Lunch`).
2.  **View Expenses (Option 2):**
    * Shows a list of all expenses you have added in the current session.
3.  **Show Total Spent (Option 3):**
    * Calculates and displays the total of your spending.
4.  **Plot Expenses Graph (Option 4):**
    * Opens a window with a line graph of your expenses.
    * *Note: You must add at least one expense before plotting.*
5.  **Exit (Option 5):**
    * Closes the application.
