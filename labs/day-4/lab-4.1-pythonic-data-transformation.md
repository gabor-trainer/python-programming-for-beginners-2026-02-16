# Lab 4.1: Pythonic data transformation

**Estimated time**: 60 minutes  
**Difficulty level**: Intermediate  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Rewrite traditional `for` loops as list comprehensions
- Filter and transform data using comprehensions with conditions
- Build dictionaries from lists and other iterables using dictionary comprehensions
- Use generator expressions for memory-efficient data processing
- Choose between comprehensions and regular loops based on readability

---

## 3. Prerequisites

**Knowledge prerequisites**: Functions, file I/O, error handling, lists, dictionaries, loops (Days 1–3 material). Chapter 4.1 presentation completed.

**Previous labs**: Labs 3.1 through 3.4 completed.

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

**Create a data file** for use in later exercises. In VS Code, create a file called `sales_data.csv` in `C:\labs` with this content:

```
product,category,price,quantity
Laptop,electronics,999.99,15
Mouse,electronics,29.99,120
Keyboard,electronics,79.99,85
Desk Lamp,home,45.50,60
Pillow,home,25.00,200
Blender,home,89.99,40
Novel,books,14.99,300
Textbook,books,59.99,75
Notebook,books,4.99,500
Pen Set,office,12.50,350
Stapler,office,8.99,150
Binder,office,6.49,220
T-Shirt,clothing,19.99,180
Jacket,clothing,129.99,30
```

Save the file (`Ctrl+S`).

---

## 5. Concept overview

List comprehensions and generator expressions are Python's preferred tools for creating and transforming collections. Instead of writing a multi-line `for` loop that builds a list one element at a time, a comprehension expresses the same transformation in a single, readable line.

This is not just about saving keystrokes. Comprehensions signal intent: when another developer (or your future self) sees `[x * 2 for x in data if x > 0]`, they immediately understand that this creates a new list by doubling the positive values. The equivalent five-line loop requires reading and mentally tracing each step to reach the same conclusion.

In this lab, you will start with basic comprehensions in the REPL, then apply them to real data from a CSV file, build dictionaries for data aggregation, and compare memory usage between list comprehensions and generator expressions.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Transform lists of data using concise, Pythonic comprehension syntax
- Read a CSV file and filter/transform its contents with comprehensions
- Aggregate data into dictionaries using dictionary comprehensions
- Process large datasets memory-efficiently with generator expressions

---

### Exercise 4.1.1: Explore comprehensions in the REPL

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Write basic list comprehensions, add filter conditions, and use conditional expressions.

**Scenario**: Before working with files and larger data, you want to build confidence with comprehension syntax interactively.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Create a basic list comprehension:

```python
>>> prices = [100, 250, 50, 300, 75]
>>> discounted = [price * 0.9 for price in prices]
>>> print(discounted)
[90.0, 225.0, 45.0, 270.0, 67.5]
```

3. Add a filter condition to keep only values above a threshold:

```python
>>> scores = [85, 42, 91, 67, 55, 78, 95, 38]
>>> passing = [s for s in scores if s >= 60]
>>> print(passing)
[85, 91, 67, 78, 95]
```

4. Use a conditional expression (if/else before `for`) to label each element:

```python
>>> labels = ["pass" if s >= 60 else "fail" for s in scores]
>>> print(labels)
['pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'pass', 'fail']
```

5. Combine transformation and filtering — get the lengths of words longer than 3 characters:

```python
>>> words = ["I", "am", "learning", "Python", "comprehensions"]
>>> long_lengths = [len(w) for w in words if len(w) > 3]
>>> print(long_lengths)
[8, 6, 14]
```

6. Use `range()` in a comprehension:

```python
>>> squares = [n ** 2 for n in range(1, 11)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

7. Try a nested comprehension to flatten a list of lists:

```python
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> flat = [val for row in matrix for val in row]
>>> print(flat)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

8. Exit the REPL:

```python
>>> exit()
```

