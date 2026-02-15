# Lab 3.2: File operations

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Open and read a text file using `with open(...)` and different read methods
- Count lines, words, and characters in a text file
- Write processed results to a new file
- Append entries to a log file without overwriting existing content
- Read and write CSV files using the `csv` module

---

## 3. Prerequisites

**Knowledge prerequisites**: Functions (Chapter 3.1), strings, loops, lists (Day 1 and Day 2 material). Chapter 3.2 presentation completed.

**Previous labs**: Lab 3.1 completed.

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

1. In VS Code, create a new file. Save it as `sample_text.txt` in `C:\labs` with this content:

```
Python is a versatile programming language.
It is used in web development, data science, and automation.
Python emphasizes readability and simplicity.
Many companies use Python for rapid prototyping.
The standard library provides tools for many common tasks.
```

2. Create another file. Save it as `sales_data.csv` in `C:\labs` with this content:

```
product,category,price,quantity
Laptop,Electronics,999.99,15
Mouse,Electronics,29.99,150
Desk Chair,Furniture,349.50,30
Monitor,Electronics,449.00,45
Bookshelf,Furniture,189.99,20
Keyboard,Electronics,79.99,120
Coffee Table,Furniture,259.00,25
Headphones,Electronics,149.99,80
Filing Cabinet,Furniture,129.99,15
Webcam,Electronics,69.99,95
```

---

## 5. Concept overview

Nearly every useful program reads data from files or writes results to files. Configuration files, log files, CSV exports, reports — file I/O is the bridge between your Python code and persistent data. Without it, every result vanishes when the script ends.

The `with` statement is central to safe file handling in Python. It guarantees the file is closed properly, even if an error occurs mid-read. You will use it in every exercise. The `csv` module handles the tricky details of comma-separated files — quoting, escaping, and line endings — so you do not have to.

In this lab, you will read a text file and analyse its contents, write a report to a new file, build an append-only log, and work with CSV data — skills you will use in virtually every Python project.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Read a text file and count its lines, words, and characters
- Write analysis results to a new file
- Build an append-only log file with timestamps
- Read a CSV file, process its data, and write a summary CSV

---

### Exercise 3.2.1: Read and analyse a text file

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Open a text file, read its contents, and compute basic statistics.

**Scenario**: You have a text file and need to produce a quick summary: how many lines, words, and characters it contains.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `file_stats.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# file_stats.py - Analyse a text file

with open("sample_text.txt") as f:
    content = f.read()

# Count characters (including whitespace)
char_count = len(content)

# Count lines
lines = content.splitlines()
line_count = len(lines)

# Count words
word_count = len(content.split())

# Find the longest line
longest_line = max(lines, key=len)

print("=== File statistics: sample_text.txt ===")
print(f"  Lines:      {line_count}")
print(f"  Words:      {word_count}")
print(f"  Characters: {char_count}")
print(f"  Longest line ({len(longest_line)} chars):")
print(f"    \"{longest_line}\"")
```

3. Run the script:

```
C:\labs> python file_stats.py
```

4. Now extend the script to also show per-line word counts. Add this code at the bottom:

```python
print()
print("=== Per-line word counts ===")
for i, line in enumerate(lines, start=1):
    words = line.split()
    print(f"  Line {i}: {len(words):>2} words  | {line}")
```

5. Run the script again.

**Expected output**: The first section shows total lines, words, and characters. The second section lists each line with its word count. The numbers should be consistent — the total word count equals the sum of per-line word counts.

**Verification**: Check that the total word count matches the sum of per-line word counts.

**Try it yourself**:
- Modify the script to also count the number of sentences (assume each sentence ends with a period).
- Add a count of unique words (hint: use `set(content.lower().split())`).

---

### Exercise 3.2.2: Write results to a file

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Write processed data to a new file using `open()` in write mode.

**Scenario**: Your manager wants the text analysis as a report file, not screen output. You need to write the results to `report.txt`.

