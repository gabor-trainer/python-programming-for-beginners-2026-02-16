# Lab 3.4: Handling errors gracefully

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner–Intermediate  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Use `try`/`except` to catch and handle specific exceptions
- Apply the `else` and `finally` blocks appropriately
- Raise exceptions in your own functions to signal invalid input
- Read a Python traceback and locate the source of an error
- Build a script that logs errors to a file instead of crashing

---

## 3. Prerequisites

**Knowledge prerequisites**: Functions (Chapter 3.1), file I/O (Chapter 3.2), modules (Chapter 3.3). Chapter 3.4 presentation completed.

**Previous labs**: Lab 3.3 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Navigate to your working directory: `cd C:\labs`

**Create the data files needed for this lab:**

1. In VS Code, create a file `scores.txt` in `C:\labs` with this content:

```
85
92
78
invalid
95
88
abc
91
76
100
```

2. Create a file `buggy_script.py` in `C:\labs` with this content (intentionally contains bugs):

```python
# buggy_script.py - This script has intentional bugs for traceback practice

def load_data(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_grade(score):
    grades = {90: "A", 80: "B", 70: "C", 60: "D"}
    for threshold in sorted(grades.keys(), reverse=True):
        if score >= threshold:
            return grades[threshold]
    return "F"


def process_student_scores(filename):
    scores = load_data(filename)
    average = calculate_average(scores)
    grade = get_grade(average)
    print(f"Average: {average:.1f}")
    print(f"Grade: {grade}")


process_student_scores("scores.txt")
```

---

## 5. Concept overview

Errors happen. Files go missing, users type unexpected input, network connections drop, and calculations hit edge cases. A program that crashes on the first unexpected value is fragile and unreliable.

Exception handling lets you anticipate problems and respond to them — retry, use a default, skip a bad record, log a warning, or ask the user to correct their input. Equally important, knowing how to **read tracebacks** lets you find bugs quickly instead of staring at code hoping the problem jumps out.

In this lab, you will add error handling to file-reading code, validate user input, create functions that raise informative exceptions, practise reading tracebacks to find bugs, and build a script that logs errors instead of crashing.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Handle missing files and invalid data in file-reading code
- Build a robust input validation loop with `try`/`except`
- Create functions that raise clear exceptions for invalid arguments
- Read and interpret tracebacks to diagnose bugs in a broken script
- Build a data processor that logs errors to a file and keeps running

---

### Exercise 3.4.1: Handle file-reading errors

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Use `try`/`except` to handle `FileNotFoundError` and `ValueError` when reading data from files.

**Scenario**: You need to read numeric scores from a file. The file might not exist, and some lines might contain invalid data. Your script should handle both problems without crashing.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `safe_reader.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# safe_reader.py - Read scores from a file with error handling


def read_scores(filename):
    """Read numeric scores from a file, skipping invalid lines."""
    scores = []
    skipped = []

    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  Error: File '{filename}' not found.")
        return scores, skipped

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            score = int(stripped)
            scores.append(score)
        except ValueError:
            skipped.append((i, stripped))
            print(f"  Warning: Line {i} is not a number: {stripped!r}")

    return scores, skipped


# --- Test with the existing file ---
print("=== Reading scores.txt ===")
scores, skipped = read_scores("scores.txt")
print()

if scores:
    print(f"  Valid scores: {scores}")
    print(f"  Count: {len(scores)}")
    print(f"  Average: {sum(scores) / len(scores):.1f}")
    print(f"  Highest: {max(scores)}")
    print(f"  Lowest: {min(scores)}")
else:
    print("  No valid scores found.")

if skipped:
    print(f"\n  Skipped {len(skipped)} invalid line(s).")

# --- Test with a missing file ---
print()
print("=== Reading missing_file.txt ===")
scores2, skipped2 = read_scores("missing_file.txt")
print(f"  Scores: {scores2}")
```

3. Run the script:

```
C:\labs> python safe_reader.py
```

**Expected output**: The first section reads `scores.txt`, prints warnings for the two invalid lines ("invalid" and "abc"), then shows statistics for the valid scores. The second section attempts to read a non-existent file and prints an error message without crashing.

**Verification**: The script does not crash despite encountering invalid data and a missing file. It prints 8 valid scores, 2 skipped lines, and handles the missing file gracefully.

