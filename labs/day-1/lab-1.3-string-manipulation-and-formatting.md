# Lab 1.3: String manipulation and formatting

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Access individual characters and extract substrings using indexing and slicing
- Apply string methods to clean, transform, and analyze text
- Validate user input by checking string content
- Build formatted output using f-strings with alignment and precision
- Handle escape characters and multi-line strings

---

## 3. Prerequisites

**Knowledge prerequisites**: Variables, data types, `input()`, `print()`, f-strings basics (Chapter 1.2).

**Previous labs**: Lab 1.2 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Navigate to your working directory: `cd C:\labs`
- [ ] Verify the REPL works: `python` -> `>>> "test"[0]` should return `'t'` -> `exit()`

No additional setup is required for this lab.

---

## 5. Concept overview

Strings are the most commonly manipulated data type in real-world programming. Whether you are processing log files, cleaning user input, generating reports, or parsing data from a web API — string operations are everywhere.

Python strings are **sequences of characters**. This means each character has a position (index), and you can extract portions (slices). Python also provides dozens of built-in methods that handle common text operations: changing case, removing whitespace, splitting text into parts, searching for patterns, and replacing content.

In this lab, you will work through practical scenarios: parsing names and emails, validating input, extracting data from structured text, and building a formatted report. These are tasks you will encounter repeatedly in any Python project.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Extract and rearrange parts of strings using indexing and slicing
- Clean and validate user input with string methods
- Parse structured text data and extract meaningful fields
- Build a formatted report with aligned columns using f-strings

---

### Exercise 1.3.1: Indexing and slicing in the REPL

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Practice accessing characters and extracting substrings.

**Scenario**: You receive data where specific characters or portions carry meaning (for example, a product code where the first two characters indicate the category).

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Create a string and explore indexing:

```python
>>> product_code = "EL-2024-0057"
>>> product_code[0]
'E'
>>> product_code[1]
'L'
>>> product_code[-1]
'7'
>>> product_code[-4]
'0'
```

3. Extract meaningful parts using slicing:

```python
>>> category = product_code[:2]
>>> category
'EL'
>>> year = product_code[3:7]
>>> year
'2024'
>>> serial = product_code[8:]
>>> serial
'0057'
>>> print(f"Category: {category}, Year: {year}, Serial: {serial}")
Category: EL, Year: 2024, Serial: 0057
```

4. Try slicing with a step:

```python
>>> text = "abcdefghij"
>>> text[::2]
'acegi'
>>> text[1::2]
'bdfhj'
>>> text[::-1]
'jihgfedcba'
```

5. Find the length of a string:

```python
>>> message = "Hello, World!"
>>> len(message)
13
```

6. Try to modify a character (observe the error):

```python
>>> word = "Python"
>>> word[0] = "J"
```

You will see a `TypeError`. Strings are immutable — you cannot change individual characters.

7. Create a new string instead:

```python
>>> word = "Python"
>>> new_word = "J" + word[1:]
>>> new_word
'Jython'
```

8. Exit the REPL:

```python
>>> exit()
```

**Verification**: You can extract the category, year, and serial from the product code using slices.

**Expected output**: Each slice returns the expected substring. Negative indexing counts from the end. Attempting to assign to an index raises a `TypeError`.

**Try it yourself**:
- Given `phone = "+36-20-555-1234"`, extract the country code, area code, and number using slicing
- Reverse a string and check if it reads the same forwards and backwards (palindrome check)

---

### Exercise 1.3.2: String methods for text processing

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Use string methods to clean, transform, and analyze text.

**Scenario**: User input is often messy — extra spaces, inconsistent capitalization, mixed formats. You need to clean it before processing.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `string_methods.py` in `C:\labs`.

2. Type the following code:

