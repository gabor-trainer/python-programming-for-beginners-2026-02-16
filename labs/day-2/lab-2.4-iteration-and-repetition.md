# Lab 2.4: Iteration and repetition

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Use `for` loops to iterate over lists, strings, and `range()` sequences
- Use `while` loops for repetition that depends on a condition
- Apply `break` and `continue` to control loop flow
- Write nested loops for multi-dimensional patterns
- Choose between `for` and `while` based on the problem

---

## 3. Prerequisites

**Knowledge prerequisites**: Lists, tuples, dictionaries, conditional statements, `input()`, and f-strings (Chapters 1.1–2.3).

**Previous labs**: Lab 2.3 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Navigate to your working directory: `cd C:\labs`
- [ ] Verify the REPL works: `python` → `>>> print("Ready")` → `exit()`

No additional setup is required for this lab.

---

## 5. Concept overview

Many tasks in programming involve repetition. Printing every item in a report, checking each file in a folder, retrying a network request until it succeeds, processing every row in a dataset — all of these require loops. Without loops, you would have to copy-paste the same code hundreds of times and still could not handle data of unknown length.

Python offers two loop constructs. A **`for` loop** iterates over a sequence (list, string, range) — you know how many times the loop will run. A **`while` loop** repeats as long as a condition is true — the number of iterations depends on runtime behaviour (user input, random events, convergence).

In this lab, you will process lists of data with `for` loops, build a number-guessing game with `while`, use nested loops to print patterns, and search through a list of dictionaries. You will also practise `break` (exit the loop early) and `continue` (skip to the next iteration).

---

## 6. Exercises

**Problems you will solve in this lab:**
- Process and summarise a dataset using `for` loops and `range()`
- Build an interactive number-guessing game with `while` and `break`
- Print geometric patterns using nested loops
- Search and filter a list of dictionaries with loops and conditions

---

### Exercise 2.4.1: Process data with for loops

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Iterate over lists and ranges to process, filter, and summarise data.

**Scenario**: A shop has a list of daily sales figures for a month. You need to calculate totals, find extremes, count specific conditions, and display a formatted report.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `sales_report.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# sales_report.py - Process daily sales data with for loops

daily_sales = [
    120, 85, 200, 150, 90, 310, 175,
    95, 130, 280, 160, 110, 205, 145,
    88, 320, 190, 135, 250, 170, 105,
    275, 140, 195, 300, 180, 115, 230,
    165, 290,
]

print("=== Monthly sales report ===\n")

# Basic statistics
total = sum(daily_sales)
average = total / len(daily_sales)
highest = max(daily_sales)
lowest = min(daily_sales)

print(f"  Days recorded: {len(daily_sales)}")
print(f"  Total sales:   ${total:,}")
print(f"  Average:       ${average:,.2f}")
print(f"  Highest day:   ${highest}")
print(f"  Lowest day:    ${lowest}")

# Count days above and below average
above_average = 0
below_100 = 0

for sale in daily_sales:
    if sale > average:
        above_average += 1
    if sale < 100:
        below_100 += 1

print(f"\n  Days above average: {above_average}")
print(f"  Days below $100:   {below_100}")

# Weekly breakdown using range with step
print("\n--- Weekly breakdown ---\n")
week = 1

for start in range(0, len(daily_sales), 7):
    week_data = daily_sales[start:start + 7]
    week_total = sum(week_data)
    week_avg = week_total / len(week_data)
    print(f"  Week {week}: {week_data}")
    print(f"         Total: ${week_total:,}  Avg: ${week_avg:,.2f}")
    week += 1

# Top 5 days
print("\n--- Top 5 sales days ---\n")
sorted_with_day = sorted(enumerate(daily_sales, start=1), key=lambda x: x[1], reverse=True)

for rank, (day, amount) in enumerate(sorted_with_day[:5], start=1):
    print(f"  {rank}. Day {day:>2}: ${amount}")
```

3. Save and run with F5.

