# Lab 4.3: Capstone — build a complete application

**Estimated time**: 90 minutes  
**Difficulty level**: Intermediate  
**Python version**: 3.12+  
**Tools**: VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Plan and structure a multi-file Python project
- Set up a project with uv and `pyproject.toml`
- Combine file I/O, data structures, functions, error handling, and classes in a single application
- Build a menu-driven command-line interface with input validation
- Organise code across multiple files with proper imports

---

## 3. Prerequisites

**Knowledge prerequisites**: All material from Days 1–3, plus list comprehensions (Lab 4.1) and classes (Lab 4.2). Chapter 4.3 presentation completed.

**Previous labs**: Labs 4.1 and 4.2 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] uv installed and on PATH
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Run `uv --version` (expect a version number)
- [ ] Navigate to your working directory: `cd C:\labs`

**Project setup:**

1. Create the project with uv:

```
C:\labs> uv init expense-tracker
C:\labs> cd expense-tracker
```

2. Verify the project structure:

```
C:\labs\expense-tracker> dir
```

You should see `pyproject.toml` and other files created by uv.

3. Verify Python runs inside the project:

```
C:\labs\expense-tracker> uv run python -c "print('Project ready')"
```

---

## 5. Concept overview

This capstone project combines every concept from the course into a single, practical application: a command-line expense tracker. You will add expenses, view them, see a summary by category, and persist data to a CSV file. The code is organised across three files, each with a clear responsibility.

This is not a step-by-step tutorial that dictates every line. The exercises give you the structure and the key pieces, but you will need to connect them yourself. If you get stuck, the hints and the complete solutions in section 15 are there to help — but try first. Struggling with the connections between components is exactly how programming skills develop.

The final application uses: variables and types, strings and f-strings, lists and dictionaries, loops and conditionals, functions, file I/O, error handling, modules and imports, classes, and comprehensions. Every topic from the past four days has a natural place in this project.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Set up a multi-file project structure with uv
- Create a data model class for expenses
- Implement CSV file reading and writing for data persistence
- Build a menu-driven interface with input validation and error handling

---

### Exercise 4.3.1: Create the data model

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Define an `Expense` class that represents a single expense record.

**Scenario**: Every expense has a date, category, amount, and description. You need a class that holds this data and can display it in a neatly formatted row.

**Tasks**:

1. In VS Code, open the `expense-tracker` folder (`File → Open Folder → C:\labs\expense-tracker`).

2. Create a new file. Save it as `expense.py` in the `expense-tracker` folder.

3. Define the `Expense` class with these requirements:
   - `__init__` accepts `date` (string), `category` (string), `amount` (float), and `description` (string)
   - `__str__` returns a formatted string with aligned columns, for example:
     `2024-11-15 | food            |   285.50 CZK | Weekly groceries`
   - Use format specifiers: `:<15` for left-aligned category, `:>8.2f` for right-aligned amount

4. Add a test section at the bottom of the file:

```python
if __name__ == "__main__":
    e1 = Expense("2024-11-15", "food", 285.50, "Weekly groceries")
    e2 = Expense("2024-11-16", "transport", 150.00, "Monthly bus pass")
    e3 = Expense("2024-11-16", "entertainment", 200.00, "Concert tickets")

    for e in [e1, e2, e3]:
        print(e)
```

5. Run the file to test:

```
C:\labs\expense-tracker> uv run python expense.py
```

**Expected output**: Three neatly aligned rows, each showing date, category (left-padded to 15 characters), amount (right-aligned with 2 decimal places and "CZK"), and description.

**Hints**:
- Hint 1: The `__str__` method should return (not print) the formatted string.
- Hint 2: Use `f"{self.category:<15}"` to left-align and `f"{self.amount:>8.2f}"` to right-align.

**Verification**: Each expense prints on one line with consistent column widths. Running the file directly triggers the test code inside `if __name__ == "__main__":`.

---

### Exercise 4.3.2: Implement CSV storage

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Write functions that load expenses from a CSV file and save them back, handling the case where the file does not yet exist.

**Scenario**: The expense tracker needs to persist data between sessions. On startup, it loads existing expenses from `expenses.csv`. On exit, it saves all expenses back. The first time the application runs, there is no file yet — this should not cause an error.