```python
# string_methods.py - Exploring string methods

# Cleaning input
raw_input = "   Alice Johnson   "
cleaned = raw_input.strip()
print(f"Original:  [{raw_input}]")
print(f"Stripped:  [{cleaned}]")
print()

# Case conversion
name = "alice JOHNSON"
print(f"lower:  {name.lower()}")
print(f"upper:  {name.upper()}")
print(f"title:  {name.title()}")
print()

# Splitting and joining
csv_line = "Budapest,Hungary,1.7 million,47.4979,19.0402"
fields = csv_line.split(",")
print(f"Fields: {fields}")
print(f"City: {fields[0]}")
print(f"Country: {fields[1]}")

# Rejoin with a different separator
reformatted = " | ".join(fields)
print(f"Reformatted: {reformatted}")
print()

# Searching
email = "alice.johnson@example.com"
at_pos = email.find("@")
username = email[:at_pos]
domain = email[at_pos + 1:]
print(f"Email: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")
print()

# Replacing
text = "Python is hard. Python is confusing."
updated = text.replace("hard", "readable").replace("confusing", "clear")
print(f"Before: {text}")
print(f"After:  {updated}")
print()

# Counting
paragraph = "the cat sat on the mat and the cat saw the rat"
the_count = paragraph.count("the")
print(f"Text: {paragraph}")
print(f"'the' appears {the_count} times")
```

3. Save as `string_methods.py` in `C:\labs`.

4. Run with F5.

**Verification**: Each operation produces the expected transformation. The email is split into username and domain. The CSV line is split into a list of five fields.

**Expected output**: The stripped string has no leading/trailing spaces. Case conversions are correct. The CSV splits into a list. The email is parsed into username and domain parts. The replacement produces the modified sentence. The count reports how many times "the" appears.

**Try it yourself**:
- Add code that checks if the email ends with `.com` using `endswith()`
- Use `startswith()` to check if the product code from Exercise 1.3.1 starts with "EL"
- Try `"hello world".center(30, "-")` and observe the result

---

### Exercise 1.3.3: Input validation

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Validate user input using string methods and membership checks.

**Scenario**: You are building a registration form that collects a name, email, and phone number. Before storing the data, you must validate each field.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `validate_input.py` in `C:\labs`.

2. Type the following code:

```python
# validate_input.py - Input validation with string methods

print("=== User registration ===")
print()

name = input("Full name: ").strip()
email = input("Email address: ").strip()
phone = input("Phone number (digits only): ").strip()

print()
print("=== Validation results ===")

# Validate name: must not be empty, must contain a space (first + last)
name_valid = len(name) > 0 and " " in name
print(f"Name '{name}': {'VALID' if name_valid else 'INVALID - enter first and last name'}")

# Validate email: must contain @ and a dot after @
has_at = "@" in email
at_pos = email.find("@")
has_dot_after_at = "." in email[at_pos + 1:] if has_at else False
email_valid = has_at and has_dot_after_at and len(email) > 5
print(f"Email '{email}': {'VALID' if email_valid else 'INVALID - must contain @ and domain'}")

# Validate phone: must contain only digits, must be 7-15 characters
digits_only = phone.isdigit()
correct_length = 7 <= len(phone) <= 15
phone_valid = digits_only and correct_length
print(f"Phone '{phone}': {'VALID' if phone_valid else 'INVALID - digits only, 7-15 characters'}")

print()
all_valid = name_valid and email_valid and phone_valid
print(f"Registration: {'ACCEPTED' if all_valid else 'REJECTED - fix errors above'}")
```

3. Save as `validate_input.py` in `C:\labs`.

4. Run with F5 and test with valid data:

```
Full name: Alice Johnson
Email address: alice@example.com
Phone number (digits only): 36201234567
```

5. Run again and test with invalid data:

```
Full name: Alice
Email address: alice.example
Phone number (digits only): 123-456
```

6. Observe how the validation catches each problem.

**Verification**: Valid input passes all three checks. Invalid input identifies specific problems: missing space in name, missing `@` in email, non-digit characters in phone.

**Expected output**: Each field shows VALID or INVALID with a reason. The final line shows ACCEPTED or REJECTED.

**Hints**:
- `"@" in email` is a membership check — returns `True` if `@` exists anywhere in the string
- `phone.isdigit()` returns `True` only if every character is a digit (0-9)
- The conditional expression `'VALID' if condition else 'INVALID'` is a compact if/else

**Try it yourself**:
- Add validation for email: the username part (before @) must be at least 1 character
- Add a check that the name does not contain digits
- Allow the phone number to start with "+" (hint: check `phone[1:].isdigit()` when `phone.startswith("+")`)

