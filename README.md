# Personal Expense Tracker.

## Project Summary.

This Python program is pretty straightforward. It helps people keep tabs on their daily spending. Users can input details about what they bought. They can check back on past transactions too. The program adds up the total spent so far. It even draws a basic graph with Matplotlib to show spending patterns over time.

## Key Features.

- •  
  You can add new expenses by typing in the amount and a short note about it. That keeps everything organized right from the start.
- •  
  Viewing the history brings up a full list of all transactions recorded. It makes it easy to see what happened when.
- •  
  Calculating the total gives an instant sum of everything entered up to now.
- •  
  For data visualization, the program creates a line graph to analyze spending trends.
- •  
  The graphs adjust their width on their own based on how many entries there are. That way, they stay clear and not too crowded no matter what.

## Dependencies.

You will need Python 3.x set up on your computer to run this project. The only extra library required is for making those graphs. It is **matplotlib**.

## Installation and Setup.

1. First, save the Python code into a file named `expense_tracker.py`. You can pick another name if that works better for you.

2. Next, open up your terminal or command prompt. Run this command to get matplotlib installed.
   ```
   pip install matplotlib
   ```

## Running the Code.

1. Start by opening your terminal or command prompt.
2. Navigate to the folder where you put the saved file.
3. Then launch the script with Python.
   ```
   python expense_tracker.py
   ```

## Instructions for Usage.

When you run the code, a menu pops up with several choices listed out.

- •
  For adding an expense, pick option 1. Type in the amount, say something like 500 for the cost. Follow that with a description, maybe Lunch or whatever it was.

- •
  Viewing expenses is option 2. It displays every expense added during this session in a list.

- •
  Option 3 shows the total spent. The program figures it out and puts the number right there on screen.

- •
  Picking option 4 plots the expenses graph. A window opens up showing a line graph of your spending. Remember to add at least one expense first, or it will not work.

- •
  Option 5 lets you exit. That closes the whole application down.

## Top down design for the algorithm of this code -

```
[ Main Program ]

    [ Initialization ] (Imports, Global List)

    [ Main Loop ]

        [ Add Expense ]
            Input Float
            Append Dict

        [ View Expenses ]
            Check Empty
            Loop & Print

        [ Show Total ]
            Sum Algorithm

        [ Plot Graph ]
            List Comprehension
            Matplotlib Config

        [ Exit ]
```