**Tasks**:

1. Create a new file. Save it as `storage.py` in the `expense-tracker` folder.

2. Implement two functions:

   **`load_expenses(filepath)`**:
   - Open the CSV file using `csv.reader`
   - Skip the header row with `next(reader)`
   - For each remaining row, create an `Expense` object (convert the amount to `float`)
   - If the file does not exist (`FileNotFoundError`), return an empty list
   - Return the list of `Expense` objects

   **`save_expenses(filepath, expenses)`**:
   - Open the file for writing using `csv.writer`
   - Write a header row: `["date", "category", "amount", "description"]`
   - Write each expense as a row: `[expense.date, expense.category, expense.amount, expense.description]`

3. Add a test section:

```python
if __name__ == "__main__":
    from expense import Expense

    test_expenses = [
        Expense("2024-11-15", "food", 285.50, "Weekly groceries"),
        Expense("2024-11-16", "transport", 150.00, "Monthly bus pass"),
    ]

    save_expenses("test_expenses.csv", test_expenses)
    print("Saved 2 expenses.")

    loaded = load_expenses("test_expenses.csv")
    print(f"Loaded {len(loaded)} expenses:")
    for e in loaded:
        print(f"  {e}")

    # Test loading a non-existent file
    empty = load_expenses("nonexistent.csv")
    print(f"\nNon-existent file: {len(empty)} expenses (no error)")

    # Clean up test file
    import os
    os.remove("test_expenses.csv")
    print("Test file removed.")
```

4. Run the tests:

```
C:\labs\expense-tracker> uv run python storage.py
```

**Expected output**: Two expenses saved, then loaded back and displayed. The non-existent file returns an empty list without crashing. The test file is cleaned up.

**Hints**:
- Hint 1: Use `import csv` and `from expense import Expense`.
- Hint 2: Wrap the file opening in `try`/`except FileNotFoundError` and return `[]` in the `except` block.
- Hint 3: Use `newline=""` in both `open()` calls to prevent blank lines in the CSV on Windows.

**Verification**: The save-then-load round-trip preserves all data. The non-existent file case is handled gracefully.

---

### Exercise 4.3.3: Build the menu interface

**Time**: 35 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Create the main application loop with a menu, input handling, and expense operations.

**Scenario**: The user interacts with the expense tracker through a numbered menu. They can add expenses, view all expenses, see a category summary, and exit. Invalid input should be handled gracefully — the application should never crash from bad user input.

**Tasks**:

1. Create a new file. Save it as `main.py` in the `expense-tracker` folder.

2. Implement the following functions:

   **`get_menu_choice()`**:
   - Print the menu with options: 1. Add expense, 2. View expenses, 3. View summary, 4. Exit
   - Return the user's input (stripped)

   **`add_expense(expenses)`**:
   - Prompt for date, category, amount, and description
   - Validate the amount: wrap `float(input(...))` in `try`/`except ValueError`
   - If valid, create an `Expense` and append it to the list
   - Print a confirmation or an error message

   **`view_expenses(expenses)`**:
   - If the list is empty, print a message and return
   - Otherwise, print each expense

   **`view_summary(expenses)`**:
   - If the list is empty, print a message and return
   - Build a dictionary of totals per category (use a loop with `dict.get()`)
   - Print each category total, sorted alphabetically
   - Print the grand total

   **`main()`**:
   - Set `DATA_FILE = "expenses.csv"`
   - Load expenses from the file
   - Print how many expenses were loaded
   - Loop: show menu, dispatch to the appropriate function based on choice
   - On exit (choice "4"), save expenses and print a goodbye message
   - Handle invalid menu choices with a message

3. At the bottom of the file, add:

```python
main()
```

4. Run the application:

```
C:\labs\expense-tracker> uv run python main.py
```

5. Test the application manually:
   - Add 2–3 expenses with different categories
   - View all expenses
   - View the summary
   - Try entering an invalid amount (e.g., "abc") — it should show an error, not crash
   - Try entering an invalid menu choice (e.g., "5") — it should show a message
   - Exit and re-run the application — your expenses should still be there