**Verification**: You wrote comprehensions with transformation, filtering, conditional expressions, `range()`, and nested iteration. Each produced the expected list in a single line.

---

### Exercise 4.1.2: Transform data from a CSV file

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Read a CSV file into a list of dictionaries and use comprehensions to filter, transform, and summarize the data.

**Scenario**: You have a product catalog in `sales_data.csv`. Management wants several views of the data: high-value products, formatted price labels, and category-specific extracts. Instead of writing a loop for each view, you will use comprehensions.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `transform_products.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code to load the CSV data:

```python
# transform_products.py - Data transformation with comprehensions

import csv


def load_products(filepath):
    """Read a CSV file and return a list of dictionaries."""
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


products = load_products("sales_data.csv")
print(f"Loaded {len(products)} products.\n")
```

3. Add comprehensions to transform the data. Continue typing below the existing code:

```python
# Convert price and quantity from strings to numbers
products = [
    {
        "product": p["product"],
        "category": p["category"],
        "price": float(p["price"]),
        "quantity": int(p["quantity"]),
    }
    for p in products
]

# 1. Products that cost more than $50
expensive = [p for p in products if p["price"] > 50]
print("Products over $50:")
for p in expensive:
    print(f"  {p['product']}: ${p['price']:.2f}")
print()

# 2. Formatted price labels
labels = [f"{p['product']}: ${p['price']:.2f}" for p in products]
print("Price labels:")
for label in labels:
    print(f"  {label}")
print()

# 3. Revenue for each product (price * quantity)
revenues = [
    {"product": p["product"], "revenue": p["price"] * p["quantity"]}
    for p in products
]
print("Revenue per product:")
for r in revenues:
    print(f"  {r['product']}: ${r['revenue']:,.2f}")
print()

# 4. Products in a specific category
electronics = [p["product"] for p in products if p["category"] == "electronics"]
print(f"Electronics products: {electronics}")
print()

# 5. Products with low stock (quantity < 50)
low_stock = [
    f"{p['product']} ({p['quantity']} units)"
    for p in products
    if p["quantity"] < 50
]
print("Low stock:")
for item in low_stock:
    print(f"  {item}")
```

4. Run the script:

```
C:\labs> python transform_products.py
```

**Expected output**: The script prints five sections. The "Products over $50" section lists items with prices above 50. The revenue section shows each product's price × quantity. The electronics list contains only products in that category. The low stock section shows items with fewer than 50 units. Verify that the number of loaded products matches the number of data rows in your CSV file.

**Verification**: Each transformation is a single comprehension — no explicit `for` loop with `.append()`. The data types are correctly converted from strings to numbers.

**Try it yourself**:
- Add a comprehension that finds all products where revenue exceeds $5,000.
- Create a list of products sorted by price (use `sorted()` with a `key` argument).

---

### Exercise 4.1.3: Dictionary comprehensions for data aggregation

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Build dictionaries from lists using dictionary comprehensions and aggregate data by category.

**Scenario**: You need quick lookups — a dictionary mapping product names to prices, and a summary of how many products exist in each category.

**Tasks**:

1. In VS Code, create a new file. Save it as `aggregate_products.py` in `C:\labs`.

2. Type the following code:

```python
# aggregate_products.py - Dictionary comprehensions for aggregation

import csv


def load_products(filepath):
    """Read a CSV file and return a list of dictionaries with proper types."""
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return [
            {
                "product": row["product"],
                "category": row["category"],
                "price": float(row["price"]),
                "quantity": int(row["quantity"]),
            }
            for row in reader
        ]


products = load_products("sales_data.csv")

# 1. Dictionary: product name -> price (quick lookup)
price_lookup = {p["product"]: p["price"] for p in products}
print("Price lookup dictionary:")
for name, price in price_lookup.items():
    print(f"  {name}: ${price:.2f}")
print()

# 2. Set comprehension: unique categories
categories = {p["category"] for p in products}
print(f"Categories: {sorted(categories)}")
print()

# 3. Dictionary: category -> list of product names
products_by_category = {}
for p in products:
    products_by_category.setdefault(p["category"], []).append(p["product"])

