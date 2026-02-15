# Lab 3.1: Writing reusable functions

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Define functions with `def` and call them with arguments
- Use `return` to send values back from a function
- Define default parameter values and call functions with keyword arguments
- Explain local versus global scope and predict which variable a function uses
- Refactor duplicated code into reusable functions

---

## 3. Prerequisites

**Knowledge prerequisites**: Lists, dictionaries, loops, conditional statements (Day 1 and Day 2 material). Chapter 3.1 presentation completed.

**Previous labs**: Labs 2.1 through 2.4 completed.

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

When you find yourself copying the same block of code and changing only one or two values, that is a signal to create a function. Functions encapsulate a piece of logic behind a name, making your code shorter, easier to read, and easier to fix. Change the function once, and every place that calls it gets the fix automatically.

Functions also make your code testable. Instead of re-running an entire script to check whether one calculation works, you can call the function directly with known inputs and verify the output. This is the foundation of professional software development.

In this lab, you will start by exploring basic function mechanics in the REPL, then refactor a repetitive script into clean functions, build a small string validation library, and experiment with scope to see how Python decides which variable to use.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Explore function definitions, parameters, and return values interactively
- Refactor a repetitive report script into clean, reusable functions
- Build a string validation library with functions for email, phone, and username checks
- Investigate local and global variable scope through experiments

---

### Exercise 3.1.1: Explore functions in the REPL

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Define simple functions, pass arguments, and use return values.

**Scenario**: Before writing a full script, you want to understand how `def`, parameters, and `return` work interactively.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Define and call a simple function:

```python
>>> def greet(name):
...     return f"Hello, {name}!"
...
>>> message = greet("Alice")
>>> print(message)
Hello, Alice!
>>> print(greet("Bob"))
Hello, Bob!
```

3. Try a function with multiple parameters:

```python
>>> def add(a, b):
...     return a + b
...
>>> result = add(10, 25)
>>> print(result)
35
>>> print(add(3.5, 2.1))
5.6
```

4. Explore default parameters:

```python
>>> def power(base, exponent=2):
...     return base ** exponent
...
>>> print(power(5))
25
>>> print(power(5, 3))
125
>>> print(power(2, 10))
1024
```

5. Use keyword arguments:

```python
>>> def describe(name, age, city="unknown"):
...     return f"{name}, age {age}, from {city}"
...
>>> print(describe("Alice", 30, "Prague"))
Alice, age 30, from Prague
>>> print(describe("Bob", 25))
Bob, age 25, from unknown
>>> print(describe(age=40, name="Charlie", city="Brno"))
Charlie, age 40, from Brno
```

6. Observe what happens without `return`:

```python
>>> def greet_no_return(name):
...     print(f"Hello, {name}!")
...
>>> result = greet_no_return("Alice")
Hello, Alice!
>>> print(result)
None
>>> print(type(result))
<class 'NoneType'>
```

7. Exit the REPL:

```python
>>> exit()
```

**Verification**: You defined functions with positional, default, and keyword arguments. You observed that a function without `return` implicitly returns `None`.

---

### Exercise 3.1.2: Refactor a repetitive script

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Identify duplicated code and refactor it into reusable functions.

**Scenario**: You have inherited a sales report script where the same formatting and calculation logic is copy-pasted for three product categories. Your task is to eliminate the repetition.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `sales_refactored.py` in `C:\labs` (`Ctrl+S`).

2. First, look at the **original repetitive code** (do not type this — just read it to understand the problem):

```python
# The REPETITIVE version (do NOT type this)

# Electronics sales
electronics = [1200, 850, 1500, 990, 1100]
electronics_total = sum(electronics)
electronics_avg = electronics_total / len(electronics)
print("=== Electronics ===")
print(f"  Items sold: {len(electronics)}")
print(f"  Total: ${electronics_total:,.2f}")
print(f"  Average: ${electronics_avg:,.2f}")
print(f"  Highest: ${max(electronics):,.2f}")
print(f"  Lowest: ${min(electronics):,.2f}")
print()

# Clothing sales  (same logic, different data)
clothing = [45, 89, 120, 65, 78, 95, 110]
clothing_total = sum(clothing)
clothing_avg = clothing_total / len(clothing)
print("=== Clothing ===")
print(f"  Items sold: {len(clothing)}")
print(f"  Total: ${clothing_total:,.2f}")
print(f"  Average: ${clothing_avg:,.2f}")
print(f"  Highest: ${max(clothing):,.2f}")
print(f"  Lowest: ${min(clothing):,.2f}")
print()

# Books sales  (same logic again)
books = [15, 22, 35, 18, 29, 12, 40, 25]
books_total = sum(books)
books_avg = books_total / len(books)
print("=== Books ===")
print(f"  Items sold: {len(books)}")
print(f"  Total: ${books_total:,.2f}")
print(f"  Average: ${books_avg:,.2f}")
print(f"  Highest: ${max(books):,.2f}")
print(f"  Lowest: ${min(books):,.2f}")
```

