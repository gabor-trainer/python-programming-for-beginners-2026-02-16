# Lab 4.4: Review quiz and self-assessment

**Estimated time**: 45 minutes  
**Difficulty level**: Beginner to Intermediate  
**Python version**: 3.12+  
**Tools**: VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Demonstrate understanding of key Python concepts from all four days
- Identify your strengths and areas that need more practice
- Debug and fix common Python errors in code you did not write
- Combine multiple concepts in a short coding exercise
- Create a personal plan for continued Python learning

---

## 3. Prerequisites

**Knowledge prerequisites**: All material from Days 1–4. Chapters 4.1–4.4 presentations completed.

**Previous labs**: All previous labs completed (or at minimum, Labs 4.1–4.3).

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

This lab is different from the previous ones. Instead of introducing new concepts, it asks you to look back at everything you have learned and assess where you stand. You will work through a debugging exercise, a multi-concept coding challenge, and a self-assessment checklist.

The goal is honest self-evaluation. Programming is a skill that develops through practice, and knowing which areas need more work is as valuable as knowing what you have mastered. There are no grades here — only a clear picture of your current abilities and a roadmap for continued growth.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Find and fix bugs in Python code that covers multiple topics
- Write a short program that combines data structures, functions, file I/O, and comprehensions
- Assess your confidence across all course topics

---

### Exercise 4.4.1: Debug and fix

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Read unfamiliar code, identify bugs from error messages and logic errors, and fix them.

**Scenario**: A colleague wrote a script to process temperature data from a file. The script has several bugs — some produce errors, others produce incorrect results. Your task is to find and fix all of them.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `temperatures.txt` in `C:\labs` (`Ctrl+S`) with this content:

```
Prague,15.2
Brno,13.8
Ostrava,12.5
Bratislava,16.1
Vienna,17.3
Budapest,18.0
Warsaw,11.9
Berlin,14.6
Munich,bad_data
Zurich,13.2
```

2. Create another file. Save it as `temp_buggy.py` in `C:\labs`. Type this **buggy** code exactly as shown:

```python
# temp_buggy.py - Process temperature data (CONTAINS BUGS - fix them!)


def load_temperatures(filepath)
    """Load city temperatures from a file. Return a list of tuples."""
    temps = []
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split(",")
            city = parts[0]
            temp = parts[1]
            temps.append((city, temp))
    return temps


def get_stats(temperatures):
    """Calculate and return temperature statistics."""
    temps_only = [t[1] for t in temperatures]
    return {
        "count": len(temps_only)
        "average": sum(temps_only) / len(temps_only),
        "highest": max(temps_only),
        "lowest": min(temps_only),
    }


def find_above(temperatures, threshold):
    """Return cities with temperature above the threshold."""
    result = []
    for city, temp in temperatures:
        if temp > threshold:
            result.append(city)


def main():
    data = load_temperatures("temperatures.txt")
    print(f"Loaded {len(data)} records.\n")

    stats = get_stats(data)
    print(f"Average: {stats['average']:.1f}°C")
    print(f"Highest: {stats['highest']:.1f}°C")
    print(f"Lowest: {stats['lowest']:.1f}°C\n")

    warm_cities = find_above(data, 15.0)
    print(f"Cities above 15°C: {warm_cities}")


main()
```

3. Run the script and observe the error:

```
C:\labs> python temp_buggy.py
```

4. Fix the bugs one at a time. There are **five bugs** in total:
   - One syntax error (the script will not run at all until this is fixed)
   - One syntax error in a dictionary literal
   - One type error (string vs. float)
   - One missing `return` statement
   - One missing error handling (the file contains invalid data)

5. After fixing all bugs, the script should run without errors, skip the invalid data row, and produce correct output.

**Expected output**: After all fixes, the script loads 9 valid records (skipping the "bad_data" entry), prints the average, highest, and lowest temperatures, and lists the cities above 15°C. The average should be based on the 9 valid numeric values.