**Expected output**: A menu-driven interaction. Adding expenses prompts for each field. Viewing shows all expenses. Summary groups by category with totals. Invalid input is handled. Data persists between runs in `expenses.csv`.

**Hints**:
- Hint 1: Import `Expense` from `expense` and `load_expenses`, `save_expenses` from `storage`.
- Hint 2: For the summary, initialise an empty dictionary and use `totals[category] = totals.get(category, 0) + amount`.
- Hint 3: Convert the category to lowercase with `.lower()` in `add_expense` to keep categories consistent.

**Verification**: The application does not crash on any input. Data is saved to `expenses.csv` and survives a restart. The summary totals are correct.

---

### Exercise 4.3.4: Polish and extend

**Time**: 20 minutes  
**Difficulty**: Advanced  
**Tool**: VS Code  
**Objective**: Add a filtering feature and improve the user experience.

**Scenario**: The basic tracker works, but users want to filter expenses by category. You also want to add a count display and make the menu more informative.

**Tasks**:

1. Add a new menu option **"5. Filter by category"** to `main.py`.

2. Implement a `filter_by_category(expenses)` function:
   - Show the available categories (use a set comprehension to get unique categories)
   - Prompt for a category name
   - Use a list comprehension to find matching expenses (case-insensitive)
   - Display the matching expenses and their total

3. Update the menu display to show the current expense count:

```python
def get_menu_choice(expense_count):
    print(f"\n=== Expense tracker ({expense_count} expenses) ===\n")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Filter by category")
    print("5. Exit")
    return input("\nChoose an option: ").strip()
```

4. Update the `main()` loop to pass the count and handle the new option.

5. Run and test the updated application:

```
C:\labs\expense-tracker> uv run python main.py
```

**Expected output**: The menu shows the current expense count. Option 4 lists available categories, prompts for one, and shows only matching expenses with a total. Option 5 exits and saves.

**Verification**: Filtering finds the correct expenses regardless of case. The count in the menu header updates after adding expenses.

**Try it yourself**:
- Add date validation: check that the date matches `YYYY-MM-DD` format using `datetime.strptime()`.
- Add an option to delete an expense by its number in the list.
- Add an option to export the summary to a text file.

---

## 7. Validation checklist

- [ ] Exercise 4.3.1: `expense.py` defines the `Expense` class and prints three aligned rows when run
- [ ] Exercise 4.3.2: `storage.py` saves and loads expenses to/from CSV, handles missing files
- [ ] Exercise 4.3.3: `main.py` provides a menu-driven interface with add, view, summary, and exit
- [ ] Exercise 4.3.4: Filtering by category works, menu shows expense count
- [ ] Data persists: exiting and restarting the application preserves expenses

```
C:\labs\expense-tracker> uv run python expense.py
# Three aligned expense rows

C:\labs\expense-tracker> uv run python storage.py
# Save, load, and non-existent file test

C:\labs\expense-tracker> uv run python main.py
# Interactive menu — add, view, summary, filter, exit
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'expense'` | Running from the wrong directory or wrong command | Run from `C:\labs\expense-tracker` with `uv run python main.py` |
| `ImportError: cannot import name 'Expense'` | Typo in class name or file name | Verify `expense.py` defines `class Expense` |
| `FileNotFoundError` | CSV file path is wrong | Check that `expenses.csv` is in the same directory as `main.py` |
| `ValueError: could not convert string to float` | User entered non-numeric amount | Wrap `float(input(...))` in `try`/`except ValueError` |
| `AttributeError: 'Expense' object has no attribute 'X'` | Typo in attribute name | Check `__init__` for `self.X = ...` |

**Common beginner pitfalls:**
- Importing from `expense` while running from the wrong directory — Python cannot find the module
- Forgetting `newline=""` in `open()` calls — CSV files get blank lines between rows on Windows
- Using `csv.DictReader` in `storage.py` when the solution uses `csv.reader` (or vice versa) — both work, but be consistent
- Not converting the amount back to `float` when loading from CSV — everything read from CSV is a string

**Environment issues:**
- `uv` not recognised → Check uv installation and PATH
- `python` not recognised → Use `uv run python` instead
- Module import errors → Verify you are in the `expense-tracker` directory