**Try it yourself**:
- Add handling for empty files (when the file exists but has no content).
- Modify the function to accept floats as well as integers (use `float()` instead of `int()`).

---

### Exercise 3.4.2: Validate user input

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Build a robust input validation loop using `try`/`except`, `else`, and `continue`.

**Scenario**: Your application needs the user to enter a price and a quantity. Both must be positive numbers. The script should keep asking until it receives valid input.

**Tasks**:

1. In VS Code, create a new file. Save it as `input_validator.py` in `C:\labs`.

2. Type the following code:

```python
# input_validator.py - Validate user input with try/except


def get_positive_number(prompt, number_type=float):
    """Keep asking until the user enters a positive number."""
    while True:
        raw = input(prompt)
        try:
            value = number_type(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Try again.")
            continue

        if value <= 0:
            print(f"  {value} is not positive. Enter a number greater than 0.")
            continue

        return value


def get_choice(prompt, valid_options):
    """Keep asking until the user enters one of the valid options."""
    options_str = "/".join(valid_options)
    while True:
        raw = input(f"{prompt} ({options_str}): ").strip().lower()
        if raw in valid_options:
            return raw
        print(f"  Invalid choice: '{raw}'. Expected one of: {options_str}")


# --- Collect order information ---
print("=== Simple order entry ===\n")

product = input("Product name: ")
price = get_positive_number("Price: $")
quantity = get_positive_number("Quantity: ", number_type=int)
confirm = get_choice("Confirm order?", ["yes", "no"])

print()
if confirm == "yes":
    total = price * quantity
    print(f"  Order confirmed:")
    print(f"  Product:  {product}")
    print(f"  Price:    ${price:,.2f}")
    print(f"  Quantity: {quantity}")
    print(f"  Total:    ${total:,.2f}")
else:
    print("  Order cancelled.")
```

3. Run the script and test it with invalid inputs:

```
C:\labs> python input_validator.py
```

Try entering:
- `abc` for the price (should show an error and re-prompt)
- `-5` for the price (should show an error and re-prompt)
- `29.99` for the price (should accept)
- `0` for quantity (should show an error)
- `3` for quantity (should accept)
- `maybe` for confirmation (should show an error)
- `yes` for confirmation (should accept and show the order)

**Expected output**: The script rejects all invalid inputs with clear messages and only proceeds when valid values are provided. The final order summary shows the correct total.

**Verification**: No matter what you type, the script never crashes. It always either re-prompts or completes the order.

---

### Exercise 3.4.3: Create functions that raise exceptions

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Write functions that validate their inputs and raise descriptive exceptions when arguments are invalid.

**Scenario**: You are building a simple banking module. Functions for deposits, withdrawals, and transfers must reject invalid amounts and raise clear errors so the calling code can handle them.

**Tasks**:

1. In VS Code, create a new file. Save it as `banking.py` in `C:\labs`.

2. Type the following code:

```python
# banking.py - Banking functions with exception raising


def create_account(owner, initial_balance=0):
    """Create a bank account dictionary."""
    if not owner or not owner.strip():
        raise ValueError("Account owner name cannot be empty")
    if not isinstance(initial_balance, (int, float)):
        raise TypeError(
            f"Balance must be a number, got {type(initial_balance).__name__}"
        )
    if initial_balance < 0:
        raise ValueError(
            f"Initial balance cannot be negative, got {initial_balance}"
        )
    return {"owner": owner.strip(), "balance": float(initial_balance)}


def deposit(account, amount):
    """Add money to an account."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Deposit amount must be positive, got {amount}")
    account["balance"] += amount
    return account["balance"]


def withdraw(account, amount):
    """Remove money from an account."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Withdrawal amount must be positive, got {amount}")
    if amount > account["balance"]:
        raise ValueError(
            f"Insufficient funds: balance is {account['balance']:.2f}, "
            f"requested {amount:.2f}"
        )
    account["balance"] -= amount
    return account["balance"]


def transfer(from_account, to_account, amount):
    """Transfer money between two accounts."""
    withdraw(from_account, amount)
    deposit(to_account, amount)


# --- Test the banking functions ---
print("=== Banking operations ===\n")

# Create accounts
alice = create_account("Alice", 1000)
bob = create_account("Bob", 500)
print(f"  Alice's balance: ${alice['balance']:,.2f}")
print(f"  Bob's balance:   ${bob['balance']:,.2f}")
print()

# Successful operations
print("--- Successful operations ---")
deposit(alice, 250)
print(f"  Alice deposited $250. Balance: ${alice['balance']:,.2f}")

withdraw(bob, 100)
print(f"  Bob withdrew $100. Balance: ${bob['balance']:,.2f}")

transfer(alice, bob, 300)
print(f"  Alice transferred $300 to Bob.")
print(f"  Alice's balance: ${alice['balance']:,.2f}")
print(f"  Bob's balance:   ${bob['balance']:,.2f}")
print()

# Error handling - each error is caught and displayed
print("--- Error handling ---")

test_cases = [
    ("Negative deposit", lambda: deposit(alice, -50)),
    ("Overdraft withdrawal", lambda: withdraw(bob, 10000)),
    ("Empty account name", lambda: create_account("")),
    ("String as amount", lambda: deposit(alice, "fifty")),
    ("Zero withdrawal", lambda: withdraw(alice, 0)),
]

for description, operation in test_cases:
    try:
        operation()
        print(f"  {description}: Succeeded (unexpected)")
    except (ValueError, TypeError) as e:
        print(f"  {description}: {type(e).__name__}: {e}")

print()
print(f"  Final - Alice: ${alice['balance']:,.2f}")
print(f"  Final - Bob:   ${bob['balance']:,.2f}")
```

3. Run the script:

```
C:\labs> python banking.py
```

**Expected output**: Successful operations update balances correctly. The error handling section catches and displays each exception with its type and descriptive message. The balances remain unchanged after failed operations.

**Verification**: After all operations (including the failed ones), Alice's balance is $950.00 and Bob's balance is $700.00. The failed operations did not modify any balances.

---

### Exercise 3.4.4: Read and fix tracebacks

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code, command line  
**Objective**: Read Python tracebacks to identify the source of errors and fix the underlying bugs.

**Scenario**: A colleague gave you `buggy_script.py` (created in the setup section). It crashes when processing the scores file. Your job is to read the traceback, identify the bug, and fix it.

**Tasks**:

1. Run the buggy script:

```
C:\labs> python buggy_script.py
```

2. You will see a traceback. Read it **from the bottom up**:
   - **Last line**: What is the exception type and message?
   - **Line above**: What line of code caused the error?
   - **Read upward**: What function calls led to this point?

3. Answer these questions before proceeding:
   - What exception type is raised?
   - Which function contains the failing line?
   - What is the root cause? (Hint: the file contains non-numeric lines)

4. Now fix the script. In VS Code, create a new file. Save it as `fixed_script.py` in `C:\labs`. Write a corrected version that handles the invalid lines:

```python
# fixed_script.py - Fixed version of buggy_script.py


def load_data(filename):
    """Load numeric data from a file, skipping invalid lines."""
    scores = []
    with open(filename) as f:
        for i, line in enumerate(lines := f.readlines(), start=1):
            stripped = line.strip()
            try:
                scores.append(int(stripped))
            except ValueError:
                print(f"  Skipping line {i}: {stripped!r}")
    return scores


def calculate_average(numbers):
    """Calculate average, handling empty lists."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def get_grade(score):
    """Convert a numeric score to a letter grade."""
    grades = {90: "A", 80: "B", 70: "C", 60: "D"}
    for threshold in sorted(grades.keys(), reverse=True):
        if score >= threshold:
            return grades[threshold]
    return "F"


def process_student_scores(filename):
    """Process scores from a file with full error handling."""
    try:
        scores = load_data(filename)
    except FileNotFoundError:
        print(f"  Error: File '{filename}' not found.")
        return

    if not scores:
        print("  No valid scores found.")
        return

    average = calculate_average(scores)
    grade = get_grade(average)
    print(f"\n  Valid scores: {scores}")
    print(f"  Count: {len(scores)}")
    print(f"  Average: {average:.1f}")
    print(f"  Grade: {grade}")


print("=== Processing scores ===")
process_student_scores("scores.txt")
```

5. Run the fixed script:

```
C:\labs> python fixed_script.py
```

**Expected output**: The fixed script reports which lines were skipped, then shows the average and grade for the valid scores.