4. Study the key patterns:
   - `for sale in daily_sales:` iterates over each value
   - `range(0, len(daily_sales), 7)` generates starting indices for each week (0, 7, 14, 21, 28)
   - `enumerate(daily_sales, start=1)` pairs each value with its day number

**Verification**: The report shows correct totals, averages, and counts. The weekly breakdown shows 4 full weeks and one partial week. The top 5 days are the five highest values in descending order.

**Expected output**: Multiple sections. The total should be the sum of all 30 values. Weekly totals should add up to the overall total. The top 5 list should start with the highest value.

**Try it yourself**:
- Add a section that shows which days had sales below $100 (print the day number and amount)
- Calculate the percentage of days that were above average
- Add a simple bar chart: for each day, print `#` characters proportional to the sales amount (e.g., one `#` per $50)

---

### Exercise 2.4.2: Number-guessing game with while

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use a `while` loop for indefinite repetition, with `break` to exit when a condition is met.

**Scenario**: You are building a simple game. The computer picks a random number, and the player guesses until they get it right. The game gives hints ("too high" / "too low") after each guess.

**Tasks**:

1. In VS Code, create a new file. Save it as `guessing_game.py` in `C:\labs`.

2. Type the following code:

```python
# guessing_game.py - Number guessing game

import random

secret = random.randint(1, 50)
max_guesses = 7
attempts = 0

print("=== Number guessing game ===")
print(f"\nI'm thinking of a number between 1 and 50.")
print(f"You have {max_guesses} guesses.\n")

while attempts < max_guesses:
    guess_str = input(f"Guess {attempts + 1}/{max_guesses}: ").strip()

    # Validate input
    if not guess_str.isdigit():
        print("  Please enter a whole number.\n")
        continue

    guess = int(guess_str)
    attempts += 1

    if guess == secret:
        print(f"\n  Correct! The number was {secret}.")
        print(f"  You got it in {attempts} guess(es)!")
        break
    elif guess < secret:
        print("  Too low!")
    else:
        print("  Too high!")

    remaining = max_guesses - attempts
    if remaining > 0:
        print(f"  ({remaining} guess(es) remaining)\n")
else:
    # This block runs if the while condition becomes False (no break)
    print(f"\n  Out of guesses! The number was {secret}.")

print("\nThanks for playing!")
```

3. Save and run with F5. Play the game a few times. Notice:
   - `continue` skips the rest of the loop body when input is invalid (no attempt is counted)
   - `break` exits the loop immediately when the guess is correct
   - The `else` clause on the `while` loop runs only if the loop exits normally (not via `break`)

4. Run the game from the command line too:

```
C:\labs> python guessing_game.py
```

**Verification**: The game accepts guesses, gives "too high" / "too low" hints, counts attempts correctly, and ends either on a correct guess or after exhausting all guesses. Invalid input (non-numeric) does not count as an attempt.

**Expected output**: A series of prompts showing the guess number, hints, and remaining guesses. The game ends with either a success or failure message.

**Hints**:
- `random.randint(1, 50)` includes both 1 and 50 as possible values
- The `while/else` pattern is unique to Python — the `else` block runs only when the loop condition becomes `False`, not when `break` exits the loop

**Try it yourself**:
- Add difficulty levels: easy (1–20, 10 guesses), medium (1–50, 7 guesses), hard (1–100, 5 guesses)
- Track the closest guess and display it if the player loses
- Add a "play again?" prompt after each round using an outer `while` loop

---

### Exercise 2.4.3: Patterns with nested loops

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use nested `for` loops to print geometric patterns.

**Scenario**: Nested loops appear whenever you work with two-dimensional data: tables, grids, matrices, or even generating formatted output. Pattern printing is a clear way to understand how an inner loop runs completely for each iteration of the outer loop.

**Tasks**:

1. In VS Code, create a new file. Save it as `patterns.py` in `C:\labs`.

2. Type the following code:

```python
# patterns.py - Geometric patterns with nested loops

size = 5

# Pattern 1: Right triangle
print("--- Right triangle ---")
for row in range(1, size + 1):
    print("* " * row)

print()

# Pattern 2: Inverted right triangle
print("--- Inverted right triangle ---")
for row in range(size, 0, -1):
    print("* " * row)

print()

# Pattern 3: Centered pyramid
print("--- Centered pyramid ---")
for row in range(1, size + 1):
    spaces = " " * (size - row)
    stars = "* " * row
    print(spaces + stars)

print()

# Pattern 4: Number triangle
print("--- Number triangle ---")
for row in range(1, size + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

print()

# Pattern 5: Multiplication table
print("--- Multiplication table (1-5) ---")
print(f"{'':>4}", end="")
for col in range(1, size + 1):
    print(f"{col:>4}", end="")
print()
print("    " + "----" * size)

for row in range(1, size + 1):
    print(f"{row:>3} |", end="")
    for col in range(1, size + 1):
        print(f"{row * col:>4}", end="")
    print()
```

3. Save and run with F5.

4. Study how nested loops work:
   - In Pattern 4, the outer loop controls the row (1 to 5). For each row, the inner loop prints numbers 1 through `row`.
   - In Pattern 5, the outer loop iterates rows, the inner loop iterates columns. Each cell prints `row * col`.
   - `end=""` prevents `print()` from starting a new line, so all values in a row appear on the same line. The bare `print()` at the end of each row starts a new line.

**Verification**: Each pattern appears correctly. The right triangle has 1 star in the first row and 5 in the last. The centered pyramid is symmetrical. The multiplication table shows correct products.

**Expected output**: Five distinct patterns. The multiplication table shows a 5×5 grid with headers and correct products at each cell.

**Try it yourself**:
- Change `size` to 8 and observe how all patterns scale
- Create a diamond pattern (pyramid + inverted pyramid combined)
- Create a pattern that prints letters instead of numbers (A, B, C, ...) using `chr(64 + col)`

---

### Exercise 2.4.4: Search through a list of dictionaries

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Combine loops, conditions, `break`, and `continue` to search and filter structured data.

**Scenario**: You have a product inventory stored as a list of dictionaries. You need to search for specific products, filter by criteria, and generate a summary.

**Tasks**:

1. In VS Code, create a new file. Save it as `inventory_search.py` in `C:\labs`.

2. Type the following code:

```python
# inventory_search.py - Search and filter product inventory

products = [
    {"name": "Laptop", "category": "electronics", "price": 999.99, "in_stock": True},
    {"name": "Headphones", "category": "electronics", "price": 79.99, "in_stock": True},
    {"name": "Desk Chair", "category": "furniture", "price": 249.99, "in_stock": False},
    {"name": "Python Book", "category": "books", "price": 39.99, "in_stock": True},
    {"name": "Monitor", "category": "electronics", "price": 449.99, "in_stock": True},
    {"name": "Bookshelf", "category": "furniture", "price": 129.99, "in_stock": True},
    {"name": "Keyboard", "category": "electronics", "price": 59.99, "in_stock": False},
    {"name": "Notebook", "category": "books", "price": 12.99, "in_stock": True},
    {"name": "Standing Desk", "category": "furniture", "price": 599.99, "in_stock": True},
    {"name": "USB Cable", "category": "electronics", "price": 9.99, "in_stock": True},
]

# 1. Find a specific product by name (use break to stop searching)
print("=== Product search ===\n")
search_name = "Monitor"
found = None

for product in products:
    if product["name"].lower() == search_name.lower():
        found = product
        break

if found:
    status = "In stock" if found["in_stock"] else "Out of stock"
    print(f"  Found: {found['name']} - ${found['price']:.2f} ({status})")
else:
    print(f"  '{search_name}' not found.")

# 2. Filter by category
print("\n--- Electronics ---\n")
for product in products:
    if product["category"] != "electronics":
        continue
    status = "✓" if product["in_stock"] else "✗"
    print(f"  [{status}] {product['name']:<15} ${product['price']:>8.2f}")

# 3. Filter by price range
print("\n--- Products under $100 (in stock) ---\n")
budget_items = []

for product in products:
    if product["price"] >= 100 or not product["in_stock"]:
        continue
    budget_items.append(product)

for item in sorted(budget_items, key=lambda p: p["price"]):
    print(f"  {item['name']:<15} ${item['price']:>7.2f}")

print(f"\n  Found {len(budget_items)} item(s)")

# 4. Category summary
print("\n--- Category summary ---\n")
categories = {}

for product in products:
    cat = product["category"]
    if cat not in categories:
        categories[cat] = {"count": 0, "total_value": 0, "in_stock": 0}
    categories[cat]["count"] += 1
    categories[cat]["total_value"] += product["price"]
    if product["in_stock"]:
        categories[cat]["in_stock"] += 1

for cat, data in sorted(categories.items()):
    print(f"  {cat.capitalize():<15} {data['count']} products, "
          f"${data['total_value']:>8.2f} total, "
          f"{data['in_stock']} in stock")
```

