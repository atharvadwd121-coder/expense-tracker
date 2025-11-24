# 📊 Personal Expense Tracker

<div align="center">

**A Python-based command-line application for tracking daily expenses with visualization capabilities**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Required-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

## 🎯 Overview

The Personal Expense Tracker is a lightweight, user-friendly Python application designed to help individuals manage their daily spending habits effectively. This tool provides essential financial tracking functionality through an intuitive command-line interface, enabling users to record expenses, analyze spending patterns, and gain valuable insights into their personal finance management.

### Why Use This Expense Tracker?

- **Simplicity First**: No complex setup or databases required - just run and start tracking
- **Visual Insights**: Automatic graph generation to visualize spending patterns over time
- **Session-Based**: Perfect for daily expense tracking without data persistence overhead
- **Lightweight**: Minimal dependencies (only matplotlib) makes it easy to deploy anywhere
- **Educational**: Clean, well-structured code ideal for learning Python programming concepts

---

## ✨ Key Features

### 1. **Expense Recording**
   - Add new expenses with amount and description
   - Instant confirmation feedback
   - Organized data structure for easy retrieval

### 2. **Transaction History**
   - View complete list of all recorded expenses
   - Numbered entries for easy reference
   - Clear display with Indian Rupee (₹) formatting

### 3. **Total Calculation**
   - Automatic summation of all expenses
   - Real-time total tracking
   - Instant financial overview

### 4. **Data Visualization**
   - Dynamic line graph generation
   - Matplotlib-powered plotting
   - Grid-enabled graphs for better readability
   - Expense trend analysis over time
   - Responsive graph sizing based on data volume

### 5. **User-Friendly Interface**
   - Clean, menu-driven navigation
   - Input validation
   - Clear prompts and feedback
   - Easy exit functionality

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your system
- **pip** package manager

### Installation

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/atharvadwd121-coder/expense-tracker.git
   cd expense-tracker
   ```

2. **Install required dependencies**:
   ```bash
   pip install matplotlib
   ```

### Running the Application

```bash
python expense_tracker.py
```

---

## 📖 Usage Guide

Upon launching the application, you'll see an interactive menu with the following options:

### Menu Options

```
Expense Tracker
1. Add Expense
2. View Expenses
3. Show Total Spent
4. Plot Expenses Graph
5. Exit
```

### Detailed Functionality

#### **Option 1: Add Expense**
- Enter the amount spent (numeric value)
- Provide a brief description of the expense
- System confirms successful addition

**Example**:
```
Choose an option (1-5): 1
Enter amount spent: 500
Enter description: Groceries
Expense added!
```

#### **Option 2: View Expenses**
- Displays all recorded expenses in a formatted list
- Shows expense number, amount in ₹, and description
- If no expenses exist, notifies user accordingly

**Example Output**:
```
List of expenses:
1. ₹500 -- Groceries
2. ₹150 -- Transportation
3. ₹300 -- Lunch
```

#### **Option 3: Show Total Spent**
- Calculates and displays cumulative spending
- Provides instant financial summary

**Example Output**:
```
Total spent: ₹950
```

#### **Option 4: Plot Expenses Graph**
- Generates a visual representation of spending patterns
- Opens matplotlib window with interactive graph
- X-axis: Expense sequence number
- Y-axis: Amount in Rupees
- Requires at least one expense entry

**Note**: Close the graph window to return to the main menu

#### **Option 5: Exit**
- Safely exits the application
- All session data is cleared

---

## 🏗️ Project Structure

### Algorithm Design

The application follows a modular top-down design approach:

```
┌─ Main Program
│
├─ Initialization
│  ├─ Import matplotlib.pyplot
│  └─ Initialize global expenses list
│
├─ Main Loop (Menu System)
│  ├─ Display options
│  ├─ Accept user input
│  └─ Route to appropriate function
│
├─ add_expense()
│  ├─ Input: amount (float)
│  ├─ Input: description (string)
│  ├─ Append to expenses list as dictionary
│  └─ Confirmation message
│
├─ view_expenses()
│  ├─ Check if expenses list is empty
│  ├─ Enumerate and display all entries
│  └─ Format with ₹ symbol
│
├─ show_total()
│  ├─ Use list comprehension for summation
│  ├─ Calculate total from 'amount' keys
│  └─ Display formatted result
│
├─ plot_graph()
│  ├─ Validate non-empty expenses list
│  ├─ Extract amounts using list comprehension
│  ├─ Configure matplotlib parameters
│  │  ├─ Title: "Expense Variation"
│  │  ├─ X-label: "Expense Number"
│  │  ├─ Y-label: "Amount (₹)"
│  │  └─ Enable grid
│  └─ Render plot window
│
└─ Exit
   └─ Terminate program
```

### Core Components

1. **Data Structure**: List of dictionaries for expense storage
2. **Input Handling**: Built-in Python functions for user interaction
3. **Calculation Logic**: List comprehension and sum() for aggregation
4. **Visualization**: Matplotlib for graphical representation
5. **Control Flow**: While loop with conditional branching

---

## 🛠️ Technical Implementation

### Technology Stack

- **Language**: Python 3.x
- **Visualization Library**: Matplotlib
- **Architecture**: Procedural programming with functional decomposition

### Key Functions

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `add_expense()` | Record new expense | amount, description | Confirmation message |
| `view_expenses()` | Display all expenses | None | Formatted list |
| `show_total()` | Calculate total spending | None | Total amount |
| `plot_graph()` | Visualize expenses | None | Matplotlib graph |
| `main()` | Application controller | None | Menu loop |

### Data Model

```python
expenses = [
    {'amount': 500.0, 'description': 'Groceries'},
    {'amount': 150.0, 'description': 'Transportation'},
    {'amount': 300.0, 'description': 'Lunch'}
]
```

---

## 📊 Screenshots

Visual examples of the application in action are available in the `screenshots/` directory.

---

## 🎓 Learning Outcomes

This project demonstrates:

- Python fundamentals (functions, loops, conditionals)
- Data structures (lists, dictionaries)
- List comprehensions for efficient data processing
- External library integration (matplotlib)
- User input validation
- Menu-driven interface design
- Data visualization concepts
- Modular code organization

---

## 🔮 Future Enhancements

Potential improvements for future versions:

- [ ] Data persistence using JSON or SQLite
- [ ] Category-based expense classification
- [ ] Date/time stamping for each transaction
- [ ] Budget limit alerts and notifications
- [ ] Multiple graph types (bar, pie charts)
- [ ] Export functionality (CSV, PDF)
- [ ] Multi-user support with profiles
- [ ] Monthly/weekly spending summaries
- [ ] GUI version using Tkinter or PyQt
- [ ] Currency conversion support
- [ ] Expense filtering and search
- [ ] Statistical analysis (averages, trends)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**atharvadwd121-coder**

- GitHub: [@atharvadwd121-coder](https://github.com/atharvadwd121-coder)

---

## 🙏 Acknowledgments

- Built with Python's powerful standard library
- Visualization powered by Matplotlib
- Inspired by the need for simple, effective personal finance tools

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

</div>