3. Now write the **refactored version** with functions. Type this code in your file:

```python
# sales_refactored.py - Sales report using functions


def print_category_report(category_name, sales):
    """Print a formatted sales report for one product category."""
    total = sum(sales)
    average = total / len(sales)
    print(f"=== {category_name} ===")
    print(f"  Items sold: {len(sales)}")
    print(f"  Total: ${total:,.2f}")
    print(f"  Average: ${average:,.2f}")
    print(f"  Highest: ${max(sales):,.2f}")
    print(f"  Lowest: ${min(sales):,.2f}")
    print()


# Data
electronics = [1200, 850, 1500, 990, 1100]
clothing = [45, 89, 120, 65, 78, 95, 110]
books = [15, 22, 35, 18, 29, 12, 40, 25]

# Generate reports - each call replaces 8 lines of repetitive code
print_category_report("Electronics", electronics)
print_category_report("Clothing", clothing)
print_category_report("Books", books)
```

4. Run the script:

```
C:\labs> python sales_refactored.py
```

5. Now add a function that returns summary data as a dictionary instead of printing it. Add this below the existing function:

```python
def calculate_summary(sales):
    """Return a dictionary with sales statistics."""
    return {
        "count": len(sales),
        "total": sum(sales),
        "average": sum(sales) / len(sales),
        "highest": max(sales),
        "lowest": min(sales),
    }


# Compare categories using the return values
categories = {
    "Electronics": electronics,
    "Clothing": clothing,
    "Books": books,
}

print("=== Comparison ===")
for name, data in categories.items():
    summary = calculate_summary(data)
    print(f"  {name}: ${summary['total']:,.2f} total, ${summary['average']:,.2f} avg")
```

6. Run the script again and verify the comparison section appears after the individual reports.

**Verification**: The output shows three identical-format reports followed by a comparison. The refactored version uses 2 function definitions instead of repeating the same logic 3 times. Adding a fourth category would require only one new line, not eight.

**Try it yourself**:
- Add a `"Groceries"` category with sales `[5, 12, 8, 15, 7, 20, 11]` and generate its report with a single function call.
- Add a parameter `currency="$"` to both functions so you can produce reports in different currencies.

---

### Exercise 3.1.3: Build a string validation library

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Write a set of validation functions with default parameters and keyword arguments.

**Scenario**: Many applications need to validate user input — email addresses, phone numbers, usernames. Instead of scattering validation logic across your code, you will build a focused set of functions.

**Tasks**:

1. In VS Code, create a new file. Save it as `validators.py` in `C:\labs`.

2. Type the following code:

```python
# validators.py - String validation functions


def is_valid_email(email):
    """Check if a string looks like a valid email address.

    Rules: must contain exactly one @, must have a dot after @,
    local part and domain must not be empty.
    """
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def is_valid_phone(phone, min_digits=7, max_digits=15):
    """Check if a string contains a valid number of digits.

    Strips spaces, dashes, and a leading + before counting digits.
    """
    cleaned = phone.replace(" ", "").replace("-", "")
    if cleaned.startswith("+"):
        cleaned = cleaned[1:]
    if not cleaned.isdigit():
        return False
    return min_digits <= len(cleaned) <= max_digits


def is_valid_username(username, min_length=3, max_length=20,
                      allow_spaces=False):
    """Check if a username meets length and character requirements.

    Allowed characters: letters, digits, underscores.
    Spaces allowed only if allow_spaces is True.
    """
    if not min_length <= len(username) <= max_length:
        return False
    for char in username:
        if char == " " and allow_spaces:
            continue
        if not (char.isalnum() or char == "_"):
            return False
    return True


# --- Test the validators ---

print("=== Email validation ===")
test_emails = [
    "alice@example.com",
    "bob@company",
    "no-at-sign.com",
    "@missing-local.com",
    "charlie@mail.server.org",
]
for email in test_emails:
    result = is_valid_email(email)
    status = "valid" if result else "INVALID"
    print(f"  {email:<30} {status}")

print()
print("=== Phone validation ===")
test_phones = [
    ("+420 123 456 789", {}),
    ("123-456", {}),
    ("12345", {"min_digits": 5, "max_digits": 5}),
    ("abc-defg", {}),
    ("+1 555 0123", {}),
]
for phone, kwargs in test_phones:
    result = is_valid_phone(phone, **kwargs)
    status = "valid" if result else "INVALID"
    print(f"  {phone:<25} {status}")

print()
print("=== Username validation ===")
test_usernames = [
    ("alice_99", {}),
    ("ab", {}),
    ("this_name_is_way_too_long_for_the_limit", {}),
    ("hello world", {}),
    ("hello world", {"allow_spaces": True}),
    ("inv@lid!", {}),
]
for username, kwargs in test_usernames:
    result = is_valid_username(username, **kwargs)
    status = "valid" if result else "INVALID"
    extras = f" (kwargs: {kwargs})" if kwargs else ""
    print(f"  {username:<40} {status}{extras}")
```

3. Run the script:

```
C:\labs> python validators.py
```

**Expected output**: Three sections showing validation results. Valid emails include the one with a proper `@` and dot. Invalid ones are missing `@`, have no local part, or have no dot in the domain. Phone validation accepts digits with spaces/dashes/plus sign and rejects letters. Username validation checks length and character rules.

**Verification**: Each validator returns `True` or `False`. The phone validator uses default parameters (`min_digits=7`). The username validator demonstrates a keyword argument (`allow_spaces=True`).

**Try it yourself**:
- Add a function `is_valid_password(password, min_length=8, require_digit=True, require_upper=True)` that checks password strength.
- Modify `is_valid_email` to also reject emails where the domain has no dot (already done) and where the local part contains spaces.

---

### Exercise 3.1.4: Explore variable scope

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Understand how Python resolves variable names inside and outside functions.

**Scenario**: Understanding scope prevents hard-to-find bugs. You want to see exactly when Python uses a local variable versus a global one.

**Tasks**:

1. In VS Code, create a new file. Save it as `scope_experiments.py` in `C:\labs`.

2. Type the following code:

```python
# scope_experiments.py - Demonstrate variable scope

# --- Experiment 1: Local vs. global ---
message = "I am global"


def show_message():
    message = "I am local"
    print(f"  Inside function: {message}")


print("Experiment 1: Local vs. global")
show_message()
print(f"  Outside function: {message}")
print()


# --- Experiment 2: Function cannot modify a global without 'global' ---
counter = 0


def increment():
    # This creates a NEW local variable, it does not modify the global
    counter = 1
    print(f"  Inside increment(): counter = {counter}")


print("Experiment 2: Shadowing a global")
print(f"  Before: counter = {counter}")
increment()
print(f"  After: counter = {counter}")
print()


# --- Experiment 3: Functions can READ globals ---
tax_rate = 0.21


def calculate_tax(price):
    # Reading a global is allowed (but not recommended for clarity)
    return price * tax_rate


print("Experiment 3: Reading a global")
print(f"  Tax on 100: {calculate_tax(100)}")
print()


# --- Experiment 4: Better approach - pass values as parameters ---
def calculate_tax_v2(price, rate):
    """Explicit parameter is clearer and more testable."""
    return price * rate


print("Experiment 4: Explicit parameter (preferred)")
print(f"  Tax on 100 at 21%: {calculate_tax_v2(100, 0.21)}")
print(f"  Tax on 100 at 15%: {calculate_tax_v2(100, 0.15)}")
```

3. Run the script:

```
C:\labs> python scope_experiments.py
```

4. Before looking at the output, predict what each experiment prints. Then compare your predictions with the actual output.

**Expected output**:
- Experiment 1: Inside the function prints "I am local", outside prints "I am global" — the function's `message` is a separate variable.
- Experiment 2: `counter` remains `0` after calling `increment()` because the function created a local `counter` rather than modifying the global.
- Experiment 3: The function reads `tax_rate` from the global scope successfully.
- Experiment 4: Passing the rate as a parameter is clearer — you can test the function with different rates without changing any global variable.