**Hints**:
- Hint 1: Look carefully at the `def` line of the first function.
- Hint 2: Check the dictionary in `get_stats` — something is missing between two key-value pairs.
- Hint 3: Are the temperatures numbers or strings after reading from the file?
- Hint 4: Does `find_above` return anything?
- Hint 5: What happens when `float("bad_data")` is called?

**Verification**: The script runs without errors, reports 9 records, and the temperature statistics are correct for the 9 valid values.

---

### Exercise 4.4.2: Multi-concept coding challenge

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Write a complete script that combines data structures, functions, file I/O, comprehensions, and error handling.

**Scenario**: You have the same `temperatures.txt` file from Exercise 4.4.1. Write a fresh script (not based on the buggy code) that processes this data using concepts from all four days.

**Tasks**:

1. In VS Code, create a new file. Save it as `temp_analysis.py` in `C:\labs`.

2. Write a script that does all of the following:

   **a)** Define a function `load_data(filepath)` that:
   - Reads the temperature file
   - Converts temperatures to floats
   - Skips lines with invalid data (using `try`/`except`)
   - Returns a list of `(city, temperature)` tuples

   **b)** Use a **list comprehension** to extract cities where the temperature is above the overall average.

   **c)** Use a **dictionary comprehension** to create a dictionary mapping each city to a label: `"warm"` if above average, `"cool"` otherwise.

   **d)** Define a function `write_report(filepath, data, labels)` that writes a summary report to a text file with:
   - The date the report was generated (use `datetime.date.today()`)
   - Each city with its temperature and warm/cool label
   - The average, highest, and lowest temperatures

   **e)** Call the functions, print the results to the screen, and write the report to `temp_report.txt`.

3. Run the script:

```
C:\labs> python temp_analysis.py
```

4. Verify the report file was created:

```
C:\labs> type temp_report.txt
```

**Expected output**: The script prints loaded data count, the list of above-average cities, the label dictionary, and the statistics. The report file contains a formatted summary.

**Hints**:
- Hint 1: Compute the average with `sum(temps) / len(temps)` where `temps` is a list of float values extracted from the tuples.
- Hint 2: Use `from datetime import date` and `date.today()` for the report date.
- Hint 3: For the report, open the file with `open(filepath, "w")` and write formatted strings.

**Verification**: The script handles the invalid data row gracefully. The comprehensions produce correct results. The report file is readable and contains all required sections.

---

### Exercise 4.4.3: Self-assessment checklist

**Time**: 10 minutes  
**Difficulty**: N/A (reflection)  
**Tool**: Paper, notes, or a text file  
**Objective**: Honestly assess your confidence with each major topic from the course.

**Scenario**: Before you leave this training, take stock of where you stand. This is not a test — it is a tool to guide your continued learning.

**Tasks**:

1. For each topic below, rate your confidence on a scale of 1–5:
   - 1 = "I do not understand this at all"
   - 2 = "I vaguely remember it but cannot do it independently"
   - 3 = "I can do it with reference material or examples nearby"
   - 4 = "I can do it independently for common cases"
   - 5 = "I am confident and could explain it to someone else"

**Day 1: Foundations**

| Topic | Confidence (1–5) |
|-------|:-:|
| Running Python scripts and using the REPL | |
| Variables, data types, type conversion | |
| Arithmetic, comparison, logical operators | |
| String indexing, slicing, and methods | |
| f-strings for formatting output | |
| Using uv for project and package management | |

**Day 2: Data structures and control flow**

| Topic | Confidence (1–5) |
|-------|:-:|
| Lists: creating, indexing, slicing, methods | |
| Tuples: immutability and use cases | |
| Dictionaries: key-value pairs, methods | |
| Sets: unique values, set operations | |
| `if`/`elif`/`else` conditional logic | |
| `for` loops with `range()` and iterables | |
| `while` loops with `break`/`continue` | |

**Day 3: Code organisation and robustness**

| Topic | Confidence (1–5) |
|-------|:-:|
| Defining functions with `def` and `return` | |
| Parameters: positional, default, keyword | |
| Variable scope (local vs. global) | |
| Reading and writing files with `open()` and `with` | |
| CSV file processing | |
| Importing modules and using the standard library | |
| `try`/`except` error handling | |
| Reading and understanding tracebacks | |