**Tasks**:

1. In VS Code, create a new file. Save it as `write_report.py` in `C:\labs`.

2. Type the following code:

```python
# write_report.py - Read a text file and write an analysis report

# Read the source file
with open("sample_text.txt") as f:
    content = f.read()

lines = content.splitlines()
word_count = len(content.split())
char_count = len(content)

# Build the report as a list of strings
report_lines = [
    "=== Text analysis report ===",
    f"Source file: sample_text.txt",
    f"Lines:      {len(lines)}",
    f"Words:      {word_count}",
    f"Characters: {char_count}",
    "",
    "=== Word count per line ===",
]

for i, line in enumerate(lines, start=1):
    words = line.split()
    report_lines.append(f"  Line {i}: {len(words):>2} words")

report_lines.append("")
report_lines.append("=== End of report ===")

# Write the report to a new file
with open("report.txt", "w") as f:
    for line in report_lines:
        f.write(line + "\n")

print(f"Report written to report.txt ({len(report_lines)} lines)")

# Verify by reading it back
print()
print("--- Verifying report.txt ---")
with open("report.txt") as f:
    print(f.read())
```

3. Run the script:

```
C:\labs> python write_report.py
```

4. Open `report.txt` in VS Code to verify its contents.

**Expected output**: The script prints a confirmation message, then displays the contents of `report.txt`. The file should contain the analysis report with the same data as Exercise 3.2.1.

**Verification**: Open `report.txt` in VS Code and confirm it contains the complete report.

**Try it yourself**:
- Modify the script to also write the report to the screen (print each line) and to the file in a single loop.
- Add the current date and time at the top of the report (hint: `from datetime import datetime`).

---

### Exercise 3.2.3: Append to a log file

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use append mode (`"a"`) to add entries to a log file without overwriting.

**Scenario**: Applications often write events to a log file. Each run adds new entries without erasing previous ones. You will build a simple logging function.

**Tasks**:

1. In VS Code, create a new file. Save it as `logger.py` in `C:\labs`.

2. Type the following code:

```python
# logger.py - Append log entries to a file

from datetime import datetime


def log_event(message, log_file="app.log"):
    """Append a timestamped message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(log_file, "a") as f:
        f.write(entry)
    print(f"  Logged: {entry.strip()}")


# Simulate application events
print("=== Logging events ===")
log_event("Application started")
log_event("User 'alice' logged in")
log_event("File 'data.csv' loaded (150 rows)")
log_event("Processing complete")
log_event("Application stopped")

# Show the full log
print()
print("=== Full log contents ===")
with open("app.log") as f:
    print(f.read())
```

3. Run the script:

```
C:\labs> python logger.py
```

4. Run the script **a second time** and notice that the new entries are added below the previous ones — nothing is overwritten.

5. View the log file:

```
C:\labs> type app.log
```

**Expected output**: After the first run, the log contains 5 entries. After the second run, it contains 10 entries. Each entry has a timestamp and message.

**Verification**: Run the script twice and confirm the log file grows rather than being replaced.

---

### Exercise 3.2.4: Read and write CSV files

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use the `csv` module to read structured data, process it, and write a summary CSV.

**Scenario**: You have a CSV file of product sales data. You need to read it, calculate totals per category, and write a summary to a new CSV file.

**Tasks**:

1. In VS Code, create a new file. Save it as `csv_processor.py` in `C:\labs`.

2. Type the following code:

```python
# csv_processor.py - Process a CSV file and write a summary

import csv


def read_sales_data(filename):
    """Read sales data from a CSV file and return a list of dictionaries."""
    products = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "product": row["product"],
                "category": row["category"],
                "price": float(row["price"]),
                "quantity": int(row["quantity"]),
            })
    return products


def calculate_category_totals(products):
    """Calculate revenue totals grouped by category."""
    totals = {}
    for product in products:
        category = product["category"]
        revenue = product["price"] * product["quantity"]
        if category in totals:
            totals[category]["revenue"] += revenue
            totals[category]["items"] += product["quantity"]
            totals[category]["product_count"] += 1
        else:
            totals[category] = {
                "revenue": revenue,
                "items": product["quantity"],
                "product_count": 1,
            }
    return totals


def write_summary_csv(totals, filename):
    """Write category summary to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "products", "total_items", "total_revenue"])
        for category, data in sorted(totals.items()):
            writer.writerow([
                category,
                data["product_count"],
                data["items"],
                f"{data['revenue']:.2f}",
            ])


# Main processing
products = read_sales_data("sales_data.csv")

print(f"Loaded {len(products)} products")
print()

# Show all products
print("=== All products ===")
for p in products:
    revenue = p["price"] * p["quantity"]
    print(f"  {p['product']:<20} {p['category']:<15} ${revenue:>10,.2f}")

print()

# Calculate and display category totals
totals = calculate_category_totals(products)

print("=== Category summary ===")
grand_total = 0
for category, data in sorted(totals.items()):
    print(f"  {category}:")
    print(f"    Products: {data['product_count']}")
    print(f"    Items sold: {data['items']}")
    print(f"    Revenue: ${data['revenue']:,.2f}")
    grand_total += data["revenue"]

print(f"\n  Grand total: ${grand_total:,.2f}")

# Write summary to CSV
write_summary_csv(totals, "category_summary.csv")
print(f"\nSummary written to category_summary.csv")

# Verify by reading it back
print()
print("=== Verifying category_summary.csv ===")
with open("category_summary.csv") as f:
    print(f.read())
```

3. Run the script:

```
C:\labs> python csv_processor.py
```

4. Open `category_summary.csv` in VS Code to verify it is a valid CSV file.

**Expected output**: The script displays all products with revenue, then a category summary showing product count, items sold, and total revenue per category. The summary CSV file contains the same data in CSV format.

**Verification**: Open `category_summary.csv` in VS Code. It should have a header row and one row per category with four columns.

**Try it yourself**:
- Add a "highest-priced product" field to each category in the summary.
- Sort the products by revenue (descending) before displaying them.

---

## 7. Validation checklist

- [ ] Exercise 3.2.1: `file_stats.py` correctly counts lines, words, and characters in `sample_text.txt`
- [ ] Exercise 3.2.2: `report.txt` exists and contains the analysis report
- [ ] Exercise 3.2.3: `app.log` grows with each run (run `logger.py` twice to verify)
- [ ] Exercise 3.2.4: `category_summary.csv` exists with a header row and one row per category

```
C:\labs> python file_stats.py
# Shows line/word/character counts and per-line word counts

C:\labs> type report.txt
# Contains the analysis report

C:\labs> type app.log
# Contains timestamped log entries (more after each run)

C:\labs> type category_summary.csv
# Contains category,products,total_items,total_revenue header and data rows
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` | File does not exist or wrong filename | Check spelling, verify the file is in `C:\labs` |
| `PermissionError` | File is open in another program | Close the file in other applications |
| `UnicodeDecodeError` | File has non-UTF-8 characters | Add `encoding="utf-8"` to `open()` |
| `csv.Error: line contains NUL` | Corrupted or binary file passed to csv reader | Verify the file is a text CSV, not an Excel file |

