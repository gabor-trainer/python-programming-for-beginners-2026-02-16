# Lab 3.3: Exploring modules and the standard library

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Import modules using `import` and `from ... import`
- Use `random` to generate random numbers, make random choices, and shuffle data
- Use `datetime` to work with dates, compute differences, and format date strings
- Use `pathlib` to inspect files and list directory contents
- Create your own module and import it into a separate script

---

## 3. Prerequisites

**Knowledge prerequisites**: Functions (Chapter 3.1), file I/O (Chapter 3.2). Chapter 3.3 presentation completed.

**Previous labs**: Lab 3.2 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Navigate to your working directory: `cd C:\labs`
- [ ] Verify the REPL works: `python` → `>>> import math; print(math.pi)` → `exit()`

**Important**: Make sure you do **not** have any files named `random.py`, `datetime.py`, `math.py`, or `pathlib.py` in `C:\labs`. Such files would shadow the standard library modules and cause `ImportError` or `AttributeError`.

---

## 5. Concept overview

Python's standard library is often called "batteries included" — it ships with over 200 modules that handle common tasks without installing anything extra. Knowing what is available (and how to import it) saves you from writing code that already exists.

In this lab, you will work with four frequently used standard library modules: `random` for generating random data (useful in simulations, testing, and games), `datetime` for date and time calculations (scheduling, age computation, timestamps), `pathlib` for file system exploration (listing files, checking paths), and `math` for mathematical operations. You will also create your own module — a `.py` file containing utility functions — and import it into a main script, experiencing the workflow of organising code across multiple files.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Simulate dice rolls and card drawing with `random`
- Compute date differences and format dates with `datetime`
- Explore directory contents and file properties with `pathlib`
- Create your own utility module and import it into a main script

---

### Exercise 3.3.1: Simulate dice and cards with `random`

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Use `random.randint()`, `random.choice()`, `random.shuffle()`, and `random.sample()` to generate random data.

**Scenario**: You are building a simple game simulator. You need to roll dice, draw cards from a deck, and pick random lottery numbers.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `random_games.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# random_games.py - Simulate games with the random module

import random

# --- Dice rolling ---
print("=== Dice simulator ===")
for i in range(1, 6):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"  Roll {i}: {die1} + {die2} = {total}")

print()

# --- Card drawing ---
print("=== Card draw ===")
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

# Build a full deck
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
print(f"  Deck size: {len(deck)} cards")

# Shuffle the deck
random.shuffle(deck)

# Draw a hand of 5 cards
hand = deck[:5]
print(f"  Your hand:")
for card in hand:
    print(f"    {card}")

print()

# --- Random selection ---
print("=== Random selections ===")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
print(f"  Random color: {random.choice(colors)}")
print(f"  Three random colors: {random.sample(colors, 3)}")

print()

# --- Lottery numbers ---
print("=== Lottery draw ===")
numbers = random.sample(range(1, 50), 6)
print(f"  Numbers: {sorted(numbers)}")

print()

# --- Dice statistics ---
print("=== Dice statistics (1000 rolls) ===")
rolls = [random.randint(1, 6) for _ in range(1000)]
for face in range(1, 7):
    count = rolls.count(face)
    bar = "#" * (count // 5)
    print(f"  {face}: {count:>3} times  {bar}")
```

3. Run the script:

```
C:\labs> python random_games.py
```

4. Run it again — the output will differ because the values are random.

**Expected output**: Five dice roll results, a hand of 5 cards from a shuffled 52-card deck, random colour selections, 6 sorted lottery numbers from 1-49, and a frequency distribution of 1000 dice rolls. Each face should appear roughly 160-170 times (1000 / 6 ≈ 167).

**Verification**: The deck has 52 cards. Each die roll is between 1 and 6. The lottery numbers are between 1 and 49 with no duplicates. The dice statistics show all six faces with similar counts.