**Day 4: Pythonic code and integration**

| Topic | Confidence (1–5) |
|-------|:-:|
| List comprehensions (basic and with filter) | |
| Dictionary and set comprehensions | |
| Generator expressions and memory efficiency | |
| Defining classes with `__init__` and methods | |
| Using `__str__` for readable object display | |
| Building a multi-file project | |

2. Identify your **top 3 strongest areas** — topics where you scored 4 or 5.

3. Identify your **top 3 areas for improvement** — topics where you scored 1 or 2.

4. For each area needing improvement, write one concrete action:
   - What will you practice? (e.g., "Write three scripts that read and process CSV files")
   - What resource will you use? (e.g., Python official tutorial, Real Python article)
   - By when? (e.g., "Within two weeks")

**Verification**: You have a completed self-assessment with specific, actionable next steps. This is your personal learning roadmap.

---

## 7. Validation checklist

- [ ] Exercise 4.4.1: All five bugs fixed, `temp_buggy.py` runs correctly with 9 valid records
- [ ] Exercise 4.4.2: `temp_analysis.py` processes data, uses comprehensions, and writes a report file
- [ ] Exercise 4.4.3: Self-assessment completed with confidence ratings and action plan

```
C:\labs> python temp_buggy.py
# Loads 9 records, prints stats and warm cities

C:\labs> python temp_analysis.py
# Prints analysis, creates temp_report.txt

C:\labs> type temp_report.txt
# Shows formatted temperature report
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: expected ':'` | Missing colon after `def`, `if`, `for`, etc. | Add `:` at the end of the line |
| `SyntaxError: invalid syntax` in a dict | Missing comma between key-value pairs | Add `,` after each value except the last |
| `TypeError: '>' not supported between 'str' and 'float'` | Comparing a string to a number | Convert the string to `float()` first |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Trying to sum strings instead of numbers | Ensure values are converted to `float` |
| `ValueError: could not convert string to float` | Data file contains non-numeric values | Wrap `float()` in `try`/`except ValueError` |

**Common beginner pitfalls:**
- Reading a file and forgetting that all values are strings — always convert to `int()` or `float()` when needed
- Missing `return` at the end of a function — the function returns `None`
- Forgetting that `str.split()` returns a list of strings, not automatically typed values
- Debugging by staring at code instead of adding `print()` statements to trace values

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`

---

## 9. Questions

1. You encounter a `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. Without seeing the code, describe at least three different scenarios that could cause this error and how you would investigate each one.

2. Explain the difference between a syntax error and a logic error. Give an example of each using code from this course. Which type is harder to find and why?

3. A function works correctly for a list of 100 items but produces wrong results for an empty list. What is the likely cause? How would you modify the function to handle edge cases?

4. You need to store information about 200 products, each with a name, price, category, and stock count. Compare three approaches: (a) a list of tuples, (b) a list of dictionaries, (c) a list of class instances. For each approach, describe one advantage and one disadvantage.

5. Describe a real-world task from your own work or daily life that you could now automate with Python. Outline the main steps: what data would you read, how would you process it, and what output would you produce?

6. A colleague asks: "Should I use a `for` loop or a list comprehension?" Write guidelines (3–4 rules of thumb) for when each is appropriate, based on what you learned in this course.

7. Explain why `with open("file.txt") as f:` is preferred over `f = open("file.txt")` followed by `f.close()`. What can go wrong with the manual approach?

8. You wrote a 300-line script in a single file. It works, but adding new features is becoming difficult. Describe the steps you would take to refactor it into a better structure, and explain what benefits the refactoring would provide.

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del temp_buggy.py
C:\labs> del temp_analysis.py
C:\labs> del temperatures.txt
C:\labs> del temp_report.txt
```

Verify your working directory is clean:

```
C:\labs> dir *.py *.txt
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- Debugging is a systematic process: read the error message, identify the line, understand the cause, fix it, and test
- Combining multiple concepts (data structures, functions, file I/O, comprehensions, error handling) is what makes Python practical
- Honest self-assessment reveals where to focus your continued learning
- Every topic in this course connects to the others — understanding these connections is more valuable than memorising syntax
- The skills you have built are immediately applicable to automation, data processing, and tool building
- Continued practice with real projects is the most effective way to solidify and expand your abilities
- Python's ecosystem (web frameworks, data libraries, automation tools) is accessible to you now that you have the fundamentals