**Verification**: The fixed script processes all valid scores, skips invalid lines with a message, handles missing files, and handles empty score lists. Compare with the traceback from the buggy version to confirm you understood the root cause.

---

### Exercise 3.4.5: Build an error-logging data processor

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Build a script that processes data, logs errors to a file, and continues processing despite errors.

**Scenario**: You are processing a batch of records. Some records may be malformed. Instead of crashing on the first bad record, the script should skip it, log the error, and continue. After processing, you review the error log.

**Tasks**:

1. In VS Code, create a new file. Save it as `batch_processor.py` in `C:\labs`.

2. Type the following code:

```python
# batch_processor.py - Process data with error logging

from datetime import datetime


def log_error(message, log_file="processing_errors.log"):
    """Append a timestamped error to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def process_record(record):
    """Process a single record: 'name,score' format.

    Returns a dict with name and score, or raises ValueError.
    """
    parts = record.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"Expected 2 fields, got {len(parts)}")

    name = parts[0].strip()
    if not name:
        raise ValueError("Name field is empty")

    score = int(parts[1].strip())
    if not 0 <= score <= 100:
        raise ValueError(f"Score {score} is out of range 0-100")

    return {"name": name, "score": score}


def process_batch(records):
    """Process a batch of records, logging errors and continuing."""
    results = []
    error_count = 0

    for i, record in enumerate(records, start=1):
        try:
            result = process_record(record)
            results.append(result)
        except (ValueError, IndexError) as e:
            error_count += 1
            error_msg = f"Record {i}: {e} (raw: {record.strip()!r})"
            log_error(error_msg)
            print(f"  Error in record {i}: {e}")

    return results, error_count


# --- Sample data (some records are intentionally malformed) ---
raw_records = [
    "Alice,92",
    "Bob,85",
    "Charlie",
    "Diana,78",
    ",90",
    "Eve,abc",
    "Frank,105",
    "Grace,88",
    "Hank,71",
    "Ivy,95,extra",
]

print("=== Processing batch ===\n")
results, errors = process_batch(raw_records)

print(f"\n=== Summary ===")
print(f"  Total records:  {len(raw_records)}")
print(f"  Processed:      {len(results)}")
print(f"  Errors:         {errors}")

if results:
    scores = [r["score"] for r in results]
    print(f"\n  Average score: {sum(scores) / len(scores):.1f}")
    print(f"  Highest: {max(results, key=lambda r: r['score'])}")
    print(f"  Lowest:  {min(results, key=lambda r: r['score'])}")

# Show the error log
print(f"\n=== Error log contents ===")
try:
    with open("processing_errors.log") as f:
        print(f.read())
except FileNotFoundError:
    print("  (no errors logged)")
```

3. Run the script:

```
C:\labs> python batch_processor.py
```

**Expected output**: The script processes 6 valid records and reports 4 errors. The error log file contains timestamped entries for each failed record — "Charlie" (wrong field count), empty name, "abc" (not a number), "105" (out of range), and "extra" (too many fields).

**Verification**: Check `processing_errors.log` — it should contain one line per error with timestamps and descriptive messages.

```
C:\labs> type processing_errors.log
```

---

## 7. Validation checklist

- [ ] Exercise 3.4.1: `safe_reader.py` reads valid scores, warns about invalid lines, handles missing files
- [ ] Exercise 3.4.2: `input_validator.py` never crashes regardless of user input
- [ ] Exercise 3.4.3: `banking.py` shows successful operations and caught exceptions with descriptive messages
- [ ] Exercise 3.4.4: `fixed_script.py` processes `scores.txt` without crashing, skips invalid lines
- [ ] Exercise 3.4.5: `batch_processor.py` processes valid records and logs errors to `processing_errors.log`

```
C:\labs> python safe_reader.py
# Reads scores.txt with warnings, handles missing file

C:\labs> python banking.py
# Shows operations and caught exceptions

C:\labs> python fixed_script.py
# Processes scores without crashing

C:\labs> python batch_processor.py
# Processes batch, logs errors to processing_errors.log

C:\labs> type processing_errors.log
# Timestamped error entries
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: invalid syntax` on `except` | Missing colon, or `except` without a preceding `try` | Check that `try:` and `except ...:` both end with colons |
| `IndentationError` in try/except | Inconsistent indentation between `try` and `except` | Ensure `try`, `except`, `else`, `finally` are at the same level |
| `NameError: name 'e' is not defined` | Using `e` outside the `except` block | The variable `e` only exists inside the `except as e:` block |
| `TypeError: catching classes that do not inherit from BaseException` | Passing a non-exception type to `except` | Ensure you are catching an exception class, not a string or value |