---

### Exercise 1.3.4: Build a formatted report

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use f-strings with alignment, padding, and precision to build a professional-looking report.

**Scenario**: You have employee data and need to produce a clean, aligned table for a printed report.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `report.py` in `C:\labs`.

2. Type the following code:

```python
# report.py - Formatted employee report

# Employee data (name, department, salary, years)
employees = [
    ("Alice Johnson", "Engineering", 72000.00, 5),
    ("Bob Smith", "Marketing", 58500.50, 3),
    ("Carol Williams", "Engineering", 85000.00, 8),
    ("David Brown", "Sales", 62750.75, 2),
    ("Eve Davis", "Marketing", 67200.00, 6),
]

# Report header
title = "Employee report"
print(title.upper())
print("=" * 65)
print(f"{'Name':<20} {'Department':<15} {'Salary':>10} {'Years':>6}")
print("-" * 65)

# Employee rows
total_salary = 0.0
total_years = 0

for name, dept, salary, years in employees:
    print(f"{name:<20} {dept:<15} ${salary:>9,.2f} {years:>6}")
    total_salary += salary
    total_years += years

# Summary
print("-" * 65)
count = len(employees)
avg_salary = total_salary / count
avg_years = total_years / count

print(f"{'TOTAL':<20} {'':<15} ${total_salary:>9,.2f} {total_years:>6}")
print(f"{'AVERAGE':<20} {'':<15} ${avg_salary:>9,.2f} {avg_years:>6.1f}")
print("=" * 65)
print(f"Report generated for {count} employees")
```

3. Save as `report.py` in `C:\labs`.

4. Run with F5.

**Verification**: The output is a neatly aligned table with left-aligned text columns and right-aligned numeric columns. Dollar amounts show two decimal places with comma separators. The totals and averages are mathematically correct.

**Expected output**: A table with a header row, five employee rows, a separator, a TOTAL row, and an AVERAGE row. All columns are aligned. Salary values use commas as thousands separators and two decimal places. The years column is right-aligned.

**Try it yourself**:
- Add a column for "Level" (Junior/Mid/Senior) based on years: less than 3 = Junior, 3-6 = Mid, 7+ = Senior
- Add a row that shows the highest salary and the name of that employee
- Modify the report to read employee names from `input()` and store them in a list

---

## 7. Validation checklist

- [ ] You can extract characters and substrings using indexing and slicing
- [ ] You understand negative indexing (counting from the end)
- [ ] `string_methods.py` demonstrates at least six different string methods
- [ ] `validate_input.py` correctly validates name, email, and phone
- [ ] `report.py` produces a neatly aligned table with formatted numbers
- [ ] You understand that strings are immutable (cannot change individual characters)
- [ ] You can split a string into parts and join parts back together

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `IndexError: string index out of range` | Index exceeds string length | Check `len()` before indexing. Remember: indices go from 0 to len-1. |
| `TypeError: 'str' does not support item assignment` | Trying to change a character in a string | Strings are immutable. Build a new string instead. |
| `AttributeError: 'int' object has no attribute 'upper'` | Calling a string method on a non-string value | Ensure the variable holds a string. Use `str()` to convert. |
| f-string alignment looks wrong | Wrong format specifier | `<` = left, `>` = right, `^` = center. Number after specifier = width. |
| `find()` returns -1 | Substring not found | -1 is not an error; it means the text was not found. Check before slicing. |

**Common beginner pitfalls:**
- Forgetting that `strip()`, `lower()`, `replace()` etc. return new strings — they do not modify the original. You must assign the result.
- Confusing `find()` (returns index or -1) with `index()` (returns index or raises ValueError).
- Off-by-one errors in slicing: `text[0:3]` gives characters at indices 0, 1, 2 — not 3.

---

## 9. Questions

1. Strings in Python are immutable, meaning you cannot change a character in place. Explain what practical advantages immutability provides. Why might Python's designers have chosen this approach rather than making strings mutable?

2. The `split()` method without arguments splits on any whitespace and also removes empty strings from the result. Compare `"a  b  c".split()` with `"a  b  c".split(" ")`. Explain the difference and when each behavior is more useful.