**Try it yourself**:
- Add a coin flip simulator that flips 100 times and counts heads vs tails.
- Modify the lottery to draw 5 numbers from 1-90 (Hungarian Ötös Lottó format).

---

### Exercise 3.3.2: Work with dates and times using `datetime`

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Create dates, calculate differences, format dates as strings, and parse date strings.

**Scenario**: You are building a project management tool that needs to calculate deadlines, display formatted dates, and determine how many days remain until key dates.

**Tasks**:

1. In VS Code, create a new file. Save it as `date_tools.py` in `C:\labs`.

2. Type the following code:

```python
# date_tools.py - Work with dates and times

from datetime import datetime, date, timedelta


def days_until(target_date):
    """Calculate the number of days from today until a target date."""
    today = date.today()
    delta = target_date - today
    return delta.days


def format_date(d, style="iso"):
    """Format a date in different styles."""
    formats = {
        "iso": "%Y-%m-%d",
        "european": "%d/%m/%Y",
        "long": "%B %d, %Y",
        "short": "%d %b %Y",
    }
    fmt = formats.get(style, formats["iso"])
    return d.strftime(fmt)


# --- Current date and time ---
print("=== Current date and time ===")
now = datetime.now()
print(f"  Now:        {now}")
print(f"  Date:       {now.date()}")
print(f"  Time:       {now.strftime('%H:%M:%S')}")
print(f"  Year:       {now.year}")
print(f"  Month:      {now.month}")
print(f"  Day:        {now.day}")
print()

# --- Date formatting ---
print("=== Date formats ===")
today = date.today()
for style in ["iso", "european", "long", "short"]:
    print(f"  {style:<10}: {format_date(today, style)}")
print()

# --- Date arithmetic ---
print("=== Date arithmetic ===")
deadline = today + timedelta(days=30)
last_week = today - timedelta(days=7)
next_quarter = today + timedelta(weeks=13)
print(f"  Today:         {today}")
print(f"  30 days out:   {deadline}")
print(f"  7 days ago:    {last_week}")
print(f"  Next quarter:  {next_quarter}")
print()

# --- Days until important dates ---
print("=== Days until... ===")
events = [
    ("New Year 2027", date(2027, 1, 1)),
    ("Summer solstice", date(2026, 6, 21)),
    ("End of year", date(2026, 12, 31)),
]
for name, event_date in events:
    days = days_until(event_date)
    if days > 0:
        print(f"  {name}: {days} days away")
    elif days == 0:
        print(f"  {name}: TODAY!")
    else:
        print(f"  {name}: {abs(days)} days ago")
print()

# --- Parse a date string ---
print("=== Parsing date strings ===")
date_strings = ["2026-03-15", "2026-12-25", "2026-07-04"]
for ds in date_strings:
    parsed = datetime.strptime(ds, "%Y-%m-%d").date()
    formatted = format_date(parsed, "long")
    days = days_until(parsed)
    print(f"  {ds} → {formatted} ({days} days away)")
```

3. Run the script:

```
C:\labs> python date_tools.py
```

**Expected output**: Current date/time, the date in four formats, date arithmetic results, countdowns to future dates, and parsed date strings with day counts. The exact numbers depend on when you run the script.

**Verification**: The "30 days out" date should be exactly 30 days after today. Parsed dates should match the original strings. Negative "days away" values indicate past dates.

**Try it yourself**:
- Add a function that takes a birthdate and returns the person's age in years and days.
- Add a "working days until" function that excludes weekends (hint: check `d.weekday()` — 5 and 6 are Saturday and Sunday).

---

### Exercise 3.3.3: Explore files with `pathlib`

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use `pathlib.Path` to navigate the file system, list files, and inspect file properties.

**Scenario**: You need to write a script that surveys the files in a directory — what types they are, how large, and when they were last modified. This is useful for cleanup scripts, backup tools, and project inventory.

**Tasks**:

1. First, create a few test files so there is something to inspect. In a terminal:

```
C:\labs> echo "Test file 1" > test_a.txt
C:\labs> echo "Test file 2 with more content" > test_b.txt
C:\labs> echo "print('hello')" > test_script.py
```

2. In VS Code, create a new file. Save it as `dir_explorer.py` in `C:\labs`.

3. Type the following code:

```python
# dir_explorer.py - Explore directory contents with pathlib

from pathlib import Path
from datetime import datetime


def format_size(size_bytes):
    """Format a file size in human-readable form."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


# --- Explore the current directory ---
current = Path(".")
print(f"=== Directory: {current.resolve()} ===")
print()

# List all files (not directories)
files = [p for p in current.iterdir() if p.is_file()]
dirs = [p for p in current.iterdir() if p.is_dir()]

print(f"  Files: {len(files)}")
print(f"  Directories: {len(dirs)}")
print()

# --- File details ---
print("=== File details ===")
print(f"  {'Name':<30} {'Size':>10} {'Extension':>10}  {'Modified'}")
print(f"  {'-'*30} {'-'*10} {'-'*10}  {'-'*19}")

for f in sorted(files, key=lambda p: p.name):
    stat = f.stat()
    size = format_size(stat.st_size)
    ext = f.suffix if f.suffix else "(none)"
    modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    print(f"  {f.name:<30} {size:>10} {ext:>10}  {modified}")

print()

# --- Group files by extension ---
print("=== Files grouped by extension ===")
extensions = {}
for f in files:
    ext = f.suffix if f.suffix else "(no extension)"
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(f.name)

for ext, names in sorted(extensions.items()):
    print(f"  {ext}: {len(names)} file(s)")
    for name in sorted(names):
        print(f"    {name}")

print()

# --- Path manipulation ---
print("=== Path manipulation ===")
example = Path("C:/labs/data/reports/summary.csv")
print(f"  Full path:  {example}")
print(f"  Name:       {example.name}")
print(f"  Stem:       {example.stem}")
print(f"  Suffix:     {example.suffix}")
print(f"  Parent:     {example.parent}")
print(f"  Parts:      {example.parts}")

# Building paths with /
base = Path("C:/projects")
project = base / "my_app" / "src" / "main.py"
print(f"\n  Built path: {project}")

# --- Find specific files ---
print()
print("=== Python files in current directory ===")
py_files = list(current.glob("*.py"))
if py_files:
    for pf in sorted(py_files):
        print(f"  {pf.name}")
else:
    print("  (no .py files found)")
```

4. Run the script:

```
C:\labs> python dir_explorer.py
```

**Expected output**: A summary of the current directory showing file count and directory count, a detailed listing of each file with size/extension/modification date, files grouped by extension, path manipulation examples, and a list of Python files.

**Verification**: The file count matches what you see in the directory. The path manipulation example correctly splits `C:/labs/data/reports/summary.csv` into its components.

**Try it yourself**:
- Modify the script to calculate the total size of all files in the directory.
- Add a search for files larger than a given threshold (e.g., 1 KB).

---

### Exercise 3.3.4: Create and import your own module

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Create a module with utility functions and import it into a main script.

**Scenario**: You have written useful helper functions across several labs. Now you want to organise them into a module so any script can reuse them.

**Tasks**:

1. In VS Code, create a new file. Save it as `text_utils.py` in `C:\labs`.

2. Type the following code — this is your **module** file:

```python
# text_utils.py - Text utility functions (module)

def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())


def count_characters(text, include_spaces=True):
    """Count characters. Optionally exclude spaces."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def truncate(text, max_length=50, suffix="..."):
    """Shorten text to max_length, adding suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def title_case(text):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


def extract_initials(full_name):
    """Extract initials from a full name."""
    parts = full_name.split()
    return "".join(part[0].upper() for part in parts if part)


# This code runs only when text_utils.py is executed directly
if __name__ == "__main__":
    print("Testing text_utils module:")
    print(f"  count_words('hello world'): {count_words('hello world')}")
    print(f"  count_characters('hello', spaces=False): "
          f"{count_characters('hello', include_spaces=False)}")
    print(f"  truncate('A very long sentence here', 15): "
          f"{truncate('A very long sentence here', 15)}")
    print(f"  title_case('hello world'): {title_case('hello world')}")
    print(f"  extract_initials('John Michael Doe'): "
          f"{extract_initials('John Michael Doe')}")
```

3. Run the module directly to test it:

```
C:\labs> python text_utils.py
```

You should see the test output.

4. Now create a **main script** that imports this module. Create a new file and save it as `main_app.py` in `C:\labs`:

```python
# main_app.py - Use the text_utils module

import text_utils

# Sample data
articles = [
    "Python is a versatile programming language used worldwide.",
    "The standard library includes modules for file I/O, math, dates, and more.",
    "Learning to write functions and organize code into modules is essential.",
    "This training covers Python fundamentals over four days of hands-on practice.",
    "Error handling with try and except makes your programs robust and reliable.",
]

print("=== Article summary ===\n")
for i, article in enumerate(articles, start=1):
    words = text_utils.count_words(article)
    chars = text_utils.count_characters(article, include_spaces=False)
    short = text_utils.truncate(article, max_length=40)
    print(f"  Article {i}:")
    print(f"    Full:      {article}")
    print(f"    Truncated: {short}")
    print(f"    Words: {words}, Characters (no spaces): {chars}")
    print()

# Use from ... import for convenience
from text_utils import title_case, extract_initials

print("=== Name formatting ===\n")
names = ["alice johnson", "bob martinez", "charlie van der berg"]
for name in names:
    titled = title_case(name)
    initials = extract_initials(name)
    print(f"  {name:<30} → {titled:<30} ({initials})")
```

5. Run the main script:

```
C:\labs> python main_app.py
```

6. Notice that when `main_app.py` imports `text_utils`, the test code at the bottom of `text_utils.py` does **not** run. The `if __name__ == "__main__":` guard prevents it.

**Expected output**: Article summaries with word counts, character counts, and truncated previews. Name formatting showing original, title-cased, and initials for each name.

**Verification**: The import works without errors. The `text_utils.py` test output does **not** appear when running `main_app.py`. Both `import text_utils` and `from text_utils import ...` styles work.

---

## 7. Validation checklist

- [ ] Exercise 3.3.1: `random_games.py` produces random dice rolls, card hands, and lottery numbers
- [ ] Exercise 3.3.2: `date_tools.py` displays formatted dates, arithmetic results, and countdowns
- [ ] Exercise 3.3.3: `dir_explorer.py` lists files with sizes and extensions, groups by extension
- [ ] Exercise 3.3.4: `text_utils.py` works as a standalone script AND as an imported module in `main_app.py`

```
C:\labs> python random_games.py
# Random dice, cards, lottery, and statistics (output varies each run)

C:\labs> python date_tools.py
# Formatted dates, arithmetic, countdowns (numbers depend on today's date)

C:\labs> python dir_explorer.py
# File listing with sizes, extensions, and grouped view

C:\labs> python text_utils.py
# Test output from __name__ == "__main__" block

C:\labs> python main_app.py
# Article summaries and name formatting (no text_utils test output)
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'text_utils'` | Python cannot find `text_utils.py` | Ensure both files are in the same directory (`C:\labs`) |
| `AttributeError: module 'random' has no attribute 'randint'` | A file named `random.py` exists in the directory | Rename or delete your `random.py` file |
| `ImportError: cannot import name 'x' from 'module'` | The function name does not exist in the module | Check spelling, verify the function is defined in the module |
| `TypeError: 'str' object is not callable` | Variable name shadows a function name | Check for variables named `date`, `path`, `format`, etc. |