3. Save and run with F5.

4. Study the patterns:
   - **Search with `break`**: Once the target product is found, `break` stops the loop immediately — no need to check remaining products.
   - **Filter with `continue`**: Products that do not match the criteria are skipped. Only matching products are processed.
   - **Accumulate**: The category summary builds a dictionary of statistics by looping through all products once.

**Verification**: The search finds "Monitor" with the correct price. The electronics filter shows 5 products with stock indicators. The budget filter shows only in-stock items under $100, sorted by price. The category summary shows correct counts and totals.

**Expected output**: Four sections. The search result shows one product. The electronics list shows 5 items. The budget list shows items under $100 that are in stock. The summary shows three categories with aggregated data.

**Try it yourself**:
- Add an interactive search: use `input()` to let the user type a product name to search for
- Add a "most expensive product" section using a loop (without `max()`)
- Add a filter for products that are out of stock and display them as a "reorder list"

---

## 7. Validation checklist

- [ ] `sales_report.py` displays correct totals, averages, weekly breakdowns, and top 5 days
- [ ] `guessing_game.py` gives correct hints, counts attempts properly, and handles invalid input
- [ ] `patterns.py` prints all five patterns correctly, including the multiplication table
- [ ] `inventory_search.py` finds products by name, filters by category and price, and shows correct category summaries
- [ ] You understand when to use `for` (known iteration count) versus `while` (condition-based)
- [ ] You can use `break` to exit a loop early and `continue` to skip an iteration

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| Program hangs (infinite loop) | `while` condition never becomes `False` | Press `Ctrl+C` to stop. Check that the loop variable changes toward the exit condition. |
| `IndentationError` in nested loop | Inner loop body not indented enough | Inner loop body needs 8 spaces (two levels of indentation) |
| Pattern prints on one line | Missing `print()` at end of inner loop | Add a bare `print()` after the inner loop to start a new line |
| Off-by-one in `range()` | `range(5)` gives 0-4, not 1-5 | Use `range(1, 6)` for 1 through 5 |
| `continue` seems to break the loop | Confusing `continue` with `break` | `continue` skips to the next iteration; `break` exits entirely |

**Common beginner pitfalls:**
- Writing `for i in range(len(my_list)):` when `for item in my_list:` or `for i, item in enumerate(my_list):` is cleaner and more Pythonic.
- Modifying a list while iterating over it. This causes skipped items or unexpected behaviour. Iterate over a copy or build a new list instead.
- Forgetting that `range(a, b)` excludes `b`. `range(1, 5)` gives `1, 2, 3, 4`.
- Using `break` inside a nested loop: `break` only exits the innermost loop, not all loops.

---

## 9. Questions

1. You need to process each item in a list and you know the list has exactly 100 items. You could use `for item in my_list:` or `while index < 100:`. Which approach is more appropriate and why? Under what circumstances would the `while` version be better?

2. In the guessing game, we used `while/else` — the `else` block runs only if the loop exits normally (not via `break`). Explain how this feature simplifies the game's logic. How would you implement the same behaviour without using `while/else`?