---

## 12. Additional resources

**Official Python resources:**
- Python Tutorial (intermediate topics): https://docs.python.org/3/tutorial/
- Python Standard Library Reference: https://docs.python.org/3/library/
- PEP 8 — Style Guide: https://peps.python.org/pep-0008/

**Continued learning:**
- Real Python (tutorials and articles): https://realpython.com
- Automate the Boring Stuff with Python (free online book): https://automatetheboringstuff.com
- Exercism Python Track (practice with mentoring): https://exercism.org/tracks/python

**Next steps by interest area:**
- Data analysis: pandas documentation — https://pandas.pydata.org/docs/
- Web development: Flask tutorial — https://flask.palletsprojects.com/en/stable/tutorial/
- Automation: Python `pathlib` and `subprocess` modules in the standard library
- Testing: pytest documentation — https://docs.pytest.org

---

## 13. Appendices

### Appendix A: Quick reference — debugging checklist

1. **Read the error message** — the last line tells you the error type, the traceback shows where it happened
2. **Check the line indicated** — and the line above it (syntax errors are often reported one line late)
3. **Add `print()` statements** — print variable values and types at key points
4. **Check types** — use `type(x)` to verify variables are the type you expect
5. **Test in the REPL** — isolate the problematic expression and test it interactively
6. **Check edge cases** — empty lists, zero values, missing files, unexpected input

### Appendix B: Common patterns from this course

```python
# Read and process a file safely
def load_data(filepath):
    results = []
    try:
        with open(filepath) as f:
            for line in f:
                # process each line
                results.append(processed_value)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    return results

# Filter with a comprehension
filtered = [item for item in data if condition(item)]

# Aggregate into a dictionary
totals = {}
for item in data:
    key = item.category
    totals[key] = totals.get(key, 0) + item.value

# Class with __str__
class Record:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"
```

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

Scenario 1: String concatenation attempt. Code like `total = 0` followed by `total = total + some_string` where `some_string` was read from a file and not converted to a number. File I/O returns strings; you must convert with `int()` or `float()`.

Scenario 2: Accumulator initialised as an integer but list contains strings. For example, `result = sum(values)` where `values` is `["10", "20", "30"]`. The `sum()` function starts with 0 (an integer) and tries to add the first string, producing this exact error.

Scenario 3: Format string mistake. Writing `print("Total: " + total)` where `total` is an integer. The fix is to use an f-string (`f"Total: {total}"`) or convert explicitly (`str(total)`).

To investigate: add `print(type(variable))` before the failing line to see what types are involved. Check where the data originates (file, user input, function return) and whether conversion was missed.

**Answer 2:**

A **syntax error** means Python cannot parse your code — it violates the language grammar. Example: `def greet(name)` (missing colon). Python catches these before running any code and points to the exact location. They are easy to find because the program will not start at all.

A **logic error** means the code runs without errors but produces wrong results. Example: `average = sum(scores) / len(scores) + 1` when you meant `/ (len(scores) + 1)` — operator precedence causes the wrong calculation. The program runs, prints a number, and nothing indicates it is wrong.

Logic errors are harder to find because there is no error message. You must notice the wrong output, trace through the logic, and figure out where your reasoning diverged from the code. Adding `print()` statements and testing with known inputs (where you can verify the expected output) are the primary tools for finding logic errors.

**Answer 3:**

The likely cause is a division by zero or an operation that assumes the list has at least one element. For example, `average = sum(items) / len(items)` crashes with `ZeroDivisionError` when the list is empty. Or `highest = max(items)` raises `ValueError: max() arg is an empty sequence`.

The fix is to check for the edge case at the start of the function: `if not items: return {}` (or return 0, or return None — whatever makes sense for the context). This guard clause handles the empty case explicitly before any calculations that assume data exists. Good functions always consider: what if the input is empty? What if the input has one element? What if the input contains unexpected values?