---

## 9. Questions

1. The expense tracker stores data in a CSV file. What would change if you needed to store additional fields (like "payment method" or "tags")? How does separating storage logic into `storage.py` help with this kind of change?

2. The `main()` function uses a `while True` loop with `if`/`elif` branches for menu dispatch. An alternative approach uses a dictionary mapping choices to functions: `actions = {"1": add_expense, "2": view_expenses, ...}`. Compare the two approaches and discuss when each is preferable.

3. The `Expense` class stores `amount` as a `float`. Financial applications typically use `decimal.Decimal` instead. What problems could `float` cause with money calculations, and how would switching to `Decimal` affect the rest of the code?

4. Currently, the application validates that the amount is a number but does not validate the date format. Describe how you would add date validation using `datetime.strptime()`. Where in the code should this validation live — in `add_expense()`, in `Expense.__init__()`, or in a separate validation function?

5. The application saves data only when the user exits. What happens if the program crashes or the user closes the terminal? Propose two different strategies for preventing data loss, and discuss the trade-offs of each.

6. You split the code across three files: `expense.py`, `storage.py`, and `main.py`. A colleague suggests putting everything in one file since the application is small. Present arguments for and against splitting, considering the current size and potential future growth.

---

## 10. Clean-up

Remove the project directory:

```
C:\labs\expense-tracker> cd ..
C:\labs> rmdir /s /q expense-tracker
```

Verify the directory is removed:

```
C:\labs> dir expense-tracker
```

**Note**: Do NOT uninstall Python, uv, or VS Code.

---

## 11. Key takeaways

- A real application combines many individual concepts: data types, functions, file I/O, error handling, modules, classes, and comprehensions
- Planning the project structure before writing code produces cleaner results
- Separating concerns — data model (`expense.py`), storage (`storage.py`), interface (`main.py`) — makes code easier to understand, test, and modify
- The menu-loop pattern (show options → get input → dispatch → repeat) is a standard approach for command-line applications
- Error handling at input boundaries (user input, file operations) prevents crashes
- `uv init` and `pyproject.toml` establish a proper project from the start
- Every topic from this course has a natural place in a real project

---

## 12. Additional resources

- Python Tutorial — Modules: https://docs.python.org/3/tutorial/modules.html
- Python csv module documentation: https://docs.python.org/3/library/csv.html
- Python decimal module documentation: https://docs.python.org/3/library/decimal.html
- uv documentation: https://docs.astral.sh/uv/
- Real Python — Working with CSV Files in Python: https://realpython.com/python-csv/

---

## 13. Appendices

### Appendix A: Quick reference — project structure pattern

```
my-project/
    pyproject.toml       # Project metadata (created by uv init)
    main.py              # Entry point — menu loop, user interaction
    model.py             # Classes that represent your data
    storage.py           # Functions that read/write data to files
    data.csv             # Data file (created at runtime)
```

### Appendix B: Key patterns used in this project

```python
# Menu loop pattern
def main():
    data = load_data(filepath)
    while True:
        choice = get_menu_choice()
        if choice == "1":
            do_action(data)
        elif choice == "quit":
            save_data(filepath, data)
            break

# Safe input pattern
try:
    value = float(input("Amount: "))
except ValueError:
    print("Invalid number.")

# Dictionary accumulation pattern
totals = {}
for item in items:
    key = item.category
    totals[key] = totals.get(key, 0) + item.amount
```

### Appendix C: Environment information