3. The `continue` statement in Exercise 2.4.4 skips non-matching products. A colleague suggests replacing `continue` with an `if` block that wraps the processing code. Compare the two approaches in terms of readability when there are many skip conditions.

4. Nested loops for the multiplication table run $n \times n$ iterations (25 for a 5×5 table). If you increased the size to 1000×1000, how many iterations would run? What does this tell you about the cost of nested loops and when you should be cautious about nesting depth?

5. You are iterating over a list of 500 records looking for one specific item. Once found, you print it and move on. Explain why using `break` after finding the item is important. What happens without `break`, and is the result incorrect or merely inefficient?

6. A program uses `for i in range(len(my_list)):` to iterate with an index. An experienced Python developer rewrites it as `for i, item in enumerate(my_list):`. What advantages does the `enumerate()` version provide? Are there situations where using `range(len(...))` is still appropriate?

7. Consider a loop that reads lines from a very large file until it finds a line starting with "END". Would you use a `for` loop or a `while` loop? What if the file has 10 million lines — does your answer change?

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\sales_report.py`
- `C:\labs\guessing_game.py`
- `C:\labs\patterns.py`
- `C:\labs\inventory_search.py`

These files demonstrate core loop patterns that appear in nearly every Python program.

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- `for` loops iterate over sequences: `for item in my_list:`, `for i in range(n):`
- `range(start, stop, step)` generates a sequence of integers (stop is excluded)
- `while` loops repeat as long as a condition is `True` — use when iteration count is unknown
- `break` exits the loop immediately; `continue` skips to the next iteration
- `while/else`: the `else` block runs only if the loop completes without `break`
- Nested loops: the inner loop runs completely for each iteration of the outer loop
- Use `for` when iterating over known data; use `while` for condition-driven repetition
- Avoid modifying a list while iterating over it — build a new list or iterate over a copy
- `enumerate()` is the Pythonic way to get both index and value in a `for` loop

---

## 12. Additional resources

- Python `for` statements: https://docs.python.org/3/tutorial/controlflow.html#for-statements
- `range()` function: https://docs.python.org/3/library/functions.html#func-range
- `break`, `continue`, and `else` on loops: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
- Looping techniques: https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
- PEP 8 — Style guide for Python code: https://peps.python.org/pep-0008/

---

## 13. Appendices

### Appendix A: Quick reference — for loop patterns

```python
# Iterate over a list
for item in my_list:
    process(item)

# Iterate with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# Iterate over a range of numbers
for i in range(10):        # 0 to 9
    print(i)

for i in range(1, 11):     # 1 to 10
    print(i)

for i in range(0, 20, 5):  # 0, 5, 10, 15
    print(i)

# Iterate over dictionary items
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Iterate over a string
for char in "hello":
    print(char)
```

### Appendix B: Quick reference — while loop patterns

```python
# Basic while loop
count = 0
while count < 10:
    print(count)
    count += 1

# Input loop (repeat until valid)
while True:
    answer = input("Enter yes or no: ")
    if answer in ("yes", "no"):
        break
    print("Invalid input, try again.")

# while/else
while condition:
    if found:
        break
else:
    print("Loop completed without break")
```

### Appendix C: Quick reference — break and continue

| Statement | Effect | Use case |
|-----------|--------|----------|
| `break` | Exit the loop immediately | Found what you are looking for |
| `continue` | Skip to the next iteration | Current item does not match criteria |

```python
# break example - search
for item in items:
    if item == target:
        print("Found!")
        break

# continue example - filter
for item in items:
    if not item["active"]:
        continue
    process(item)