3. You receive a CSV file where some fields contain extra whitespace (for example, `"  Alice  , Johnson  , 28  "`). Describe step by step how you would use string methods to clean this data into `["Alice", "Johnson", "28"]`.

4. Compare using `find()` versus the `in` operator to check whether a substring exists. What does each return, and in what scenario would you prefer one over the other?

5. You are building a report generator. The column widths need to accommodate the longest value in each column. Explain why hard-coding the width (like `{name:<20}`) can fail. How would you calculate the correct width dynamically?

6. A colleague writes `email.find("@")` to extract the domain from an email, but their code crashes for the input `"alice_at_example.com"` (no actual `@` character). Explain what goes wrong and how to make the code robust.

7. Explain the difference between a raw string (`r"C:\new"`) and a regular string (`"C:\\new"`). When would you use each, and what happens if you forget the `r` prefix for a Windows file path?

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\string_methods.py`
- `C:\labs\validate_input.py`
- `C:\labs\report.py`

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- Strings are indexed starting at 0; use `[index]` for single characters
- Negative indexing (`[-1]`) counts from the end — useful for the last character
- Slicing `[start:stop:step]` extracts substrings; the stop index is excluded
- `strip()`, `lower()`, `upper()`, `title()` clean and transform text
- `split()` and `join()` convert between strings and lists
- `find()`, `replace()`, `count()`, `startswith()`, `endswith()` search and modify
- `in` checks for substring membership: `"@" in email`
- `isdigit()`, `isalpha()`, `isalnum()` validate character content
- String methods return new strings — always assign the result
- f-strings support alignment (`<`, `>`, `^`), width, and precision (`.2f`)
- Raw strings (`r"..."`) treat backslashes as literal characters

---

## 12. Additional resources

- Python string methods reference: https://docs.python.org/3/library/stdtypes.html#string-methods
- Python f-string format specification: https://docs.python.org/3/library/string.html#formatspec
- Python tutorial on strings: https://docs.python.org/3/tutorial/introduction.html#strings
- PEP 498 — Literal string interpolation (f-strings): https://peps.python.org/pep-0498/

---

## 13. Appendices

### Appendix A: Quick reference — String methods

| Method | Description | Example |
|--------|-------------|---------|
| `strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` -> `"hi"` |
| `lower()` | Convert to lowercase | `"ABC".lower()` -> `"abc"` |
| `upper()` | Convert to uppercase | `"abc".upper()` -> `"ABC"` |
| `title()` | Capitalize each word | `"hello world".title()` -> `"Hello World"` |
| `split(sep)` | Split string into list | `"a,b,c".split(",")` -> `["a","b","c"]` |
| `join(list)` | Join list into string | `",".join(["a","b"])` -> `"a,b"` |
| `find(sub)` | Find index of substring (-1 if not found) | `"hello".find("ll")` -> `2` |
| `replace(old, new)` | Replace occurrences | `"aab".replace("a","x")` -> `"xxb"` |
| `count(sub)` | Count occurrences | `"aaba".count("a")` -> `3` |
| `startswith(s)` | Check prefix | `"hello".startswith("he")` -> `True` |
| `endswith(s)` | Check suffix | `"hello".endswith("lo")` -> `True` |
| `isdigit()` | All characters are digits | `"123".isdigit()` -> `True` |
| `isalpha()` | All characters are letters | `"abc".isalpha()` -> `True` |

### Appendix B: f-string format specifiers

| Specifier | Meaning | Example | Result |
|-----------|---------|---------|--------|
| `:<20` | Left-align, 20 chars wide | `f"{'hi':<20}"` | `"hi                  "` |
| `:>20` | Right-align, 20 chars wide | `f"{'hi':>20}"` | `"                  hi"` |
| `:^20` | Center, 20 chars wide | `f"{'hi':^20}"` | `"         hi         "` |
| `:.2f` | Float, 2 decimal places | `f"{3.1:.2f}"` | `"3.10"` |
| `:,.2f` | Float with comma separator | `f"{1234.5:,.2f}"` | `"1,234.50"` |
| `:0>5` | Pad with zeros, right-align | `f"{'42':0>5}"` | `"00042"` |

### Appendix C: Escape characters

| Sequence | Meaning |
|----------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\'` | Literal single quote |
| `\"` | Literal double quote |

