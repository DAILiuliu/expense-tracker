# Expense Tracker

A simple command-line expense tracker written in Python.
I built this while learning Python with Stanford's Code in Place.

## Features

- Record daily expenses by category (food, transport, fun, daily, study, phone, housing)
- Warn when you type a category that doesn't exist
- Show the total for each category at the end
- Show total spending and check it against a monthly budget

## How to run

```
python expense_tracker.py
```

Type a category and an amount for each expense. Type `done` when you are finished.

## What I learned

- **Version 1**: Used 7 separate variables and 7 `if/elif` branches, about 40 lines.
- **Version 2**: Replaced them with a dictionary. One line, `totals[category] += money`, does the job of all 7 branches, and the program is now about 16 lines.

## Next steps

- [x] Show total spending and check it against a monthly budget of 300,000 yen
- [ ] Handle non-number input for the amount
- [ ] Save records to a file