print("Products by category:")
for cat, names in sorted(products_by_category.items()):
    print(f"  {cat}: {names}")
print()

# 4. Dictionary comprehension: category -> total revenue
category_revenue = {}
for p in products:
    cat = p["category"]
    category_revenue[cat] = category_revenue.get(cat, 0) + p["price"] * p["quantity"]

# Now build a sorted summary using a dictionary comprehension
sorted_revenue = {
    cat: total
    for cat, total in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
}
print("Revenue by category (highest first):")
for cat, total in sorted_revenue.items():
    print(f"  {cat}: ${total:,.2f}")
print()

# 5. Dictionary: product name -> price tier using conditional expression
price_tiers = {
    p["product"]: "premium" if p["price"] >= 100 else "standard" if p["price"] >= 25 else "budget"
    for p in products
}
print("Price tiers:")
for name, tier in price_tiers.items():
    print(f"  {name}: {tier}")
```

3. Run the script:

```
C:\labs> python aggregate_products.py
```

**Expected output**: Five sections of output. The price lookup is a flat name-to-price dictionary. The categories set shows unique category names. The products-by-category groups product names under each category. Revenue by category sorts categories from highest to lowest total revenue. Price tiers classify each product as "premium", "standard", or "budget".

**Verification**: The price lookup dictionary has one entry per product. The set comprehension produces unique category names with no duplicates. The revenue totals and price tier assignments are consistent with the CSV data.

**Try it yourself**:
- Create a dictionary that maps each category to its average product price.
- Build a dictionary of only the most expensive product in each category using a comprehension with `max()`.

---

### Exercise 4.1.4: Compare list comprehensions and generator expressions

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Understand when to use a generator expression instead of a list comprehension, and measure the memory difference.

**Scenario**: You need to process a large dataset — say, a million numbers. Building the entire result list in memory is wasteful if you only need to iterate once (for example, to compute a sum or find a maximum). Generator expressions solve this.

**Tasks**:

1. In VS Code, create a new file. Save it as `generators_vs_lists.py` in `C:\labs`.

2. Type the following code:

```python
# generators_vs_lists.py - Compare memory usage and behaviour

import sys

# --- Memory comparison ---
print("=== Memory comparison ===\n")

list_comp = [n ** 2 for n in range(100_000)]
gen_expr = (n ** 2 for n in range(100_000))

list_size = sys.getsizeof(list_comp)
gen_size = sys.getsizeof(gen_expr)

print(f"List comprehension: {list_size:>10,} bytes")
print(f"Generator expression: {gen_size:>10,} bytes")
print(f"Ratio: list is {list_size / gen_size:,.0f}x larger")
print()

# --- Using generators with built-in functions ---
print("=== Generators with built-in functions ===\n")

# Sum of squares from 1 to 1,000,000 — no list needed in memory
total = sum(n ** 2 for n in range(1, 1_000_001))
print(f"Sum of squares (1 to 1,000,000): {total:,}")

# Maximum value — generator feeds values one at a time
largest = max(n ** 2 for n in range(1, 1_001))
print(f"Largest square (1 to 1,000): {largest:,}")
print()

# --- Single-use nature of generators ---
print("=== Generators are single-use ===\n")

gen = (n for n in range(5))
print(f"First iteration:  {list(gen)}")
print(f"Second iteration: {list(gen)}")
print()

# --- Chaining generators for a data pipeline ---
print("=== Generator pipeline ===\n")

# Simulate processing lines from a large file
raw_lines = [
    "  Alice, 85  ",
    "  Bob, 42  ",
    "  Charlie, 91  ",
    "  Diana, 67  ",
    "  Eve, 55  ",
    "  Frank, 78  ",
    "  Grace, 95  ",
]

# Each step is a generator — no intermediate lists
stripped = (line.strip() for line in raw_lines)
parsed = (line.split(", ") for line in stripped)
records = ((name, int(score)) for name, score in parsed)
passing = ((name, score) for name, score in records if score >= 60)