**Answer 4:**

**(a) List of tuples**: `[("Laptop", 999.99, "electronics", 15), ...]`. Advantage: compact and memory-efficient, works well with unpacking. Disadvantage: you must remember the position of each field — `product[0]` is the name, `product[2]` is the category — which is error-prone and unreadable.

**(b) List of dictionaries**: `[{"name": "Laptop", "price": 999.99, ...}, ...]`. Advantage: fields are accessed by name (`product["price"]`), which is self-documenting. Disadvantage: no structure enforcement — typos in keys create silent bugs, and there is no validation or behaviour attached to the data.

**(c) List of class instances**: `[Product("Laptop", 999.99, "electronics", 15), ...]`. Advantage: defined structure catches typos, methods can validate and transform data, IDE autocomplete shows available attributes. Disadvantage: requires more upfront code (the class definition), which may be overhead for quick one-off scripts.

For 200 products with ongoing operations (filtering, sorting, reporting), classes provide the best balance of safety and functionality. For a quick data exploration in the REPL, dictionaries are faster to set up.

**Answer 5:**

This is a personal reflection question. A strong answer identifies a specific task (not a vague category), names the data source, describes the processing steps, and specifies the output. For example:

"I regularly compile a weekly summary of team hours from a CSV export of our time-tracking tool. Currently I do this manually in a spreadsheet. With Python, I would: (1) read the CSV file using `csv.DictReader`, (2) filter rows to the current week using `datetime`, (3) use a dictionary comprehension to sum hours per team member, (4) calculate team totals and averages, and (5) write a formatted report to a text file. This would take about 50 lines of code and save me 30 minutes every week."

**Answer 6:**

Rule 1: **Use a comprehension when building a new collection from an existing one.** If the pattern is "for each item in X, compute Y and collect the results," a comprehension expresses this directly: `[f(x) for x in items]`.

Rule 2: **Use a loop when performing side effects.** Printing, writing to files, modifying external state, or calling functions for their effects (not their return values) should use a plain `for` loop.

Rule 3: **Use a loop when the logic has more than two branches or exceeds one line of reasonable length.** Complex filtering with nested conditions, multiple transformations, or error handling is clearer as a loop with explicit `if`/`elif`/`else` blocks.

Rule 4: **Use a generator expression when you only need to iterate once and the data is large.** If you are passing the result directly to `sum()`, `max()`, `any()`, or a `for` loop and never need the data again, a generator avoids building the entire list in memory.

**Answer 7:**

The `with` statement guarantees the file is closed when the block exits — even if an exception occurs. Without `with`, an exception between `f = open(...)` and `f.close()` skips the close call, leaving the file open. On Windows, an open file cannot be deleted, moved, or written to by other programs, causing hard-to-diagnose problems.

Even without exceptions, forgetting `f.close()` entirely is a common mistake. Python eventually closes the file when the object is garbage collected, but the timing is unpredictable. In a long-running program or a loop that opens many files, you can exhaust the operating system's file handle limit. The `with` statement makes resource management automatic and reliable — it is the Pythonic standard for any operation that acquires and releases a resource.

**Answer 8:**

Step 1: **Identify responsibilities.** Read through the script and group related functions: data loading, data processing, user interface, output/reporting. These are your future modules.

Step 2: **Extract the data model.** If the script uses dictionaries to represent structured data (products, employees, records), consider converting them to classes. Put the class definitions in a separate file (e.g., `models.py`).

Step 3: **Separate I/O from logic.** Move file reading/writing functions to a `storage.py` or `io_utils.py` module. Move computation and transformation functions to a `processing.py` module. The main script becomes a thin coordinator that calls functions from other modules.

Step 4: **Create a clear entry point.** The `main()` function in `main.py` should read like a high-level summary: load data, process data, display results, save data. Implementation details live in the imported modules.

Benefits: each file is shorter and has a single purpose, making it easier to understand, test, and modify. Adding a new feature means editing one module without risking unrelated breakage. Multiple developers can work on different modules simultaneously. And when you return to the project months later, the file names alone tell you where to look.