- Python: `python --version`
- uv: `uv --version`
- Create project: `uv init project-name`
- Run scripts: `uv run python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

Adding a new field like "payment method" requires changes in three places: (1) add the attribute to the `Expense` class and update `__str__`, (2) update `storage.py` to read/write the new column in the CSV, and (3) update `add_expense()` to prompt for the new field.

Because storage is isolated in `storage.py`, you can change the file format (add a column, switch to JSON, use a database) without touching the menu logic in `main.py`. Similarly, adding a new field to `Expense` does not require understanding how the file I/O works. Each file has a single responsibility, so changes are localised. Without this separation, adding a field would mean editing a single large file and hoping you found every relevant section.

**Answer 2:**

The `if`/`elif` approach is explicit and straightforward. Every branch is visible, and the logic is easy to trace. For 4–5 options, it is perfectly readable.

The dictionary approach — `actions = {"1": add_expense, "2": view_expenses}` followed by `actions.get(choice, invalid_choice)()` — eliminates repetitive `if`/`elif` checks and makes adding new options a one-line change (add a key-value pair). It also treats functions as first-class objects, which is a powerful Python pattern.

The trade-off: the dictionary approach requires that all action functions have the same signature (or use wrappers), which can be awkward when some functions need different arguments. For small menus, `if`/`elif` is clearer. For large menus or dynamic option sets, the dictionary approach scales better.

**Answer 3:**

Floating-point numbers cannot represent all decimal fractions exactly. `0.1 + 0.2` equals `0.30000000000000004`, not `0.3`. For an expense tracker, this can cause totals to display with unexpected extra digits (e.g., `$10.30` becomes `$10.300000000000001`). Using `:.2f` formatting hides this in display, but internal calculations can accumulate rounding errors over hundreds of operations.

`decimal.Decimal` represents decimal fractions exactly: `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")`. Switching requires changing how amounts are created (use `Decimal(string)` instead of `float(string)`), updating format strings, and ensuring no accidental conversion to float. The rest of the code — comparisons, summing, sorting — works the same because `Decimal` supports the same arithmetic operators. For a learning project, `float` is fine. For production financial software, `Decimal` is essential.

**Answer 4:**

Date validation using `datetime.strptime()`:

```python
from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
```

The best place depends on your design goals. In `add_expense()`, validation is close to the user input — simple and direct. In `Expense.__init__()`, it guarantees that no `Expense` object can exist with an invalid date, which is safer but raises an exception that callers must handle. In a separate `validators.py` module, it is reusable across different contexts.

For this project, validating in `add_expense()` is the most practical: you can re-prompt the user immediately. Validation in `__init__` is better for larger systems where expenses might be created from multiple sources (user input, file import, API) and you want consistent enforcement.

**Answer 5:**

Strategy 1: **Save after every modification.** Call `save_expenses()` after each `add_expense()` call, not just on exit. This ensures data is always current on disk. The trade-off: more frequent disk writes, which is slower — but for a small CSV file, the overhead is negligible.

Strategy 2: **Auto-save on a timer or after N changes.** Save periodically (e.g., every 60 seconds) or after every 5 changes. This balances data safety with performance. The trade-off: more complex to implement (requires threading or counting changes), and you can still lose up to N changes or 60 seconds of data.

For this application, saving after every modification is the simplest and most reliable approach. Disk I/O for a small CSV is fast, and the simplicity outweighs any performance concern. The current exit-only approach is the riskiest — a crash loses all work from the session.

**Answer 6:**

For the current size (roughly 100–150 lines of application code), a single file is manageable. You can scroll through it, search for functions, and understand the whole application. The argument for one file: less complexity, no import issues, no need to coordinate between files.

The argument for splitting: each file has a clear purpose. `expense.py` is the data model — you can read it in isolation to understand what an expense is. `storage.py` handles persistence — you can swap CSV for JSON by changing one file. `main.py` is the user interface — you can redesign the menu without touching data logic. As the project grows (adding reports, charts, web interface, tests), this separation becomes essential. Starting with good structure is easier than refactoring later.

For a learning project, splitting demonstrates professional practice and prepares students for real-world codebases where single-file applications simply do not exist.

---

## 15. Code solutions

### Exercise 4.3.1: expense.py

```python
# expense.py - Expense data model


class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (
            f"{self.date} | {self.category:<15} | "
            f"{self.amount:>8.2f} CZK | {self.description}"
        )


if __name__ == "__main__":
    e1 = Expense("2024-11-15", "food", 285.50, "Weekly groceries")
    e2 = Expense("2024-11-16", "transport", 150.00, "Monthly bus pass")
    e3 = Expense("2024-11-16", "entertainment", 200.00, "Concert tickets")

    for e in [e1, e2, e3]:
        print(e)
```

### Exercise 4.3.2: storage.py