**Verification**: The global variables are never modified by the functions. The preferred approach (Experiment 4) makes dependencies explicit through parameters.

---

## 7. Validation checklist

- [ ] Exercise 3.1.1: You defined functions in the REPL with default and keyword arguments
- [ ] Exercise 3.1.2: `sales_refactored.py` produces three category reports and a comparison section
- [ ] Exercise 3.1.3: `validators.py` tests emails, phones, and usernames — each validator returns `True` or `False`
- [ ] Exercise 3.1.4: `scope_experiments.py` demonstrates four scope experiments matching the expected output

```
C:\labs> python sales_refactored.py
# Three category reports, each showing count/total/average/highest/lowest
# Followed by a comparison section

C:\labs> python validators.py
# Three sections: email, phone, username — each line shows valid or INVALID

C:\labs> python scope_experiments.py
# Four experiments showing local vs. global scope behaviour
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: invalid syntax` | Missing colon after `def`, mismatched parentheses | Check the `def` line ends with `:` |
| `IndentationError: expected an indented block` | Empty function body or inconsistent indentation | Add at least one statement inside the function, use 4 spaces |
| `TypeError: missing required argument` | Called a function without providing all required parameters | Check how many parameters the function expects |
| `TypeError: takes X positional arguments but Y were given` | Too many arguments passed | Count the parameters in the `def` line |
| `NameError: name 'x' is not defined` | Variable does not exist in the current scope | Check spelling, ensure it is defined before use |
| `UnboundLocalError` | Trying to read a variable that is assigned later in the same function | Move the assignment before the read, or pass as parameter |

**Common beginner pitfalls:**
- Forgetting the colon `:` after the `def` line
- Forgetting parentheses when calling a function: `greet` vs `greet()`
- Using `print()` inside a function when you should use `return`
- Expecting a function to return a value when it only prints

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found when running → Verify you are in `C:\labs` with `cd C:\labs`

---

## 9. Questions

1. You have a script with the same 10-line block of code appearing in four places. What specific problems would arise when you need to change the logic (for example, fixing a calculation bug)? How do functions solve this?

2. A colleague writes a function that both prints results to the screen and returns a value. Why is it generally better to separate these concerns — one function to calculate and return, another to format and print?

3. Explain why passing `tax_rate` as a parameter to a function is preferable to having the function read a global variable `tax_rate` directly. Consider testing, reusability, and readability.

4. What is the difference between calling `power(5, 3)` and `power(exponent=3, base=5)`? When would you prefer keyword arguments over positional ones?

5. A function defines `data = []` as a default parameter: `def add_item(item, data=[])`. A colleague warns this is dangerous. What is the problem, and what is the standard fix?

6. You write `result = my_function()` and find that `result` is `None`. What are the two most likely causes?

7. Explain why `len()`, `sum()`, and `sorted()` are designed to return values rather than modify and print data directly. How does this design make them more useful?

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del sales_refactored.py
C:\labs> del validators.py
C:\labs> del scope_experiments.py
```

Verify your working directory is clean:

```
C:\labs> dir *.py
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- `def function_name(parameters):` defines a function; call it with `function_name(arguments)`
- `return` sends a value back to the caller; without it, the function returns `None`
- Default parameters (`def f(x, y=10)`) let callers omit arguments that usually have the same value
- Keyword arguments (`f(y=20, x=5)`) make calls readable when a function has many parameters
- Variables assigned inside a function are local — they do not affect variables with the same name outside
- Functions that return values are more reusable than functions that only print — the caller decides what to do with the result
- When you see repeated code, refactor it into a function — fix once, fixed everywhere

---

## 12. Additional resources

- Python Tutorial — Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Python Tutorial — Default Argument Values: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
- Python Tutorial — Keyword Arguments: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
- PEP 8 — Function and Variable Names: https://peps.python.org/pep-0008/#function-and-variable-names
- Real Python — Defining Your Own Python Function: https://realpython.com/defining-your-own-python-function/

---

## 13. Appendices

### Appendix A: Quick reference — function syntax

```python
# Basic function
def function_name(param1, param2):
    """Docstring explaining what the function does."""
    # function body
    return result

# Default parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple return values (returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])

# Keyword arguments at call site
greet(greeting="Hi", name="Alice")
```

### Appendix B: Built-in functions used in this lab