---

## 15. Code solutions

### Exercise 4.4.1: temp_buggy.py (fixed version)

```python
# temp_buggy.py - Process temperature data (FIXED)


def load_temperatures(filepath):  # Bug 1: missing colon
    """Load city temperatures from a file. Return a list of tuples."""
    temps = []
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split(",")
            city = parts[0]
            try:  # Bug 5: no error handling for invalid data
                temp = float(parts[1])  # Bug 3: was string, not float
            except ValueError:
                print(f"  Skipping invalid data: {line.strip()}")
                continue
            temps.append((city, temp))
    return temps


def get_stats(temperatures):
    """Calculate and return temperature statistics."""
    temps_only = [t[1] for t in temperatures]
    return {
        "count": len(temps_only),  # Bug 2: missing comma
        "average": sum(temps_only) / len(temps_only),
        "highest": max(temps_only),
        "lowest": min(temps_only),
    }


def find_above(temperatures, threshold):
    """Return cities with temperature above the threshold."""
    result = []
    for city, temp in temperatures:
        if temp > threshold:
            result.append(city)
    return result  # Bug 4: missing return statement


def main():
    data = load_temperatures("temperatures.txt")
    print(f"Loaded {len(data)} records.\n")

    stats = get_stats(data)
    print(f"Average: {stats['average']:.1f}°C")
    print(f"Highest: {stats['highest']:.1f}°C")
    print(f"Lowest: {stats['lowest']:.1f}°C\n")

    warm_cities = find_above(data, 15.0)
    print(f"Cities above 15°C: {warm_cities}")


main()
```

**The five bugs were:**
1. `def load_temperatures(filepath)` — missing colon at the end
2. `"count": len(temps_only)` — missing comma after this line in the dictionary
3. `temp = parts[1]` — temperature stored as string, not converted to `float`
4. `find_above()` — missing `return result` at the end
5. No `try`/`except` around `float(parts[1])` — crashes on "bad_data"

### Exercise 4.4.2: temp_analysis.py

```python
# temp_analysis.py - Temperature data analysis

from datetime import date


def load_data(filepath):
    """Load city temperatures. Skip invalid data."""
    data = []
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            city = parts[0]
            try:
                temp = float(parts[1])
            except ValueError:
                print(f"  Skipping invalid data: {line.strip()}")
                continue
            data.append((city, temp))
    return data


def write_report(filepath, data, labels, stats):
    """Write a temperature report to a text file."""
    with open(filepath, "w") as f:
        f.write(f"Temperature Report — {date.today()}\n")
        f.write("=" * 45 + "\n\n")

        f.write("City data:\n")
        for city, temp in data:
            label = labels[city]
            f.write(f"  {city:<15} {temp:>5.1f}°C  ({label})\n")

        f.write(f"\nStatistics:\n")
        f.write(f"  Average: {stats['average']:.1f}°C\n")
        f.write(f"  Highest: {stats['highest']:.1f}°C\n")
        f.write(f"  Lowest:  {stats['lowest']:.1f}°C\n")
        f.write(f"  Count:   {stats['count']}\n")


# Load data
data = load_data("temperatures.txt")
print(f"Loaded {len(data)} valid records.\n")

# Calculate statistics
temps = [t for _, t in data]
avg = sum(temps) / len(temps)
stats = {
    "count": len(temps),
    "average": avg,
    "highest": max(temps),
    "lowest": min(temps),
}

# List comprehension: cities above average
above_avg = [city for city, temp in data if temp > avg]
print(f"Average temperature: {avg:.1f}°C")
print(f"Cities above average: {above_avg}\n")

# Dictionary comprehension: city -> label
labels = {city: "warm" if temp > avg else "cool" for city, temp in data}
print("Labels:")
for city, label in labels.items():
    print(f"  {city}: {label}")
print()

# Print statistics
print(f"Highest: {stats['highest']:.1f}°C")
print(f"Lowest: {stats['lowest']:.1f}°C\n")

# Write report
report_file = "temp_report.txt"
write_report(report_file, data, labels, stats)
print(f"Report written to {report_file}.")
```