**Common beginner pitfalls:**
- Forgetting `newline=""` in `open()` when using the `csv` module on Windows (causes blank lines between rows)
- Using `"w"` mode when you meant `"a"` (overwrites the entire file)
- Forgetting to call `.strip()` on lines read from a file (trailing `\n`)
- Not closing files (solved by always using `with`)

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`
- Data file missing → Re-create it following the setup instructions in Section 4

---

## 9. Questions

1. Why does Python recommend the `with open(...) as f:` pattern instead of calling `f = open(...)` and `f.close()` separately? What could go wrong with the manual approach?

2. You need to process a 5 GB log file on a machine with 4 GB of RAM. Why would `f.read()` fail, and which reading method would work instead? Explain your approach.

3. Explain the difference between `"w"` and `"a"` mode. Describe a real scenario where using the wrong one would cause data loss.

4. When writing CSV files on Windows, the `open()` call includes `newline=""`. What happens if you omit it? Why does this issue exist specifically on Windows?

5. Compare `csv.reader` (which returns lists) with `csv.DictReader` (which returns dictionaries). When would you prefer each, and what are the trade-offs?

6. You read a file line by line and print each line, but the output has extra blank lines between each line of text. What is the cause and how do you fix it?

7. A colleague suggests storing application settings in a `.txt` file with one setting per line (e.g., `theme=dark`). Another suggests using a `.csv` file. A third suggests JSON. Discuss the trade-offs of each approach for configuration data.

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del file_stats.py
C:\labs> del write_report.py
C:\labs> del logger.py
C:\labs> del csv_processor.py
C:\labs> del sample_text.txt
C:\labs> del sales_data.csv
C:\labs> del report.txt
C:\labs> del app.log
C:\labs> del category_summary.csv
```

Verify your working directory is clean:

```
C:\labs> dir *.py *.txt *.csv *.log
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- Always use `with open(...) as f:` — it guarantees the file is closed, even if an error occurs
- `"r"` mode reads (default), `"w"` creates/overwrites, `"a"` appends to the end
- `f.read()` loads the entire file; `f.readline()` reads one line; `f.readlines()` returns a list of lines
- For large files, iterate line by line with `for line in f:` instead of loading everything into memory
- When writing CSV on Windows, always use `newline=""` in `open()` to prevent blank rows
- `csv.DictReader` maps each row to a dictionary using the header — cleaner than working with index positions
- Separate reading, processing, and writing into distinct functions for clarity and reusability

---

## 12. Additional resources

- Python Tutorial — Reading and Writing Files: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Python `csv` module documentation: https://docs.python.org/3/library/csv.html
- Python `open()` built-in function: https://docs.python.org/3/library/functions.html#open
- Real Python — Reading and Writing Files in Python: https://realpython.com/read-write-files-python/
- Real Python — Reading and Writing CSV Files in Python: https://realpython.com/python-csv/

---

## 13. Appendices

### Appendix A: Quick reference — file I/O syntax

```python
# Read entire file
with open("file.txt") as f:
    content = f.read()

# Read line by line (memory-efficient)
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# Write to a new file (overwrites if exists)
with open("output.txt", "w") as f:
    f.write("line 1\n")
    f.write("line 2\n")

# Append to a file
with open("log.txt", "a") as f:
    f.write("new entry\n")

# Read CSV with DictReader
import csv
with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column_name"])

# Write CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["col1", "col2"])
    writer.writerow(["value1", "value2"])