```

### Appendix D: Common loop patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| Accumulate | Sum or collect values | `total += sale` |
| Count | Count matching items | `if condition: count += 1` |
| Filter | Keep matching items | `if condition: result.append(item)` |
| Search | Find first match | `if match: found = item; break` |
| Transform | Build new list | `new_list.append(transform(item))` |
| Flatten | Combine nested lists | `for sublist in nested: for item in sublist:` |

---

## 14. Answers

**Answer 1:**

`for item in my_list:` is the clear winner for iterating over a known list. It is more readable, less error-prone (no index variable to manage), and more Pythonic. The `while` version requires initialising an index variable, incrementing it manually, and accessing items with `my_list[index]` — all of which add boilerplate and introduce potential bugs (forgetting to increment, off-by-one errors).

The `while` version would be better if you need to modify the index dynamically during iteration. For example, if you sometimes need to skip ahead by two positions or go back one position depending on the data, a `while` loop with manual index control gives you that flexibility. This pattern appears in certain parsing algorithms. But for straightforward sequential processing, always prefer `for`.

**Answer 2:**

Without `while/else`, you would need a separate boolean variable to track whether the player won:

```python
won = False
while attempts < max_guesses:
    ...
    if guess == secret:
        won = True
        break
    ...

if won:
    print("Correct!")
else:
    print("Out of guesses!")
```

The `while/else` pattern eliminates the `won` variable entirely. The `else` block runs only when the loop condition becomes `False` (guesses exhausted), not when `break` exits (correct guess). This is cleaner because the success path is handled at the `break` point and the failure path is in the `else` block — no extra variable needed.

The downside is that `while/else` is a Python-specific idiom that many programmers (even experienced ones from other languages) find surprising. In team projects, the explicit boolean approach may be preferred for clarity.

**Answer 3:**

With `continue`, each skip condition appears at the top of the loop body as a guard clause:

```python
for product in products:
    if product["category"] != "electronics":
        continue
    if not product["in_stock"]:
        continue
    # process product (at base indentation)
```

With nested `if` blocks:

```python
for product in products:
    if product["category"] == "electronics":
        if product["in_stock"]:
            # process product (deeply indented)
```

When there are many skip conditions, the `continue` approach keeps the processing code at a low indentation level. Each condition is a flat, independent check. The nested `if` approach creates a rightward drift (the "arrow anti-pattern") where the actual work is buried inside multiple levels of indentation.

For one or two conditions, the difference is minor. For three or more, `continue` is significantly more readable because each guard clause is independent and the main logic remains at base indentation.

**Answer 4:**

A 1000×1000 nested loop runs 1,000,000 iterations. In general, a nested loop of depth $d$ with $n$ iterations at each level runs $n^d$ iterations. This is $O(n^2)$ for two levels, $O(n^3)$ for three levels, and so on.

For the 5×5 multiplication table, 25 iterations are trivial. For 1000×1000, one million iterations are still fast (Python handles this in about a second). But adding a third nesting level with 1000 iterations would mean one billion iterations — this could take hours.

The lesson is to be cautious with nesting depth. Each additional nested loop multiplies the total work by $n$. If you find yourself writing three or more levels of nesting, consider whether a different algorithm or data structure (like a dictionary for lookups instead of a nested search) can reduce the complexity.

**Answer 5:**

Without `break`, the loop continues checking all remaining 499 records after finding the target at, say, position 10. The result is still correct — the found item is printed — but the program does 490 unnecessary comparisons. For 500 records, the wasted time is negligible. For 5 million records or repeated searches, it adds up.

More importantly, `break` signals intent. It tells the reader: "we only need one match, and we found it." Without `break`, the reader must scan the rest of the loop body to verify that only the first match matters. This is a clarity issue, not just a performance issue.

If you need to find all matches rather than just the first, then `break` would be incorrect — you want the loop to complete naturally. The choice between using `break` and letting the loop run depends on whether you need one result or all of them.

**Answer 6:**

`enumerate()` provides both the index and the value in a clean, readable way: `for i, item in enumerate(my_list):`. The `range(len(...))` version requires a separate indexing step: `item = my_list[i]`, which is repetitive and error-prone (typo in the index variable, accessing the wrong list).

`enumerate()` also works with any iterable, not just sequences with a length. You can use it with generators, file objects, and other iterables that do not support `len()`.

However, `range(len(...))` is still appropriate when you need the index but not the value (rare), or when you need to modify the list in place: `my_list[i] = new_value`. While you can assign with `enumerate` using the index, the intent is clearer with `range(len(...))` in this specific case. It is also useful when you need to access adjacent elements: `my_list[i]` and `my_list[i + 1]`.

**Answer 7:**

A `for` loop is the natural choice: `for line in file:`. Python's file objects are iterables — you can loop over them directly, and Python reads one line at a time, keeping memory usage constant regardless of file size.

A `while` loop with `readline()` would also work:

```python
while True:
    line = file.readline()
    if not line or line.startswith("END"):
        break