```python
# storage.py - Load and save expenses to CSV

import csv
from expense import Expense


def load_expenses(filepath):
    """Load expenses from a CSV file. Return empty list if file not found."""
    expenses = []
    try:
        with open(filepath, newline="") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                date, category, amount, description = row
                expenses.append(
                    Expense(date, category, float(amount), description)
                )
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(filepath, expenses):
    """Save expenses to a CSV file."""
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount", "description"])
        for e in expenses:
            writer.writerow([e.date, e.category, e.amount, e.description])


if __name__ == "__main__":
    test_expenses = [
        Expense("2024-11-15", "food", 285.50, "Weekly groceries"),
        Expense("2024-11-16", "transport", 150.00, "Monthly bus pass"),
    ]

    save_expenses("test_expenses.csv", test_expenses)
    print("Saved 2 expenses.")

    loaded = load_expenses("test_expenses.csv")
    print(f"Loaded {len(loaded)} expenses:")
    for e in loaded:
        print(f"  {e}")

    empty = load_expenses("nonexistent.csv")
    print(f"\nNon-existent file: {len(empty)} expenses (no error)")

    import os
    os.remove("test_expenses.csv")
    print("Test file removed.")
```

### Exercise 4.3.3: main.py (basic version)

```python
# main.py - Expense tracker application

from expense import Expense
from storage import load_expenses, save_expenses

DATA_FILE = "expenses.csv"


def get_menu_choice():
    print("\n=== Expense tracker ===\n")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Exit")
    return input("\nChoose an option: ").strip()


def add_expense(expenses):
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip().lower()
    amount_input = input("Amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print(f"Invalid amount: '{amount_input}'. Expense not added.")
        return
    description = input("Description: ").strip()

    expense = Expense(date, category, amount, description)
    expenses.append(expense)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"  {expense}")


def view_summary(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    totals = {}
    for expense in expenses:
        cat = expense.category
        totals[cat] = totals.get(cat, 0) + expense.amount

    print("\nCategory summary:")
    for category, total in sorted(totals.items()):
        print(f"  {category}: {total:.2f} CZK")
    print(f"Total: {sum(totals.values()):.2f} CZK")


def main():
    expenses = load_expenses(DATA_FILE)
    print(f"Loaded {len(expenses)} expense(s) from {DATA_FILE}.")

    while True:
        choice = get_menu_choice()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            save_expenses(DATA_FILE, expenses)
            print("Data saved. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


main()
```

### Exercise 4.3.4: main.py (extended version with filtering)

```python
# main.py - Expense tracker application (extended)

from expense import Expense
from storage import load_expenses, save_expenses

DATA_FILE = "expenses.csv"


def get_menu_choice(expense_count):
    print(f"\n=== Expense tracker ({expense_count} expenses) ===\n")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Filter by category")
    print("5. Exit")
    return input("\nChoose an option: ").strip()


def add_expense(expenses):
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip().lower()
    amount_input = input("Amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print(f"Invalid amount: '{amount_input}'. Expense not added.")
        return
    description = input("Description: ").strip()

    expense = Expense(date, category, amount, description)
    expenses.append(expense)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"  {expense}")


def view_summary(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    totals = {}
    for expense in expenses:
        cat = expense.category
        totals[cat] = totals.get(cat, 0) + expense.amount

    print("\nCategory summary:")
    for category, total in sorted(totals.items()):
        print(f"  {category}: {total:.2f} CZK")
    print(f"Total: {sum(totals.values()):.2f} CZK")


def filter_by_category(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    categories = sorted({e.category for e in expenses})
    print(f"Available categories: {', '.join(categories)}")

    query = input("Enter category: ").strip().lower()
    filtered = [e for e in expenses if e.category == query]

    if not filtered:
        print(f"No expenses found in category '{query}'.")
        return

    print(f"\nExpenses in '{query}':")
    for e in filtered:
        print(f"  {e}")
    total = sum(e.amount for e in filtered)
    print(f"Category total: {total:.2f} CZK")


def main():
    expenses = load_expenses(DATA_FILE)
    print(f"Loaded {len(expenses)} expense(s) from {DATA_FILE}.")

    while True:
        choice = get_menu_choice(len(expenses))

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            save_expenses(DATA_FILE, expenses)
            print("Data saved. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


main()
```