**Common beginner pitfalls:**
- Naming your file `random.py`, `datetime.py`, `math.py`, or `pathlib.py` — this shadows the standard library
- Forgetting to save the module file before importing it — Python imports the old version
- Running the script from a different directory than where the module is — Python cannot find it
- Confusing `datetime.datetime` (class) with `datetime` (module) — use `from datetime import datetime` to clarify

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`

---

## 9. Questions

1. You have a file called `math.py` in your project directory that contains your own helper functions. When you run `import math` followed by `math.sqrt(16)`, you get an `AttributeError`. Explain why this happens and how to fix it.

2. Compare `import datetime` with `from datetime import datetime`. What does each give you access to, and when would you prefer one form over the other?

3. Why does the `if __name__ == "__main__":` pattern exist? What problem does it solve? Could you achieve the same result without it?

4. Your script uses `random.randint()` to generate test data, but your tests produce different results every time you run them. A colleague says this makes testing unreliable. How can you use `random` while still getting reproducible results for testing?

5. You need to write a script that processes files from a directory. Compare using string paths (`"C:\\labs\\data\\file.txt"`) with `pathlib.Path("C:/labs/data") / "file.txt"`. What practical advantages does `pathlib` offer?

6. Your project has grown to include `utils.py`, `validators.py`, and `formatters.py`. The main script imports all three. A colleague suggests combining them into a single `helpers.py` file. Discuss the trade-offs of many small modules versus one large module.

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del random_games.py
C:\labs> del date_tools.py
C:\labs> del dir_explorer.py
C:\labs> del text_utils.py
C:\labs> del main_app.py
C:\labs> del test_a.txt test_b.txt test_script.py
```

Verify your working directory is clean:

```
C:\labs> dir *.py *.txt
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- `import module` loads the entire module; access with `module.name`. `from module import name` imports specific names directly.
- `random` provides `randint()`, `choice()`, `shuffle()`, and `sample()` for random data generation
- `datetime` handles dates, times, and arithmetic — subtract two dates to get a `timedelta`
- `pathlib.Path` is the modern way to work with file paths — use the `/` operator to build paths
- Any `.py` file is a module — create your own and import them into other scripts
- Use `if __name__ == "__main__":` to include test code that only runs when executing the module directly
- Never name your files after standard library modules (`random.py`, `datetime.py`, etc.)

---

## 12. Additional resources

- Python `random` module: https://docs.python.org/3/library/random.html
- Python `datetime` module: https://docs.python.org/3/library/datetime.html
- Python `pathlib` module: https://docs.python.org/3/library/pathlib.html
- Python Tutorial — Modules: https://docs.python.org/3/tutorial/modules.html
- `strftime`/`strptime` format codes: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

---

## 13. Appendices

### Appendix A: Quick reference — key module imports

```python
import random
random.randint(1, 6)          # Random int in [1, 6]
random.choice(["a", "b"])     # Random pick from list
random.shuffle(my_list)       # Shuffle in place
random.sample(range(1, 50), 5)  # 5 unique picks

from datetime import datetime, date, timedelta
now = datetime.now()
today = date.today()
delta = date(2027, 1, 1) - today
future = today + timedelta(days=30)
now.strftime("%Y-%m-%d %H:%M")
datetime.strptime("2026-03-15", "%Y-%m-%d")