| Function | Purpose |
|----------|---------|
| `len()` | Number of elements |
| `sum()` | Sum of numeric elements |
| `min()` / `max()` | Smallest / largest element |
| `sorted()` | Return a new sorted list |
| `type()` | Return the type of an object |
| `print()` | Display output |
| `input()` | Read user input |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `Ctrl+`` ` (terminal)

---

## 14. Answers

**Answer 1:**

When the same 10-line block appears in four places and you need to fix a bug in it, you must find and update all four copies. Miss one, and your program behaves inconsistently — three places are correct, one still has the bug. As the project grows, you might not even remember where all the copies are.

Functions solve this by centralizing the logic in one place. You write the 10 lines once inside a function and call it from four places. When you fix the bug, you fix it once. This is the DRY (Don't Repeat Yourself) principle. It also reduces the total amount of code, making the script easier to read and navigate.

**Answer 2:**

A function that both calculates and prints is hard to reuse. What if you want the result but do not want to print it — for example, you need to use it in a further calculation, or write it to a file, or send it over a network? You cannot silence the print without modifying the function.

Separating calculation from presentation is a fundamental design principle. The calculation function returns data; the caller decides what to do with it — print it, store it, pass it to another function, or format it differently. This makes the calculation function usable in any context, not just the one where printing is appropriate.

**Answer 3:**

When a function reads a global variable directly, anyone reading the function cannot tell from its signature what data it depends on. You have to read the entire function body to discover the hidden dependency. Passing `tax_rate` as a parameter makes the dependency explicit — it is right there in the function's definition.

For testing, an explicit parameter lets you call `calculate_tax(100, 0.21)` and then `calculate_tax(100, 0.15)` without modifying any global state. If the function reads a global, you would have to change the global variable between tests and remember to reset it afterward. Explicit parameters also make the function reusable in different contexts — different countries, different tax brackets — without any coupling to a global variable.

**Answer 4:**

Both calls produce the same result: `125`. Positional arguments are matched left to right by position: `5` goes to `base`, `3` goes to `exponent`. Keyword arguments are matched by name regardless of order: `exponent=3` goes to `exponent`, `base=5` goes to `base`.

Keyword arguments are preferable when a function has many parameters (especially optional ones), when parameter names add clarity (e.g., `send_email(to="alice@example.com", subject="Report", urgent=True)`), or when you want to skip some defaults and set only specific ones. For simple two-parameter functions like `power(5, 3)`, positional arguments are typically clearer and more concise.

**Answer 5:**

Default mutable arguments are evaluated once — when the function is defined, not each time it is called. This means every call that uses the default shares the **same list object**. If the function appends to `data`, those items persist across calls:

```python
def add_item(item, data=[]):
    data.append(item)
    return data

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] — surprise!
```

The standard fix is to use `None` as the default and create a new list inside the function:

```python
def add_item(item, data=None):
    if data is None:
        data = []
    data.append(item)
    return data
```

Now each call without an explicit `data` argument gets a fresh empty list.

**Answer 6:**

The two most likely causes are: (1) the function does not have a `return` statement at all — it performs some action (like printing) but never returns a value, so Python returns `None` implicitly; (2) the function has a `return` statement, but execution follows a code path that does not reach it — for example, the `return` is inside an `if` block and the condition is `False`, so the function falls through to the end and returns `None`.

In both cases, adding an explicit `return` on every code path ensures the function returns a meaningful value. A quick check: search the function for all `return` statements and verify that every possible path through the function reaches one.

**Answer 7:**

`len()`, `sum()`, and `sorted()` return values because that design maximises flexibility. When a function returns a value, the caller can use it in any way: store it, pass it to another function, use it in a condition, include it in an f-string, or simply ignore it. If these functions printed instead, you could not do any of that without modifying the function itself.

`sorted()` is a good example: it returns a new sorted list, leaving the original unchanged. This lets you keep the original order when you need it and use the sorted version where you need it. If it modified the list in place and printed it, you would lose the original order and have no way to use the sorted result in further calculations. The separation of data transformation from data presentation is a core design principle in Python.

---

## 15. Code solutions

### Exercise 3.1.2: sales_refactored.py

```python
# sales_refactored.py - Sales report using functions


def print_category_report(category_name, sales):
    """Print a formatted sales report for one product category."""
    total = sum(sales)
    average = total / len(sales)
    print(f"=== {category_name} ===")
    print(f"  Items sold: {len(sales)}")
    print(f"  Total: ${total:,.2f}")
    print(f"  Average: ${average:,.2f}")
    print(f"  Highest: ${max(sales):,.2f}")
    print(f"  Lowest: ${min(sales):,.2f}")
    print()


def calculate_summary(sales):
    """Return a dictionary with sales statistics."""
    return {
        "count": len(sales),
        "total": sum(sales),
        "average": sum(sales) / len(sales),
        "highest": max(sales),
        "lowest": min(sales),
    }


# Data
electronics = [1200, 850, 1500, 990, 1100]
clothing = [45, 89, 120, 65, 78, 95, 110]
books = [15, 22, 35, 18, 29, 12, 40, 25]

# Generate reports
print_category_report("Electronics", electronics)
print_category_report("Clothing", clothing)
print_category_report("Books", books)

# Compare categories
categories = {
    "Electronics": electronics,
    "Clothing": clothing,
    "Books": books,
}

print("=== Comparison ===")
for name, data in categories.items():
    summary = calculate_summary(data)
    print(f"  {name}: ${summary['total']:,.2f} total, ${summary['average']:,.2f} avg")
```

### Exercise 3.1.3: validators.py

```python
# validators.py - String validation functions


def is_valid_email(email):
    """Check if a string looks like a valid email address."""
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def is_valid_phone(phone, min_digits=7, max_digits=15):
    """Check if a string contains a valid number of digits."""
    cleaned = phone.replace(" ", "").replace("-", "")
    if cleaned.startswith("+"):
        cleaned = cleaned[1:]
    if not cleaned.isdigit():
        return False
    return min_digits <= len(cleaned) <= max_digits


def is_valid_username(username, min_length=3, max_length=20,
                      allow_spaces=False):
    """Check if a username meets length and character requirements."""
    if not min_length <= len(username) <= max_length:
        return False
    for char in username:
        if char == " " and allow_spaces:
            continue
        if not (char.isalnum() or char == "_"):
            return False
    return True


# --- Test the validators ---

print("=== Email validation ===")
test_emails = [
    "alice@example.com",
    "bob@company",
    "no-at-sign.com",
    "@missing-local.com",
    "charlie@mail.server.org",
]
for email in test_emails:
    result = is_valid_email(email)
    status = "valid" if result else "INVALID"
    print(f"  {email:<30} {status}")

print()
print("=== Phone validation ===")
test_phones = [
    ("+420 123 456 789", {}),
    ("123-456", {}),
    ("12345", {"min_digits": 5, "max_digits": 5}),
    ("abc-defg", {}),
    ("+1 555 0123", {}),
]
for phone, kwargs in test_phones:
    result = is_valid_phone(phone, **kwargs)
    status = "valid" if result else "INVALID"
    print(f"  {phone:<25} {status}")

print()
print("=== Username validation ===")
test_usernames = [
    ("alice_99", {}),
    ("ab", {}),
    ("this_name_is_way_too_long_for_the_limit", {}),
    ("hello world", {}),
    ("hello world", {"allow_spaces": True}),
    ("inv@lid!", {}),
]
for username, kwargs in test_usernames:
    result = is_valid_username(username, **kwargs)
    status = "valid" if result else "INVALID"
    extras = f" (kwargs: {kwargs})" if kwargs else ""
    print(f"  {username:<40} {status}{extras}")
```

### Exercise 3.1.4: scope_experiments.py

```python
# scope_experiments.py - Demonstrate variable scope

message = "I am global"


def show_message():
    message = "I am local"
    print(f"  Inside function: {message}")


print("Experiment 1: Local vs. global")
show_message()
print(f"  Outside function: {message}")
print()

counter = 0


def increment():
    counter = 1
    print(f"  Inside increment(): counter = {counter}")


print("Experiment 2: Shadowing a global")
print(f"  Before: counter = {counter}")
increment()
print(f"  After: counter = {counter}")
print()

tax_rate = 0.21


def calculate_tax(price):
    return price * tax_rate


print("Experiment 3: Reading a global")
print(f"  Tax on 100: {calculate_tax(100)}")
print()


def calculate_tax_v2(price, rate):
    """Explicit parameter is clearer and more testable."""
    return price * rate


print("Experiment 4: Explicit parameter (preferred)")
print(f"  Tax on 100 at 21%: {calculate_tax_v2(100, 0.21)}")
print(f"  Tax on 100 at 15%: {calculate_tax_v2(100, 0.15)}")
```