```

### Appendix B: File open modes

| Mode | Description | Creates file? | Overwrites? |
|------|-------------|:---:|:---:|
| `"r"` | Read (default) | No | — |
| `"w"` | Write | Yes | Yes |
| `"a"` | Append | Yes | No |
| `"r+"` | Read and write | No | Depends on position |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

The `with` statement guarantees the file is closed when the block ends, regardless of what happens inside — even if an error occurs and the program crashes mid-read. With the manual approach (`f = open(...)`), if an error occurs between `open()` and `f.close()`, the `close()` call is never reached. The file stays open, which can cause data loss (buffered writes not flushed), locked files (especially on Windows where open files cannot be deleted or moved), and resource exhaustion (opening many files without closing them eventually hits the operating system's limit).

The `with` statement removes this risk entirely. It is shorter, safer, and communicates intent clearly: "I am working with this file within this block." There is no practical reason to use the manual approach in modern Python.

**Answer 2:**

`f.read()` loads the entire 5 GB file into memory at once. With only 4 GB of RAM, this will either crash with a `MemoryError` or cause severe swapping and freezing.

The solution is to read the file line by line using `for line in f:`. This approach loads only one line at a time, keeping memory usage constant regardless of file size. For a 5 GB file, each line might be a few hundred bytes — trivial for memory. You process each line, extract what you need, and the previous line is discarded. If you need to accumulate results (like counts or totals), store only the computed values, not the raw lines.

**Answer 3:**

`"w"` (write) mode creates a new file or **overwrites** an existing file — its previous content is erased the moment you open it. `"a"` (append) mode opens the file and positions the write cursor at the end, so new content is added after existing content.

A real data-loss scenario: you have a log file (`app.log`) with weeks of application events. A script opens the log with `"w"` mode to add a new entry. The moment `open("app.log", "w")` executes, all previous log entries are destroyed — even before `f.write()` is called. The correct approach is `"a"` mode, which preserves existing entries and adds the new one at the end.

**Answer 4:**

On Windows, the default text mode translates `\n` to `\r\n` when writing. The `csv` module already adds its own line endings (`\r\n` by default on Windows). Without `newline=""`, Python's text-mode translation adds a second `\r`, resulting in `\r\r\n` — which appears as a blank line between every row when you open the file.

Setting `newline=""` disables this automatic translation, letting the `csv` module handle line endings correctly. This issue does not occur on Linux/macOS because those systems use `\n` natively and the text mode does not add `\r`. Since this training targets Windows, the `newline=""` parameter is essential whenever you use `csv.writer` or `csv.DictWriter`.

**Answer 5:**

`csv.reader` returns each row as a list of strings. You access fields by index: `row[0]`, `row[1]`, `row[2]`. This is lightweight and works well for simple CSVs where column positions are fixed and few. However, if someone reorders the columns in the CSV file, your code breaks silently — `row[2]` now returns a different field.

`csv.DictReader` maps each row to a dictionary using the header row as keys. You access fields by name: `row["product"]`, `row["price"]`. This is more readable, self-documenting, and resilient to column reordering. The trade-off is slightly more memory usage (dictionary overhead per row) and marginally slower performance. For most applications, `DictReader` is the better choice because clarity and correctness outweigh the minimal performance difference.

**Answer 6:**

Each line read from the file ends with `\n` (the newline character). The `print()` function adds its own newline at the end. So you get the line's `\n` plus `print()`'s `\n`, resulting in a double newline (visible as a blank line).

Two fixes: (1) strip the trailing newline with `print(line.strip())` — this also removes leading/trailing spaces, which may or may not be desired. (2) Tell `print()` not to add its own newline: `print(line, end="")`. The second option preserves the line exactly as it appears in the file.

**Answer 7:**

A **plain text file** (`theme=dark`) is human-readable and easy to edit manually. But you need to write your own parser — splitting on `=`, handling edge cases (spaces, comments, multi-line values). It works for simple flat settings but becomes awkward for nested or structured configuration.

A **CSV file** is designed for tabular data (rows and columns of the same structure). Configuration data is typically key-value pairs, not tabular — so CSV is a poor fit. You would end up with a two-column CSV (`key,value`) that is harder to edit manually than a text file and does not support nesting.

**JSON** supports nested structures (dictionaries, lists), is both human-readable and machine-parseable, and Python's built-in `json` module handles it with a few lines of code. The trade-off is that JSON does not support comments (making it less self-documenting) and requires valid syntax (a missing comma breaks the entire file). For most applications, JSON is the best choice for configuration because it balances structure, readability, and tooling support.

---

## 15. Code solutions

### Exercise 3.2.1: file_stats.py

```python
# file_stats.py - Analyse a text file

with open("sample_text.txt") as f:
    content = f.read()

char_count = len(content)
lines = content.splitlines()
line_count = len(lines)
word_count = len(content.split())
longest_line = max(lines, key=len)