```

For 10 million lines, the answer does not change — `for line in file:` is still the best choice. Python streams the file line by line, so memory usage stays low. The loop simply runs 10 million iterations (or fewer if "END" is found early, using `break`).

The `while` version is only preferable if you need to read variable amounts of data per iteration (e.g., sometimes reading two lines at once) or if the loop termination depends on complex state beyond a simple line check. For the stated problem — find a line starting with "END" — `for` with `break` is cleaner.

---

## 15. Code solutions

### Exercise 2.4.1: sales_report.py

```python
# sales_report.py - Process daily sales data with for loops

daily_sales = [
    120, 85, 200, 150, 90, 310, 175,
    95, 130, 280, 160, 110, 205, 145,
    88, 320, 190, 135, 250, 170, 105,
    275, 140, 195, 300, 180, 115, 230,
    165, 290,
]

print("=== Monthly sales report ===\n")

# Basic statistics
total = sum(daily_sales)
average = total / len(daily_sales)
highest = max(daily_sales)
lowest = min(daily_sales)

print(f"  Days recorded: {len(daily_sales)}")
print(f"  Total sales:   ${total:,}")
print(f"  Average:       ${average:,.2f}")
print(f"  Highest day:   ${highest}")
print(f"  Lowest day:    ${lowest}")

# Count days above and below average
above_average = 0
below_100 = 0

for sale in daily_sales:
    if sale > average:
        above_average += 1
    if sale < 100:
        below_100 += 1

print(f"\n  Days above average: {above_average}")
print(f"  Days below $100:   {below_100}")

# Weekly breakdown using range with step
print("\n--- Weekly breakdown ---\n")
week = 1

for start in range(0, len(daily_sales), 7):
    week_data = daily_sales[start:start + 7]
    week_total = sum(week_data)
    week_avg = week_total / len(week_data)
    print(f"  Week {week}: {week_data}")
    print(f"         Total: ${week_total:,}  Avg: ${week_avg:,.2f}")
    week += 1

# Top 5 days
print("\n--- Top 5 sales days ---\n")
sorted_with_day = sorted(enumerate(daily_sales, start=1), key=lambda x: x[1], reverse=True)

for rank, (day, amount) in enumerate(sorted_with_day[:5], start=1):
    print(f"  {rank}. Day {day:>2}: ${amount}")
```

### Exercise 2.4.2: guessing_game.py

```python
# guessing_game.py - Number guessing game

import random

secret = random.randint(1, 50)
max_guesses = 7
attempts = 0

print("=== Number guessing game ===")
print(f"\nI'm thinking of a number between 1 and 50.")
print(f"You have {max_guesses} guesses.\n")

while attempts < max_guesses:
    guess_str = input(f"Guess {attempts + 1}/{max_guesses}: ").strip()

    # Validate input
    if not guess_str.isdigit():
        print("  Please enter a whole number.\n")
        continue

    guess = int(guess_str)
    attempts += 1

    if guess == secret:
        print(f"\n  Correct! The number was {secret}.")
        print(f"  You got it in {attempts} guess(es)!")
        break
    elif guess < secret:
        print("  Too low!")
    else:
        print("  Too high!")

    remaining = max_guesses - attempts
    if remaining > 0:
        print(f"  ({remaining} guess(es) remaining)\n")