print("Passing students:")
for name, score in passing:
    print(f"  {name}: {score}")
```

3. Run the script:

```
C:\labs> python generators_vs_lists.py
```

**Expected output**: The memory comparison shows the list using significantly more bytes than the generator (the ratio should be several thousand times). The built-in function examples compute sum and max without building a list. The single-use section shows the second iteration returning an empty list. The pipeline section prints only students with scores of 60 or above.

**Verification**: The generator size is around 200 bytes regardless of the range size. The list grows proportionally. The second `list(gen)` call returns `[]`, confirming generators are exhausted after one pass. The pipeline produces the correct filtered output.

**Try it yourself**:
- Modify the pipeline to also compute the average score of passing students (you will need to collect values — think about when a list is necessary).
- Replace the hard-coded `raw_lines` list with `open("some_file.txt")` to see how generators work with real file I/O.

---

## 7. Validation checklist

- [ ] Exercise 4.1.1: You explored comprehensions in the REPL — basic, filtered, conditional, nested
- [ ] Exercise 4.1.2: `transform_products.py` loads CSV data and produces five transformation outputs
- [ ] Exercise 4.1.3: `aggregate_products.py` builds dictionaries for lookups, grouping, and aggregation
- [ ] Exercise 4.1.4: `generators_vs_lists.py` shows the memory difference and demonstrates generator pipelines

```
C:\labs> python transform_products.py
# Five sections: expensive products, price labels, revenue, electronics list, low stock

C:\labs> python aggregate_products.py
# Five sections: price lookup, categories set, products by category, revenue by category, price tiers

C:\labs> python generators_vs_lists.py
# Memory comparison, built-in function usage, single-use demonstration, pipeline output
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: invalid syntax` | Missing bracket, colon, or malformed comprehension | Check matching `[` `]` or `{` `}`, verify `for` and `if` placement |
| `FileNotFoundError` | CSV file not in the current directory | Verify `sales_data.csv` exists in `C:\labs` with `dir sales_data.csv` |
| `ValueError: could not convert string to float` | CSV data has unexpected format | Check CSV for extra spaces or missing values |
| `KeyError` | Wrong dictionary key name | Check column names in the CSV header row |
| `TypeError: 'generator' object is not subscriptable` | Trying to index a generator with `gen[0]` | Convert to a list first with `list(gen)`, or iterate instead |

**Common beginner pitfalls:**
- Putting the `if` condition in the wrong place: after `for` filters elements, before `for` transforms all elements with if/else
- Forgetting that generators are single-use — iterating a second time yields nothing
- Writing overly complex comprehensions that are harder to read than a plain loop
- Confusing `{expr for x in items}` (set) with `{key: val for x in items}` (dict)

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`

---

## 9. Questions

1. You have a list of 1,000 filenames and need to extract only those ending in `.csv`. Compare doing this with a `for` loop and `.append()` versus a list comprehension. Beyond shorter code, what practical advantages does the comprehension offer?

2. A colleague writes `[print(x) for x in items]` to print every item in a list. Explain why this is considered bad practice and what should be used instead.

3. You need to process a 5 GB log file and count how many lines contain the word "ERROR". Would you use a list comprehension or a generator expression? Explain your reasoning, including what would happen with each approach.

4. Consider this comprehension: `[x if x > 0 else -x for x in numbers]`. Rewrite it using a function call inside the comprehension instead. Which version is clearer, and why might you prefer the function approach for more complex conditions?

5. You have two lists of equal length — `names` and `ages` — and need to create a dictionary mapping each name to its age. Write the comprehension. Now explain what would happen if the `names` list contained duplicate names.

6. Explain why `sum(n ** 2 for n in range(1_000_000))` uses almost no memory, while `sum([n ** 2 for n in range(1_000_000)])` (with square brackets) temporarily allocates a large amount of memory. Both produce the same result — when does the difference matter?