from pathlib import Path
p = Path("C:/labs")
p.exists()
p.is_file()
p.glob("*.py")
p / "subdir" / "file.txt"
```

### Appendix B: Common `strftime` format codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | `2026` |
| `%m` | Month (01–12) | `02` |
| `%d` | Day (01–31) | `09` |
| `%H` | Hour 24h (00–23) | `14` |
| `%M` | Minute (00–59) | `35` |
| `%S` | Second (00–59) | `07` |
| `%B` | Full month name | `February` |
| `%b` | Abbreviated month | `Feb` |
| `%A` | Full weekday name | `Monday` |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

When you have a file called `math.py` in your project directory, `import math` imports **your** file instead of Python's standard library `math` module. Python searches the current directory before the standard library, so your local `math.py` takes priority. Since your file does not contain a `sqrt` function, `math.sqrt(16)` raises an `AttributeError`.

The fix is to rename your file to something that does not collide with a standard library module — for example, `math_helpers.py` or `my_math.py`. This is a common trap for beginners because Python does not warn you about the shadowing. The same problem occurs with `random.py`, `datetime.py`, `csv.py`, and any other standard library module name.

**Answer 2:**

`import datetime` makes the entire `datetime` module available. You access its contents with dot notation: `datetime.datetime.now()`, `datetime.date.today()`, `datetime.timedelta(days=7)`. The module name and the class name are both `datetime`, which creates some visual redundancy.

`from datetime import datetime` imports the `datetime` class directly into your namespace. You can write `datetime.now()` instead of `datetime.datetime.now()`. This is shorter but means you can no longer access other members of the module (like `date` or `timedelta`) unless you import them too: `from datetime import datetime, date, timedelta`.

Prefer `from datetime import datetime, date, timedelta` when you use these classes frequently — it is more readable. Use `import datetime` when you want to make it clear that `datetime` refers to the module, not a local variable or class, or when you use many different items from the module and want the namespace to prevent collisions.

**Answer 3:**

The `if __name__ == "__main__":` pattern lets a `.py` file serve two roles: as a standalone script and as an importable module. When Python runs a file directly, it sets `__name__` to `"__main__"`. When it imports the file, `__name__` is set to the module's name (e.g., `"text_utils"`).

Without this pattern, any code at the module level (outside functions) runs during import. If your module has test code or a demo at the bottom, importing it in another script would execute that code — printing output, asking for input, or modifying files. The guard prevents this, allowing you to include test code that only runs when you execute the module directly for testing.

You could achieve a similar result by putting all test code in a separate file, but the `__name__` pattern is simpler and keeps tests close to the code they test. It is a standard Python convention that every developer expects to see.

**Answer 4:**

Use `random.seed()` to set a fixed starting point for the random number generator. When you call `random.seed(42)` (or any fixed number) before generating random values, the sequence of values is identical every time:

```python
random.seed(42)
print(random.randint(1, 100))  # Always the same value
```

For testing, set the seed at the beginning of your test. For production code, do not set the seed (or use `random.seed()` without arguments, which uses the current time). This gives you reproducibility when you need it and true randomness when you do not. Many testing frameworks and data science libraries use this approach to make experiments repeatable.

**Answer 5:**

String paths require careful handling of backslashes on Windows (`"C:\\labs\\data"` or `r"C:\labs\data"`). Forgetting to escape backslashes leads to subtle bugs (`\n` becomes a newline). Concatenating paths with `+` is error-prone — you might forget the separator or accidentally double it.

`pathlib.Path` objects handle separators automatically. The `/` operator joins paths correctly on any operating system. `Path` also provides methods like `.exists()`, `.is_file()`, `.glob()`, `.name`, `.suffix`, `.parent` — all of which would require separate `os.path` function calls with string paths. The code is shorter, more readable, and less likely to have platform-specific bugs. The only trade-off is a slight learning curve, but once you know the `Path` API, it consistently saves time and prevents errors.

**Answer 6:**

Many small modules provide clear separation of concerns. Each module has a focused purpose (`validators.py` validates, `formatters.py` formats), making it easy to find code and change one area without affecting others. It also limits the scope of imports — a script that only needs validation imports only `validators`.

A single large module is simpler to manage in terms of files. There is no risk of circular imports, and new developers see all the helpers in one place. But as the file grows beyond a few hundred lines, navigating it becomes harder, and merge conflicts in version control become more frequent when multiple people edit the same file.

The general guideline: if your modules are small (under 100 lines each) and closely related, combining them is reasonable. If they serve genuinely different purposes or are edited by different people, keep them separate. You can always split later if a single module grows unwieldy.

---

## 15. Code solutions

### Exercise 3.3.1: random_games.py

```python
# random_games.py - Simulate games with the random module