**Common beginner pitfalls:**
- Writing `except ValueError, TypeError:` instead of `except (ValueError, TypeError):` — the first syntax is invalid in Python 3
- Putting too much code in `try` — makes it unclear which line caused the error
- Catching `Exception` or bare `except:` — hides bugs you need to see
- Forgetting that `except` blocks only catch exceptions from the `try` block, not from `else` or `finally`

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`
- Data file missing → Re-create it following the setup instructions in Section 4

---

## 9. Questions

1. Explain the difference between catching `ValueError` and catching the generic `Exception`. Why do Python style guides recommend catching specific exceptions?

2. A colleague wraps their entire 50-line `main()` function in a single `try`/`except Exception as e: print(e)` block. What problems does this approach create for debugging and maintenance?

3. When reading a traceback, why should you start at the bottom rather than the top? What information does each section of the traceback provide?

4. You have a function that validates input and currently returns `None` for invalid input. A colleague suggests raising a `ValueError` instead. Compare the two approaches — when is returning `None` acceptable, and when is raising an exception better?

5. Explain the purpose of the `else` block in a `try`/`except`/`else` statement. Why not just put that code at the end of the `try` block? Give a concrete example where the distinction matters.

6. You are writing a data processing pipeline that reads 10,000 records from a CSV file. About 1% of records have errors. Should you stop processing at the first error or log errors and continue? Discuss the trade-offs.

7. A function uses `finally` to close a database connection. Explain why this is safer than closing the connection at the end of the `try` block. What happens if the `except` block itself raises an exception?

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del safe_reader.py
C:\labs> del input_validator.py
C:\labs> del banking.py
C:\labs> del buggy_script.py
C:\labs> del fixed_script.py
C:\labs> del batch_processor.py
C:\labs> del scores.txt
C:\labs> del processing_errors.log
```

Verify your working directory is clean:

```
C:\labs> dir *.py *.txt *.log
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- Always catch **specific** exception types — `except ValueError:`, not bare `except:`
- Keep `try` blocks short and focused on the single operation that might fail
- Use `else` for code that should run only on success (not protected by `except`)
- Use `finally` for cleanup that must happen regardless of success or failure
- `raise ValueError("descriptive message")` in your functions to signal invalid input clearly
- Read tracebacks **from the bottom up**: exception type → failing line → call chain
- For batch processing, log errors and continue rather than crashing on the first problem
- A function that raises exceptions is more robust than one that silently returns `None`

---

## 12. Additional resources

- Python Tutorial — Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html
- Python Built-in Exceptions: https://docs.python.org/3/library/exceptions.html
- PEP 8 — Programming Recommendations (exception handling): https://peps.python.org/pep-0008/#programming-recommendations
- Real Python — Python Exceptions: An Introduction: https://realpython.com/python-exceptions/

---

## 13. Appendices

### Appendix A: Quick reference — exception handling syntax

```python
# Basic try/except
try:
    value = int(user_input)
except ValueError:
    print("Not a valid number.")

# Catch multiple types
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Full try/except/else/finally
try:
    result = risky_operation()
except SomeError:
    handle_error()
else:
    use_result(result)
finally:
    cleanup()

# Raise your own exception
def validate(x):
    if x < 0:
        raise ValueError(f"x must be non-negative, got {x}")