---

## 14. Answers

**Answer 1:**

Immutability provides several practical advantages. First, immutable objects are safe to share. If you pass a string to a function, the function cannot accidentally modify your original string — it can only create new ones. This eliminates a class of bugs where one part of a program unexpectedly changes data used by another part.

Second, immutable strings can be used as dictionary keys and set elements, because their content never changes after creation. Mutable objects cannot be hashed reliably, so they cannot serve as keys. Third, Python can optimize memory usage by reusing identical strings (a technique called "interning"), which is only safe because strings never change.

The trade-off is that operations like building a string character by character require creating many intermediate strings, which can be slow. For those cases, Python provides `str.join()` or `io.StringIO` as efficient alternatives.

**Answer 2:**

`"a  b  c".split()` (no arguments) splits on any whitespace and removes empty strings, returning `["a", "b", "c"]`. It treats consecutive spaces as a single separator.

`"a  b  c".split(" ")` splits specifically on single space characters, returning `["a", "", "b", "", "c"]`. The double spaces produce empty strings in the result because each space is a separate split point.

The no-argument form is better for tokenizing natural text (extracting words), because it handles multiple spaces, tabs, and newlines uniformly. The explicit separator form is better when you need to preserve the structure (for example, parsing a file format where empty fields are meaningful, like CSV data with missing values).

**Answer 3:**

Start by splitting the string on commas: `fields = raw.split(",")`. This gives `["  Alice  ", " Johnson  ", " 28  "]`. Then apply `strip()` to each field to remove leading and trailing whitespace. You can do this in a loop: iterate over `fields`, call `strip()` on each element, and collect the results. The cleaned list is `["Alice", "Johnson", "28"]`.

In more advanced Python (covered on Day 4), you could write this as a list comprehension: `[field.strip() for field in raw.split(",")]`. This is a one-line solution that splits and strips in a single expression. Both approaches produce the same result; the comprehension is more concise.

**Answer 4:**

The `in` operator returns a boolean: `True` if the substring exists, `False` if not. It is ideal for simple presence checks: `if "@" in email:`. It is readable and clearly communicates intent.

`find()` returns the index (position) of the first occurrence, or `-1` if the substring is not found. It is useful when you need to know where the substring is, not just whether it exists — for example, to slice the string at that position.

Use `in` when you only need a yes/no answer. Use `find()` when you need the position for further processing. Avoid using `find()` just for presence checks, because checking `find() != -1` is less readable than `in`.

**Answer 5:**

Hard-coding the width to 20 works only if no value exceeds 20 characters. If an employee name is 25 characters long, it overflows the column and misaligns the entire table. Conversely, if the longest name is 10 characters, a width of 20 wastes space.

To calculate the correct width dynamically, iterate over all values in the column and find the longest one: `max_width = max(len(name) for name, _, _, _ in employees)`. Then use that value in the f-string: `f"{name:<{max_width}}"`. The double braces `{max_width}` inside the format specifier let you use a variable for the width. Add 2-3 characters of padding for readability.

**Answer 6:**

When `email.find("@")` does not find the `@` character, it returns `-1`. If the code then slices with `email[-1 + 1:]` (which is `email[0:]`), it returns the entire string — not the domain. The code does not crash with an error but produces incorrect output silently, which is worse than a visible crash.

To make the code robust, check the return value of `find()` before using it: `at_pos = email.find("@")`, then `if at_pos == -1: print("Invalid email")`. Only proceed with slicing if `at_pos` is a valid index. Alternatively, first check with `if "@" in email:` before calling `find()`. Defensive programming means never assuming the data is valid.

**Answer 7:**

A regular string interprets backslashes as escape sequences. `"C:\new"` contains a newline character (`\n`), not the literal text `\new`. This produces incorrect output and can be hard to debug because the path looks correct in the source code but behaves unexpectedly when used.

A raw string (`r"C:\new"`) treats every backslash as a literal character. `r"C:\new"` contains exactly the six characters `C`, `:`, `\`, `n`, `e`, `w`. This is the correct way to write Windows file paths in Python. Alternatively, you can escape each backslash (`"C:\\new"`) or use forward slashes (`"C:/new"`), which Python accepts on Windows. Raw strings are the cleanest solution for paths.

---

## 15. Code solutions

### Exercise 1.3.2: string_methods.py

```python
# string_methods.py - Exploring string methods