else:
    # This block runs if the while condition becomes False (no break)
    print(f"\n  Out of guesses! The number was {secret}.")

print("\nThanks for playing!")
```

### Exercise 2.4.3: patterns.py

```python
# patterns.py - Geometric patterns with nested loops

size = 5

# Pattern 1: Right triangle
print("--- Right triangle ---")
for row in range(1, size + 1):
    print("* " * row)

print()

# Pattern 2: Inverted right triangle
print("--- Inverted right triangle ---")
for row in range(size, 0, -1):
    print("* " * row)

print()

# Pattern 3: Centered pyramid
print("--- Centered pyramid ---")
for row in range(1, size + 1):
    spaces = " " * (size - row)
    stars = "* " * row
    print(spaces + stars)

print()

# Pattern 4: Number triangle
print("--- Number triangle ---")
for row in range(1, size + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

print()

# Pattern 5: Multiplication table
print("--- Multiplication table (1-5) ---")
print(f"{'':>4}", end="")
for col in range(1, size + 1):
    print(f"{col:>4}", end="")
print()
print("    " + "----" * size)

for row in range(1, size + 1):
    print(f"{row:>3} |", end="")
    for col in range(1, size + 1):
        print(f"{row * col:>4}", end="")
    print()
```

### Exercise 2.4.4: inventory_search.py

```python
# inventory_search.py - Search and filter product inventory

products = [
    {"name": "Laptop", "category": "electronics", "price": 999.99, "in_stock": True},
    {"name": "Headphones", "category": "electronics", "price": 79.99, "in_stock": True},
    {"name": "Desk Chair", "category": "furniture", "price": 249.99, "in_stock": False},
    {"name": "Python Book", "category": "books", "price": 39.99, "in_stock": True},
    {"name": "Monitor", "category": "electronics", "price": 449.99, "in_stock": True},
    {"name": "Bookshelf", "category": "furniture", "price": 129.99, "in_stock": True},
    {"name": "Keyboard", "category": "electronics", "price": 59.99, "in_stock": False},
    {"name": "Notebook", "category": "books", "price": 12.99, "in_stock": True},
    {"name": "Standing Desk", "category": "furniture", "price": 599.99, "in_stock": True},
    {"name": "USB Cable", "category": "electronics", "price": 9.99, "in_stock": True},
]

# 1. Find a specific product by name (use break to stop searching)
print("=== Product search ===\n")
search_name = "Monitor"
found = None

for product in products:
    if product["name"].lower() == search_name.lower():
        found = product
        break

if found:
    status = "In stock" if found["in_stock"] else "Out of stock"
    print(f"  Found: {found['name']} - ${found['price']:.2f} ({status})")
else:
    print(f"  '{search_name}' not found.")

# 2. Filter by category
print("\n--- Electronics ---\n")
for product in products:
    if product["category"] != "electronics":
        continue
    status = "✓" if product["in_stock"] else "✗"
    print(f"  [{status}] {product['name']:<15} ${product['price']:>8.2f}")

# 3. Filter by price range
print("\n--- Products under $100 (in stock) ---\n")
budget_items = []

for product in products:
    if product["price"] >= 100 or not product["in_stock"]:
        continue
    budget_items.append(product)

for item in sorted(budget_items, key=lambda p: p["price"]):
    print(f"  {item['name']:<15} ${item['price']:>7.2f}")

print(f"\n  Found {len(budget_items)} item(s)")

# 4. Category summary
print("\n--- Category summary ---\n")
categories = {}

for product in products:
    cat = product["category"]
    if cat not in categories:
        categories[cat] = {"count": 0, "total_value": 0, "in_stock": 0}
    categories[cat]["count"] += 1
    categories[cat]["total_value"] += product["price"]
    if product["in_stock"]:
        categories[cat]["in_stock"] += 1

for cat, data in sorted(categories.items()):
    print(f"  {cat.capitalize():<15} {data['count']} products, "
          f"${data['total_value']:>8.2f} total, "
          f"{data['in_stock']} in stock")
```