```

### Appendix B: Common built-in exceptions

| Exception | When raised |
|-----------|-------------|
| `ValueError` | Wrong value for the type |
| `TypeError` | Wrong type |
| `IndexError` | Sequence index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object missing attribute/method |
| `NameError` | Undefined name |
| `ImportError` | Failed import |
| `PermissionError` | Insufficient file permissions |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

Catching `ValueError` means your code only handles the specific case where a value is inappropriate — for example, converting a non-numeric string to `int`. Any other error (like a `TypeError`, `KeyError`, or `AttributeError`) propagates up and produces a traceback, alerting you to a genuine bug.

Catching `Exception` catches *nearly every* error, including bugs in your own code that you did not anticipate. A misspelled variable name (`NameError`), an incorrect method call (`AttributeError`), or passing the wrong type (`TypeError`) would all be silently swallowed. You would see your generic error message instead of the traceback that points to the actual bug. Python style guides recommend catching specific exceptions because it separates *expected failures* (which you handle) from *unexpected bugs* (which you need to see and fix).

**Answer 2:**

A single `try`/`except` around 50 lines creates several problems. First, when an error occurs, you do not know which of the 50 lines caused it — the error message says what went wrong but the broad `except` catches errors from any line. Second, different errors require different responses: a missing file needs a different recovery than a malformed number, but the single `except` gives them all the same treatment. Third, bugs in the function itself are caught and hidden — if you introduce a typo or logic error, it is silently printed as a generic error instead of producing a traceback.

The fix is to use focused `try`/`except` blocks around specific operations: one around the file open, another around data conversion, another around the calculation. Each handles its expected failure mode. Unexpected errors are left uncaught so they produce tracebacks during development.

**Answer 3:**

A traceback reads from oldest call to newest call (top to bottom). The **bottom line** tells you *what* went wrong (exception type and message). The **entry above it** tells you *where* it happened (file, line number, and the actual code). The **entries above that** show the *call chain* — how execution reached that point.

Starting at the bottom is efficient because the exception type immediately narrows the problem. `ValueError` means a bad value, `FileNotFoundError` means a missing file, `ZeroDivisionError` means you divided by zero. Once you know the type, you look at the failing line for context. Only if the bug is not obvious do you read upward through the call chain to understand how that code was reached with those particular arguments.

**Answer 4:**

Returning `None` for invalid input is acceptable when the function is a simple lookup or conversion where "not found" is a normal outcome — like `dict.get(key)` returning `None` for missing keys. The caller expects to check the return value: `if result is not None:`.

Raising a `ValueError` is better when invalid input is a mistake that the caller should address. It forces the caller to handle the error explicitly (or see a traceback if they do not). A function that silently returns `None` can lead to bugs where `None` is accidentally used in further calculations, producing confusing errors far from the original problem. The general rule: if the caller can reasonably pass invalid input by mistake, raise an exception with a descriptive message. If "no result" is a normal part of the function's contract, returning `None` (or a sentinel value) is appropriate.

**Answer 5:**

Code in the `else` block runs only if the `try` block completed without raising an exception. The key distinction: code in `else` is **not protected** by the `except` block. If `else` code raises an error, that error propagates normally instead of being caught.

Example: you open a file in `try` and catch `FileNotFoundError`. In `else`, you process the file content. If processing raises a `ValueError`, you want to see that error — it is a bug in your processing logic, not a missing file. If you put the processing code inside `try`, the `except FileNotFoundError` would not catch it (correct type), but a broader `except` might. Using `else` keeps the intent clear: "this code runs on success and should not be error-protected."

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File missing")
else:
    # If this line has a bug, you see the traceback
    data = process(f.read())
    f.close()
```

**Answer 6:**

Stopping at the first error is simpler and appropriate when data integrity is critical — for example, financial transactions or database migrations where partial processing could leave the system in an inconsistent state.

Logging and continuing is better for batch analytics, data imports, and report generation. If 100 out of 10,000 records are bad, you still want results from the other 9,900. The error log lets you review and fix the bad records later. The trade-off is complexity: you need a logging mechanism, you need to report how many records succeeded and failed, and you need to ensure that one bad record does not corrupt the results for others. In practice, most data processing pipelines log and continue because re-running 10,000 records due to one bad record is wasteful.

**Answer 7:**

The `finally` block runs regardless of what happens — whether the `try` succeeds, the `except` handles an error, or even if the `except` block itself raises a new exception. If you close the connection at the end of `try`, it is skipped when an exception occurs. If you close it at the end of `except`, it is skipped when no exception occurs (or when a different exception type is raised). Only `finally` guarantees execution in all cases.

If the `except` block raises an exception, the `finally` block still runs before the new exception propagates. This is essential for resource cleanup — you cannot risk leaving a database connection open because an error handler itself failed. This is why `finally` (and the `with` statement, which uses the same mechanism) is the standard pattern for managing resources in Python.

---

## 15. Code solutions

### Exercise 3.4.1: safe_reader.py