7. A nested comprehension like `[val for row in matrix for val in row]` reads left to right: outer loop first, inner loop second. Why does Python use this order, and when would you choose a regular nested loop over a nested comprehension?

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del transform_products.py
C:\labs> del aggregate_products.py
C:\labs> del generators_vs_lists.py
C:\labs> del sales_data.csv
```

Verify your working directory is clean:

```
C:\labs> dir *.py *.csv
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- List comprehensions replace the "create empty list → loop → append" pattern with a single, expressive line
- Add `if condition` after `for` to filter elements; use `if`/`else` before `for` to transform conditionally
- Dictionary comprehensions build dictionaries with `{key: value for item in iterable}`
- Set comprehensions produce unique values with `{expression for item in iterable}`
- Generator expressions use parentheses `()` and produce values on demand — minimal memory regardless of data size
- Generators are single-use: once iterated, they are empty
- Keep comprehensions readable — if it exceeds 80 characters or has complex logic, use a regular loop or a function

---

## 12. Additional resources

- Python Tutorial — List Comprehensions: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- Python Tutorial — Generators: https://docs.python.org/3/tutorial/classes.html#generators
- PEP 274 — Dict Comprehensions: https://peps.python.org/pep-0274/
- PEP 289 — Generator Expressions: https://peps.python.org/pep-0289/
- Real Python — List Comprehensions in Python: https://realpython.com/list-comprehension-python/

---

## 13. Appendices

### Appendix A: Quick reference — comprehension syntax

```python
# List comprehension
result = [expression for item in iterable]

# With filter
result = [expression for item in iterable if condition]

# With conditional expression
result = [val_if_true if condition else val_if_false for item in iterable]

# Dictionary comprehension
result = {key_expr: val_expr for item in iterable}

# Set comprehension
result = {expression for item in iterable}

# Generator expression
result = (expression for item in iterable)

# Nested comprehension (flatten)
result = [val for outer in nested for val in outer]
```

### Appendix B: Built-in functions that work with generators

| Function | Purpose |
|----------|---------|
| `sum()` | Sum of all values |
| `min()` / `max()` | Smallest / largest value |
| `any()` | `True` if any value is truthy |
| `all()` | `True` if all values are truthy |
| `list()` | Convert generator to list |
| `sorted()` | Return sorted list from any iterable |
| `enumerate()` | Pair each value with its index |
| `zip()` | Combine multiple iterables element-wise |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

With a `for` loop, you write five lines: create an empty list, write the `for` statement, write the `if` condition, call `.append()`, and end up with the result in a variable. A list comprehension does this in one line: `csv_files = [f for f in filenames if f.endswith(".csv")]`.

Beyond brevity, the comprehension communicates intent more directly. A reader sees one expression and immediately understands the result: "a filtered list." With the loop, they must read each line and mentally simulate the execution to understand what is being built. Comprehensions also avoid a common bug surface: forgetting to initialise the list, appending to the wrong variable, or accidentally modifying the source list. The single expression makes the operation atomic and self-contained.

In terms of performance, list comprehensions are slightly faster than equivalent loops because the append operation is optimised internally by Python. For 1,000 items the difference is negligible, but it is worth knowing.

**Answer 2:**

`[print(x) for x in items]` builds a list of `None` values (because `print()` returns `None`) that is immediately discarded. This wastes memory and confuses anyone reading the code, because a list comprehension signals "I am creating a list" — but no list is wanted here.

The correct approach is a plain `for` loop: `for x in items: print(x)`. Loops are the right tool when the goal is to perform side effects (printing, writing to files, modifying external state). Comprehensions are for building new collections from existing data. Using the right construct for the right purpose makes your code immediately understandable: a loop means "do something for each item"; a comprehension means "build a new collection from these items."

**Answer 3:**

A list comprehension `[line for line in open("huge.log") if "ERROR" in line]` reads the entire file and stores all matching lines in memory. If the file is 5 GB and 10% of lines contain "ERROR", that is roughly 500 MB of data in a list — plus the overhead of reading the entire file before any processing begins.

