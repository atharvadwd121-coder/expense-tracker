```markdown
# Simple Expense Tracker (Python)

A lightweight, beginner‑friendly expense tracker that runs in the terminal and helps you record your daily spending, see a total, and visualize your expenses using a simple line graph.

---

## What this project does

This project is a small command‑line application where you can:

- Add expenses with an amount and a short description  
- View all recorded expenses in a neat, numbered list  
- See the total money spent so far  
- Plot a line graph of your expenses using their descriptions and amounts  

It is designed to be easy to understand and extend, especially for beginners learning Python.

---

## Features

- Add expense entries with amount and description  
- View all saved expenses in a user‑friendly format  
- Calculate and display the total money spent  
- Plot a line graph of your expenses using matplotlib  
- Simple text‑menu interface with options 1–5  
- Handles empty states (e.g., no expenses added yet)

---

## Dependencies

Make sure you have the following installed:

- Python 3.x  
- `matplotlib` library for plotting the expense graph  

You can install matplotlib using:

```
pip install matplotlib
```

---

## How to run the code

1. Save the code in a file, for example:

   ```
   expense_tracker.py
   ```

2. Open a terminal or command prompt in the folder where the file is saved.

3. Run the script with:

   ```
   python expense_tracker.py
   ```

   or, depending on your system:

   ```
   python3 expense_tracker.py
   ```

4. You will see a menu like:

   ```
   Expense Tracker
   1. Add Expense
   2. View Expenses
   3. Show Total Spent
   4. Plot Expenses Graph
   5. Exit
   ```

5. Enter a number from 1 to 5 to choose what you want to do.

---

## Usage instructions

### 1. Add an expense

- Choose option `1` from the menu.  
- Enter the amount when asked (for example: `250.75`).  
- Enter a short description (for example: `Groceries` or `Bus ticket`).  
- The program will confirm: `"Expense added!"`

### 2. View all expenses

- Choose option `2`.  
- If there are expenses, you will see them listed as:

  ```
  1. ₹250.75  -- Groceries
  2. ₹50.00   -- Bus ticket
  ```

- If no expenses have been added yet, it will say: `"No expenses recorded."`

### 3. Show total spent

- Choose option `3`.  
- The program will sum all amounts and print something like:

  ```
  Total spent: ₹300.75
  ```

### 4. Plot expenses graph

- Choose option `4`.  
- If you have added expenses, a matplotlib window will open showing a line graph:
  - X‑axis: Expense descriptions  
  - Y‑axis: Amount in ₹  
- The graph automatically adjusts its width based on how many expenses you have.  
- If there are no expenses, it will print: `"No expenses to plot!"`

### 5. Exit the program

- Choose option `5` to quit.  
- The program will print `"Goodbye!"` and stop running.

---

## Notes and suggestions

- Amounts are stored in memory only; once you close the program, all data is lost.  
- You can extend this project by:
  - Saving expenses to a file (e.g., CSV or JSON)  
  - Adding categories (Food, Transport, etc.)  
  - Adding date and time for each expense  
  - Improving validation (e.g., handling invalid numeric input)  

This simple script is a great starting point for learning Python, working with lists and dictionaries, and using matplotlib for basic data visualization.
```