```python
# safe_reader.py - Read scores from a file with error handling


def read_scores(filename):
    """Read numeric scores from a file, skipping invalid lines."""
    scores = []
    skipped = []

    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  Error: File '{filename}' not found.")
        return scores, skipped

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            score = int(stripped)
            scores.append(score)
        except ValueError:
            skipped.append((i, stripped))
            print(f"  Warning: Line {i} is not a number: {stripped!r}")

    return scores, skipped


print("=== Reading scores.txt ===")
scores, skipped = read_scores("scores.txt")
print()

if scores:
    print(f"  Valid scores: {scores}")
    print(f"  Count: {len(scores)}")
    print(f"  Average: {sum(scores) / len(scores):.1f}")
    print(f"  Highest: {max(scores)}")
    print(f"  Lowest: {min(scores)}")
else:
    print("  No valid scores found.")

if skipped:
    print(f"\n  Skipped {len(skipped)} invalid line(s).")

print()
print("=== Reading missing_file.txt ===")
scores2, skipped2 = read_scores("missing_file.txt")
print(f"  Scores: {scores2}")
```

### Exercise 3.4.2: input_validator.py

```python
# input_validator.py - Validate user input with try/except


def get_positive_number(prompt, number_type=float):
    """Keep asking until the user enters a positive number."""
    while True:
        raw = input(prompt)
        try:
            value = number_type(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Try again.")
            continue

        if value <= 0:
            print(f"  {value} is not positive. Enter a number greater than 0.")
            continue

        return value


def get_choice(prompt, valid_options):
    """Keep asking until the user enters one of the valid options."""
    options_str = "/".join(valid_options)
    while True:
        raw = input(f"{prompt} ({options_str}): ").strip().lower()
        if raw in valid_options:
            return raw
        print(f"  Invalid choice: '{raw}'. Expected one of: {options_str}")


print("=== Simple order entry ===\n")

product = input("Product name: ")
price = get_positive_number("Price: $")
quantity = get_positive_number("Quantity: ", number_type=int)
confirm = get_choice("Confirm order?", ["yes", "no"])

print()
if confirm == "yes":
    total = price * quantity
    print(f"  Order confirmed:")
    print(f"  Product:  {product}")
    print(f"  Price:    ${price:,.2f}")
    print(f"  Quantity: {quantity}")
    print(f"  Total:    ${total:,.2f}")
else:
    print("  Order cancelled.")
```

### Exercise 3.4.3: banking.py

```python
# banking.py - Banking functions with exception raising


def create_account(owner, initial_balance=0):
    """Create a bank account dictionary."""
    if not owner or not owner.strip():
        raise ValueError("Account owner name cannot be empty")
    if not isinstance(initial_balance, (int, float)):
        raise TypeError(
            f"Balance must be a number, got {type(initial_balance).__name__}"
        )
    if initial_balance < 0:
        raise ValueError(
            f"Initial balance cannot be negative, got {initial_balance}"
        )
    return {"owner": owner.strip(), "balance": float(initial_balance)}


def deposit(account, amount):
    """Add money to an account."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Deposit amount must be positive, got {amount}")
    account["balance"] += amount
    return account["balance"]


def withdraw(account, amount):
    """Remove money from an account."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Withdrawal amount must be positive, got {amount}")
    if amount > account["balance"]:
        raise ValueError(
            f"Insufficient funds: balance is {account['balance']:.2f}, "
            f"requested {amount:.2f}"
        )
    account["balance"] -= amount
    return account["balance"]


def transfer(from_account, to_account, amount):
    """Transfer money between two accounts."""
    withdraw(from_account, amount)
    deposit(to_account, amount)


print("=== Banking operations ===\n")

alice = create_account("Alice", 1000)
bob = create_account("Bob", 500)
print(f"  Alice's balance: ${alice['balance']:,.2f}")
print(f"  Bob's balance:   ${bob['balance']:,.2f}")
print()

print("--- Successful operations ---")
deposit(alice, 250)
print(f"  Alice deposited $250. Balance: ${alice['balance']:,.2f}")

withdraw(bob, 100)
print(f"  Bob withdrew $100. Balance: ${bob['balance']:,.2f}")

transfer(alice, bob, 300)
print(f"  Alice transferred $300 to Bob.")
print(f"  Alice's balance: ${alice['balance']:,.2f}")
print(f"  Bob's balance:   ${bob['balance']:,.2f}")
print()

print("--- Error handling ---")

test_cases = [
    ("Negative deposit", lambda: deposit(alice, -50)),
    ("Overdraft withdrawal", lambda: withdraw(bob, 10000)),
    ("Empty account name", lambda: create_account("")),
    ("String as amount", lambda: deposit(alice, "fifty")),
    ("Zero withdrawal", lambda: withdraw(alice, 0)),
]

for description, operation in test_cases:
    try:
        operation()
        print(f"  {description}: Succeeded (unexpected)")
    except (ValueError, TypeError) as e:
        print(f"  {description}: {type(e).__name__}: {e}")

print()
print(f"  Final - Alice: ${alice['balance']:,.2f}")
print(f"  Final - Bob:   ${bob['balance']:,.2f}")
```