print("=== File statistics: sample_text.txt ===")
print(f"  Lines:      {line_count}")
print(f"  Words:      {word_count}")
print(f"  Characters: {char_count}")
print(f"  Longest line ({len(longest_line)} chars):")
print(f"    \"{longest_line}\"")

print()
print("=== Per-line word counts ===")
for i, line in enumerate(lines, start=1):
    words = line.split()
    print(f"  Line {i}: {len(words):>2} words  | {line}")
```

### Exercise 3.2.2: write_report.py

```python
# write_report.py - Read a text file and write an analysis report

with open("sample_text.txt") as f:
    content = f.read()

lines = content.splitlines()
word_count = len(content.split())
char_count = len(content)

report_lines = [
    "=== Text analysis report ===",
    f"Source file: sample_text.txt",
    f"Lines:      {len(lines)}",
    f"Words:      {word_count}",
    f"Characters: {char_count}",
    "",
    "=== Word count per line ===",
]

for i, line in enumerate(lines, start=1):
    words = line.split()
    report_lines.append(f"  Line {i}: {len(words):>2} words")

report_lines.append("")
report_lines.append("=== End of report ===")

with open("report.txt", "w") as f:
    for line in report_lines:
        f.write(line + "\n")

print(f"Report written to report.txt ({len(report_lines)} lines)")

print()
print("--- Verifying report.txt ---")
with open("report.txt") as f:
    print(f.read())
```

### Exercise 3.2.3: logger.py

```python
# logger.py - Append log entries to a file

from datetime import datetime


def log_event(message, log_file="app.log"):
    """Append a timestamped message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(log_file, "a") as f:
        f.write(entry)
    print(f"  Logged: {entry.strip()}")


print("=== Logging events ===")
log_event("Application started")
log_event("User 'alice' logged in")
log_event("File 'data.csv' loaded (150 rows)")
log_event("Processing complete")
log_event("Application stopped")

print()
print("=== Full log contents ===")
with open("app.log") as f:
    print(f.read())
```

### Exercise 3.2.4: csv_processor.py

```python
# csv_processor.py - Process a CSV file and write a summary

import csv


def read_sales_data(filename):
    """Read sales data from a CSV file and return a list of dictionaries."""
    products = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "product": row["product"],
                "category": row["category"],
                "price": float(row["price"]),
                "quantity": int(row["quantity"]),
            })
    return products


def calculate_category_totals(products):
    """Calculate revenue totals grouped by category."""
    totals = {}
    for product in products:
        category = product["category"]
        revenue = product["price"] * product["quantity"]
        if category in totals:
            totals[category]["revenue"] += revenue
            totals[category]["items"] += product["quantity"]
            totals[category]["product_count"] += 1
        else:
            totals[category] = {
                "revenue": revenue,
                "items": product["quantity"],
                "product_count": 1,
            }
    return totals


def write_summary_csv(totals, filename):
    """Write category summary to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "products", "total_items", "total_revenue"])
        for category, data in sorted(totals.items()):
            writer.writerow([
                category,
                data["product_count"],
                data["items"],
                f"{data['revenue']:.2f}",
            ])


products = read_sales_data("sales_data.csv")
print(f"Loaded {len(products)} products")
print()

print("=== All products ===")
for p in products:
    revenue = p["price"] * p["quantity"]
    print(f"  {p['product']:<20} {p['category']:<15} ${revenue:>10,.2f}")

print()

totals = calculate_category_totals(products)

print("=== Category summary ===")
grand_total = 0
for category, data in sorted(totals.items()):
    print(f"  {category}:")
    print(f"    Products: {data['product_count']}")
    print(f"    Items sold: {data['items']}")
    print(f"    Revenue: ${data['revenue']:,.2f}")
    grand_total += data["revenue"]

print(f"\n  Grand total: ${grand_total:,.2f}")

write_summary_csv(totals, "category_summary.csv")
print(f"\nSummary written to category_summary.csv")

print()
print("=== Verifying category_summary.csv ===")
with open("category_summary.csv") as f:
    print(f.read())
```