# Cleaning input
raw_input = "   Alice Johnson   "
cleaned = raw_input.strip()
print(f"Original:  [{raw_input}]")
print(f"Stripped:  [{cleaned}]")
print()

# Case conversion
name = "alice JOHNSON"
print(f"lower:  {name.lower()}")
print(f"upper:  {name.upper()}")
print(f"title:  {name.title()}")
print()

# Splitting and joining
csv_line = "Budapest,Hungary,1.7 million,47.4979,19.0402"
fields = csv_line.split(",")
print(f"Fields: {fields}")
print(f"City: {fields[0]}")
print(f"Country: {fields[1]}")

# Rejoin with a different separator
reformatted = " | ".join(fields)
print(f"Reformatted: {reformatted}")
print()

# Searching
email = "alice.johnson@example.com"
at_pos = email.find("@")
username = email[:at_pos]
domain = email[at_pos + 1:]
print(f"Email: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")
print()

# Replacing
text = "Python is hard. Python is confusing."
updated = text.replace("hard", "readable").replace("confusing", "clear")
print(f"Before: {text}")
print(f"After:  {updated}")
print()

# Counting
paragraph = "the cat sat on the mat and the cat saw the rat"
the_count = paragraph.count("the")
print(f"Text: {paragraph}")
print(f"'the' appears {the_count} times")
```

### Exercise 1.3.3: validate_input.py

```python
# validate_input.py - Input validation with string methods

print("=== User registration ===")
print()

name = input("Full name: ").strip()
email = input("Email address: ").strip()
phone = input("Phone number (digits only): ").strip()

print()
print("=== Validation results ===")

# Validate name: must not be empty, must contain a space (first + last)
name_valid = len(name) > 0 and " " in name
print(f"Name '{name}': {'VALID' if name_valid else 'INVALID - enter first and last name'}")

# Validate email: must contain @ and a dot after @
has_at = "@" in email
at_pos = email.find("@")
has_dot_after_at = "." in email[at_pos + 1:] if has_at else False
email_valid = has_at and has_dot_after_at and len(email) > 5
print(f"Email '{email}': {'VALID' if email_valid else 'INVALID - must contain @ and domain'}")

# Validate phone: must contain only digits, must be 7-15 characters
digits_only = phone.isdigit()
correct_length = 7 <= len(phone) <= 15
phone_valid = digits_only and correct_length
print(f"Phone '{phone}': {'VALID' if phone_valid else 'INVALID - digits only, 7-15 characters'}")

print()
all_valid = name_valid and email_valid and phone_valid
print(f"Registration: {'ACCEPTED' if all_valid else 'REJECTED - fix errors above'}")
```

### Exercise 1.3.4: report.py

```python
# report.py - Formatted employee report

# Employee data (name, department, salary, years)
employees = [
    ("Alice Johnson", "Engineering", 72000.00, 5),
    ("Bob Smith", "Marketing", 58500.50, 3),
    ("Carol Williams", "Engineering", 85000.00, 8),
    ("David Brown", "Sales", 62750.75, 2),
    ("Eve Davis", "Marketing", 67200.00, 6),
]

# Report header
title = "Employee report"
print(title.upper())
print("=" * 65)
print(f"{'Name':<20} {'Department':<15} {'Salary':>10} {'Years':>6}")
print("-" * 65)

# Employee rows
total_salary = 0.0
total_years = 0

for name, dept, salary, years in employees:
    print(f"{name:<20} {dept:<15} ${salary:>9,.2f} {years:>6}")
    total_salary += salary
    total_years += years

# Summary
print("-" * 65)
count = len(employees)
avg_salary = total_salary / count
avg_years = total_years / count

print(f"{'TOTAL':<20} {'':<15} ${total_salary:>9,.2f} {total_years:>6}")
print(f"{'AVERAGE':<20} {'':<15} ${avg_salary:>9,.2f} {avg_years:>6.1f}")
print("=" * 65)
print(f"Report generated for {count} employees")
```