### Exercise 3.4.4: fixed_script.py

```python
# fixed_script.py - Fixed version of buggy_script.py


def load_data(filename):
    """Load numeric data from a file, skipping invalid lines."""
    scores = []
    with open(filename) as f:
        for i, line in enumerate(lines := f.readlines(), start=1):
            stripped = line.strip()
            try:
                scores.append(int(stripped))
            except ValueError:
                print(f"  Skipping line {i}: {stripped!r}")
    return scores


def calculate_average(numbers):
    """Calculate average, handling empty lists."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def get_grade(score):
    """Convert a numeric score to a letter grade."""
    grades = {90: "A", 80: "B", 70: "C", 60: "D"}
    for threshold in sorted(grades.keys(), reverse=True):
        if score >= threshold:
            return grades[threshold]
    return "F"


def process_student_scores(filename):
    """Process scores from a file with full error handling."""
    try:
        scores = load_data(filename)
    except FileNotFoundError:
        print(f"  Error: File '{filename}' not found.")
        return

    if not scores:
        print("  No valid scores found.")
        return

    average = calculate_average(scores)
    grade = get_grade(average)
    print(f"\n  Valid scores: {scores}")
    print(f"  Count: {len(scores)}")
    print(f"  Average: {average:.1f}")
    print(f"  Grade: {grade}")


print("=== Processing scores ===")
process_student_scores("scores.txt")
```

### Exercise 3.4.5: batch_processor.py

```python
# batch_processor.py - Process data with error logging

from datetime import datetime


def log_error(message, log_file="processing_errors.log"):
    """Append a timestamped error to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def process_record(record):
    """Process a single record: 'name,score' format."""
    parts = record.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"Expected 2 fields, got {len(parts)}")

    name = parts[0].strip()
    if not name:
        raise ValueError("Name field is empty")

    score = int(parts[1].strip())
    if not 0 <= score <= 100:
        raise ValueError(f"Score {score} is out of range 0-100")

    return {"name": name, "score": score}


def process_batch(records):
    """Process a batch of records, logging errors and continuing."""
    results = []
    error_count = 0

    for i, record in enumerate(records, start=1):
        try:
            result = process_record(record)
            results.append(result)
        except (ValueError, IndexError) as e:
            error_count += 1
            error_msg = f"Record {i}: {e} (raw: {record.strip()!r})"
            log_error(error_msg)
            print(f"  Error in record {i}: {e}")

    return results, error_count


raw_records = [
    "Alice,92",
    "Bob,85",
    "Charlie",
    "Diana,78",
    ",90",
    "Eve,abc",
    "Frank,105",
    "Grace,88",
    "Hank,71",
    "Ivy,95,extra",
]

print("=== Processing batch ===\n")
results, errors = process_batch(raw_records)

print(f"\n=== Summary ===")
print(f"  Total records:  {len(raw_records)}")
print(f"  Processed:      {len(results)}")
print(f"  Errors:         {errors}")

if results:
    scores = [r["score"] for r in results]
    print(f"\n  Average score: {sum(scores) / len(scores):.1f}")
    print(f"  Highest: {max(results, key=lambda r: r['score'])}")
    print(f"  Lowest:  {min(results, key=lambda r: r['score'])}")

print(f"\n=== Error log contents ===")
try:
    with open("processing_errors.log") as f:
        print(f.read())
except FileNotFoundError:
    print("  (no errors logged)")
```