A generator expression `sum(1 for line in open("huge.log") if "ERROR" in line)` processes one line at a time. Each line is read, checked, counted, and discarded before the next line is read. Memory usage stays constant regardless of file size. For a task where you only need a count (or a sum, or a maximum), the generator is the right choice because you never need all matching lines in memory simultaneously.

**Answer 4:**

The comprehension `[x if x > 0 else -x for x in numbers]` computes the absolute value of each number. Using a function: `[abs(x) for x in numbers]`. The function version is clearer because `abs` is a well-known built-in whose purpose is obvious from its name.

For simple two-way conditions, inline `if`/`else` is readable. But when the logic has three or more branches or involves complex calculations, a function is better. Consider classifying temperatures as "hot", "warm", "mild", or "cold" — a four-way inline conditional becomes unreadable. Extracting it into a `classify_temperature(t)` function makes the comprehension `[classify_temperature(t) for t in temps]` clean and self-documenting. The function is also independently testable.

**Answer 5:**

The comprehension is: `name_to_age = {name: age for name, age in zip(names, ages)}`. If `names` contains duplicates, the later value overwrites the earlier one. Dictionaries require unique keys, so only the last occurrence of each duplicate name survives. For example, if `"Alice"` appears at positions 0 and 5, the dictionary stores the age from position 5.

This is a silent data loss problem — no error is raised. If duplicates are possible and you need to keep all values, use a different structure: a dictionary mapping each name to a list of ages, or a list of tuples. The choice depends on whether duplicate names are expected (use a list of ages) or a bug (add a check that raises an error).

**Answer 6:**

`sum(n ** 2 for n in range(1_000_000))` passes a generator expression directly to `sum()`. The generator produces one squared value at a time, `sum()` adds it to a running total, and the value is discarded. At any point, only one number and the running total exist in memory.

`sum([n ** 2 for n in range(1_000_000)])` first builds a complete list of one million integers, then passes that list to `sum()`. The list occupies roughly 8 MB of memory while `sum()` iterates over it. After the call, the list is garbage collected, but during the computation it must exist entirely in memory.

The difference matters when processing large datasets — millions of records, multi-gigabyte files, or memory-constrained environments. For small collections (hundreds or thousands of items), both approaches are fine and the list version is arguably clearer.

**Answer 7:**

The order `for row in matrix for val in row` mirrors the equivalent nested loop structure: the outer `for` is written first, the inner `for` second. This consistency means you can convert between loop and comprehension forms mechanically: read the `for` and `if` clauses in the same order as the nested loops, then place the expression at the front.

Python uses this order because the alternative — inner loop first — would require reading right-to-left, which contradicts how English and Python code are normally read. However, nested comprehensions become hard to follow beyond two levels. A regular nested loop with clear indentation is easier to read, debug, and modify when the logic is complex. The rule of thumb: if the comprehension does not fit comfortably on one line, use a loop.

---

## 15. Code solutions

### Exercise 4.1.2: transform_products.py

```python
# transform_products.py - Data transformation with comprehensions

import csv


def load_products(filepath):
    """Read a CSV file and return a list of dictionaries."""
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


products = load_products("sales_data.csv")
print(f"Loaded {len(products)} products.\n")

# Convert price and quantity from strings to numbers
products = [
    {
        "product": p["product"],
        "category": p["category"],
        "price": float(p["price"]),
        "quantity": int(p["quantity"]),
    }
    for p in products
]

# 1. Products that cost more than $50
expensive = [p for p in products if p["price"] > 50]
print("Products over $50:")
for p in expensive:
    print(f"  {p['product']}: ${p['price']:.2f}")
print()

# 2. Formatted price labels
labels = [f"{p['product']}: ${p['price']:.2f}" for p in products]
print("Price labels:")
for label in labels:
    print(f"  {label}")
print()

# 3. Revenue for each product (price * quantity)
revenues = [
    {"product": p["product"], "revenue": p["price"] * p["quantity"]}
    for p in products
]
print("Revenue per product:")
for r in revenues:
    print(f"  {r['product']}: ${r['revenue']:,.2f}")
print()

# 4. Products in a specific category
electronics = [p["product"] for p in products if p["category"] == "electronics"]
print(f"Electronics products: {electronics}")
print()

# 5. Products with low stock (quantity < 50)
low_stock = [
    f"{p['product']} ({p['quantity']} units)"
    for p in products
    if p["quantity"] < 50
]
print("Low stock:")
for item in low_stock:
    print(f"  {item}")
```