import random

print("=== Dice simulator ===")
for i in range(1, 6):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"  Roll {i}: {die1} + {die2} = {total}")

print()

print("=== Card draw ===")
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
print(f"  Deck size: {len(deck)} cards")

random.shuffle(deck)

hand = deck[:5]
print(f"  Your hand:")
for card in hand:
    print(f"    {card}")

print()

print("=== Random selections ===")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
print(f"  Random color: {random.choice(colors)}")
print(f"  Three random colors: {random.sample(colors, 3)}")

print()

print("=== Lottery draw ===")
numbers = random.sample(range(1, 50), 6)
print(f"  Numbers: {sorted(numbers)}")

print()

print("=== Dice statistics (1000 rolls) ===")
rolls = [random.randint(1, 6) for _ in range(1000)]
for face in range(1, 7):
    count = rolls.count(face)
    bar = "#" * (count // 5)
    print(f"  {face}: {count:>3} times  {bar}")
```

### Exercise 3.3.2: date_tools.py

```python
# date_tools.py - Work with dates and times

from datetime import datetime, date, timedelta


def days_until(target_date):
    """Calculate the number of days from today until a target date."""
    today = date.today()
    delta = target_date - today
    return delta.days


def format_date(d, style="iso"):
    """Format a date in different styles."""
    formats = {
        "iso": "%Y-%m-%d",
        "european": "%d/%m/%Y",
        "long": "%B %d, %Y",
        "short": "%d %b %Y",
    }
    fmt = formats.get(style, formats["iso"])
    return d.strftime(fmt)


print("=== Current date and time ===")
now = datetime.now()
print(f"  Now:        {now}")
print(f"  Date:       {now.date()}")
print(f"  Time:       {now.strftime('%H:%M:%S')}")
print(f"  Year:       {now.year}")
print(f"  Month:      {now.month}")
print(f"  Day:        {now.day}")
print()

print("=== Date formats ===")
today = date.today()
for style in ["iso", "european", "long", "short"]:
    print(f"  {style:<10}: {format_date(today, style)}")
print()

print("=== Date arithmetic ===")
deadline = today + timedelta(days=30)
last_week = today - timedelta(days=7)
next_quarter = today + timedelta(weeks=13)
print(f"  Today:         {today}")
print(f"  30 days out:   {deadline}")
print(f"  7 days ago:    {last_week}")
print(f"  Next quarter:  {next_quarter}")
print()

print("=== Days until... ===")
events = [
    ("New Year 2027", date(2027, 1, 1)),
    ("Summer solstice", date(2026, 6, 21)),
    ("End of year", date(2026, 12, 31)),
]
for name, event_date in events:
    days = days_until(event_date)
    if days > 0:
        print(f"  {name}: {days} days away")
    elif days == 0:
        print(f"  {name}: TODAY!")
    else:
        print(f"  {name}: {abs(days)} days ago")
print()

print("=== Parsing date strings ===")
date_strings = ["2026-03-15", "2026-12-25", "2026-07-04"]
for ds in date_strings:
    parsed = datetime.strptime(ds, "%Y-%m-%d").date()
    formatted = format_date(parsed, "long")
    days = days_until(parsed)
    print(f"  {ds} → {formatted} ({days} days away)")
```

### Exercise 3.3.3: dir_explorer.py

```python
# dir_explorer.py - Explore directory contents with pathlib

from pathlib import Path
from datetime import datetime


def format_size(size_bytes):
    """Format a file size in human-readable form."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


current = Path(".")
print(f"=== Directory: {current.resolve()} ===")
print()

files = [p for p in current.iterdir() if p.is_file()]
dirs = [p for p in current.iterdir() if p.is_dir()]

print(f"  Files: {len(files)}")
print(f"  Directories: {len(dirs)}")
print()

print("=== File details ===")
print(f"  {'Name':<30} {'Size':>10} {'Extension':>10}  {'Modified'}")
print(f"  {'-'*30} {'-'*10} {'-'*10}  {'-'*19}")

for f in sorted(files, key=lambda p: p.name):
    stat = f.stat()
    size = format_size(stat.st_size)
    ext = f.suffix if f.suffix else "(none)"
    modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    print(f"  {f.name:<30} {size:>10} {ext:>10}  {modified}")

print()

print("=== Files grouped by extension ===")
extensions = {}
for f in files:
    ext = f.suffix if f.suffix else "(no extension)"
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(f.name)

for ext, names in sorted(extensions.items()):
    print(f"  {ext}: {len(names)} file(s)")
    for name in sorted(names):
        print(f"    {name}")

print()

print("=== Path manipulation ===")
example = Path("C:/labs/data/reports/summary.csv")
print(f"  Full path:  {example}")
print(f"  Name:       {example.name}")
print(f"  Stem:       {example.stem}")
print(f"  Suffix:     {example.suffix}")
print(f"  Parent:     {example.parent}")
print(f"  Parts:      {example.parts}")

base = Path("C:/projects")
project = base / "my_app" / "src" / "main.py"
print(f"\n  Built path: {project}")

print()
print("=== Python files in current directory ===")
py_files = list(current.glob("*.py"))
if py_files:
    for pf in sorted(py_files):
        print(f"  {pf.name}")
else:
    print("  (no .py files found)")
```

### Exercise 3.3.4: text_utils.py

```python
# text_utils.py - Text utility functions (module)

def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())


def count_characters(text, include_spaces=True):
    """Count characters. Optionally exclude spaces."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def truncate(text, max_length=50, suffix="..."):
    """Shorten text to max_length, adding suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def title_case(text):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


def extract_initials(full_name):
    """Extract initials from a full name."""
    parts = full_name.split()
    return "".join(part[0].upper() for part in parts if part)


if __name__ == "__main__":
    print("Testing text_utils module:")
    print(f"  count_words('hello world'): {count_words('hello world')}")
    print(f"  count_characters('hello', spaces=False): "
          f"{count_characters('hello', include_spaces=False)}")
    print(f"  truncate('A very long sentence here', 15): "
          f"{truncate('A very long sentence here', 15)}")
    print(f"  title_case('hello world'): {title_case('hello world')}")
    print(f"  extract_initials('John Michael Doe'): "
          f"{extract_initials('John Michael Doe')}")
```

### Exercise 3.3.4: main_app.py

```python
# main_app.py - Use the text_utils module

import text_utils

articles = [
    "Python is a versatile programming language used worldwide.",
    "The standard library includes modules for file I/O, math, dates, and more.",
    "Learning to write functions and organize code into modules is essential.",
    "This training covers Python fundamentals over four days of hands-on practice.",
    "Error handling with try and except makes your programs robust and reliable.",
]

print("=== Article summary ===\n")
for i, article in enumerate(articles, start=1):
    words = text_utils.count_words(article)
    chars = text_utils.count_characters(article, include_spaces=False)
    short = text_utils.truncate(article, max_length=40)
    print(f"  Article {i}:")
    print(f"    Full:      {article}")
    print(f"    Truncated: {short}")
    print(f"    Words: {words}, Characters (no spaces): {chars}")
    print()

from text_utils import title_case, extract_initials

print("=== Name formatting ===\n")
names = ["alice johnson", "bob martinez", "charlie van der berg"]
for name in names:
    titled = title_case(name)
    initials = extract_initials(name)
    print(f"  {name:<30} → {titled:<30} ({initials})")
```