### Exercise 4.1.3: aggregate_products.py

```python
# aggregate_products.py - Dictionary comprehensions for aggregation

import csv


def load_products(filepath):
    """Read a CSV file and return a list of dictionaries with proper types."""
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return [
            {
                "product": row["product"],
                "category": row["category"],
                "price": float(row["price"]),
                "quantity": int(row["quantity"]),
            }
            for row in reader
        ]


products = load_products("sales_data.csv")

# 1. Dictionary: product name -> price
price_lookup = {p["product"]: p["price"] for p in products}
print("Price lookup dictionary:")
for name, price in price_lookup.items():
    print(f"  {name}: ${price:.2f}")
print()

# 2. Set comprehension: unique categories
categories = {p["category"] for p in products}
print(f"Categories: {sorted(categories)}")
print()

# 3. Dictionary: category -> list of product names
products_by_category = {}
for p in products:
    products_by_category.setdefault(p["category"], []).append(p["product"])

print("Products by category:")
for cat, names in sorted(products_by_category.items()):
    print(f"  {cat}: {names}")
print()

# 4. Dictionary comprehension: category -> total revenue
category_revenue = {}
for p in products:
    cat = p["category"]
    category_revenue[cat] = category_revenue.get(cat, 0) + p["price"] * p["quantity"]

sorted_revenue = {
    cat: total
    for cat, total in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True)
}
print("Revenue by category (highest first):")
for cat, total in sorted_revenue.items():
    print(f"  {cat}: ${total:,.2f}")
print()

# 5. Dictionary: product name -> price tier
price_tiers = {
    p["product"]: "premium" if p["price"] >= 100 else "standard" if p["price"] >= 25 else "budget"
    for p in products
}
print("Price tiers:")
for name, tier in price_tiers.items():
    print(f"  {name}: {tier}")
```

### Exercise 4.1.4: generators_vs_lists.py

```python
# generators_vs_lists.py - Compare memory usage and behaviour

import sys

# --- Memory comparison ---
print("=== Memory comparison ===\n")

list_comp = [n ** 2 for n in range(100_000)]
gen_expr = (n ** 2 for n in range(100_000))

list_size = sys.getsizeof(list_comp)
gen_size = sys.getsizeof(gen_expr)

print(f"List comprehension: {list_size:>10,} bytes")
print(f"Generator expression: {gen_size:>10,} bytes")
print(f"Ratio: list is {list_size / gen_size:,.0f}x larger")
print()

# --- Using generators with built-in functions ---
print("=== Generators with built-in functions ===\n")

total = sum(n ** 2 for n in range(1, 1_000_001))
print(f"Sum of squares (1 to 1,000,000): {total:,}")

largest = max(n ** 2 for n in range(1, 1_001))
print(f"Largest square (1 to 1,000): {largest:,}")
print()

# --- Single-use nature of generators ---
print("=== Generators are single-use ===\n")

gen = (n for n in range(5))
print(f"First iteration:  {list(gen)}")
print(f"Second iteration: {list(gen)}")
print()

# --- Chaining generators for a data pipeline ---
print("=== Generator pipeline ===\n")

raw_lines = [
    "  Alice, 85  ",
    "  Bob, 42  ",
    "  Charlie, 91  ",
    "  Diana, 67  ",
    "  Eve, 55  ",
    "  Frank, 78  ",
    "  Grace, 95  ",
]

stripped = (line.strip() for line in raw_lines)
parsed = (line.split(", ") for line in stripped)
records = ((name, int(score)) for name, score in parsed)
passing = ((name, score) for name, score in records if score >= 60)

print("Passing students:")
for name, score in passing:
    print(f"  {name}: {score}")
```
