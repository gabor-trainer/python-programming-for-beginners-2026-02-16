# Python Syntax Cheat Sheet

**Quick Reference for Python 3.12+ Beginners**  
**Print-friendly format — Save or print for desk reference**

---

## Basic Syntax

### Comments
```python
# Single-line comment

"""
Multi-line comment
or docstring
"""
```

### Variables and Assignment
```python
x = 5                    # Integer
y = 3.14                 # Float
name = "Alice"           # String
is_valid = True          # Boolean
nothing = None           # None type

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0
```

### Print Output
```python
print("Hello")           # Hello
print("Hello", "World")  # Hello World
print(x, y, z)          # With variables

# f-strings (formatted strings)
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 30
```

---

## Data Types

### Numbers
```python
x = 5                    # int
y = 3.14                 # float
z = 1 + 2j               # complex

# Operations
10 + 3      # 13 (addition)
10 - 3      # 7 (subtraction)
10 * 3      # 30 (multiplication)
10 / 3      # 3.333... (division)
10 // 3     # 3 (floor division)
10 % 3      # 1 (modulus/remainder)
10 ** 3     # 1000 (exponent)
```

### Strings
```python
s = "hello"
s = 'hello'              # Single or double quotes
s = """multi
line"""                  # Triple quotes

# Operations
"hello" + "world"        # "helloworld" (concatenation)
"ha" * 3                 # "hahaha" (repetition)
len("hello")             # 5 (length)

# Indexing and slicing
s = "hello"
s[0]                     # 'h' (first character)
s[-1]                    # 'o' (last character)
s[1:4]                   # 'ell' (substring)
s[:3]                    # 'hel' (start to index 3)
s[2:]                    # 'llo' (index 2 to end)

# Methods
s.upper()                # 'HELLO'
s.lower()                # 'hello'
s.strip()                # Remove whitespace
s.split(',')             # Split into list
s.replace('l', 'L')      # 'heLLo'
s.startswith('he')       # True
s.endswith('lo')         # True
'e' in s                 # True (membership)
```

### Booleans
```python
True, False              # Boolean values

# Comparison operators
x == y                   # Equal to
x != y                   # Not equal to
x > y                    # Greater than
x < y                    # Less than
x >= y                   # Greater than or equal
x <= y                   # Less than or equal

# Logical operators
x and y                  # Both true
x or y                   # At least one true
not x                    # Opposite
```

---

## Collections

### Lists (mutable, ordered)
```python
# Creation
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
empty = []

# Access
list1[0]                 # 1 (first element)
list1[-1]                # 5 (last element)
list1[1:3]               # [2, 3] (slice)

# Methods
list1.append(6)          # Add to end
list1.insert(0, 0)       # Insert at position
list1.remove(3)          # Remove first occurrence
list1.pop()              # Remove and return last
list1.pop(0)             # Remove and return at index
list1.sort()             # Sort in place
list1.reverse()          # Reverse in place
len(list1)               # Length
2 in list1               # True if 2 exists

# List comprehension
[x * 2 for x in range(5)]  # [0, 2, 4, 6, 8]
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Tuples (immutable, ordered)
```python
# Creation
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3         # Parentheses optional
single = (1,)            # Note trailing comma

# Access (same as lists)
tuple1[0]                # 1
tuple1[1:3]              # (2, 3)

# Unpacking
x, y, z = tuple1         # x=1, y=2, z=3
```

### Dictionaries (mutable, key-value pairs)
```python
# Creation
dict1 = {'name': 'Alice', 'age': 30}
dict2 = dict(name='Bob', age=25)
empty = {}

# Access
dict1['name']            # 'Alice'
dict1.get('age')         # 30
dict1.get('city', 'Unknown')  # 'Unknown' (default)

# Modify
dict1['age'] = 31        # Update value
dict1['city'] = 'NYC'    # Add new key

# Methods
dict1.keys()             # All keys
dict1.values()           # All values
dict1.items()            # Key-value pairs
dict1.pop('age')         # Remove and return value
'name' in dict1          # True if key exists

# Dictionary comprehension
{x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### Sets (mutable, unordered, unique)
```python
# Creation
set1 = {1, 2, 3, 4, 5}
set2 = set([1, 2, 2, 3])  # {1, 2, 3} (duplicates removed)
empty = set()            # NOT {} (that's a dict)

# Operations
set1.add(6)              # Add element
set1.remove(3)           # Remove (raises error if not found)
set1.discard(3)          # Remove (no error if not found)
3 in set1                # True if exists

# Set operations
set1 | set2              # Union
set1 & set2              # Intersection
set1 - set2              # Difference
set1 ^ set2              # Symmetric difference
```

---

## Control Flow

### If Statement
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# Inline if (ternary)
result = "yes" if condition else "no"
```

### For Loop
```python
# Iterate over sequence
for item in [1, 2, 3]:
    print(item)

# Iterate with index
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)       # 0 a, 1 b, 2 c

# Iterate over range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Iterate dictionary
for key, value in dict1.items():
    print(key, value)
```

### While Loop
```python
while condition:
    # code
    break      # Exit loop
    continue   # Skip to next iteration

# Example
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## Functions

### Define Function
```python
def function_name(param1, param2):
    """Docstring describing function."""
    # code
    return result

# Call function
result = function_name(arg1, arg2)
```

### Parameters and Arguments
```python
# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Keyword arguments
greet(name="Alice", greeting="Hi")

# Variable arguments
def sum_all(*args):      # args is a tuple
    return sum(args)

def print_info(**kwargs):  # kwargs is a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call with unpacking
numbers = [1, 2, 3]
sum_all(*numbers)        # Unpack list as arguments
```

### Lambda (Anonymous Functions)
```python
# Syntax: lambda parameters: expression
square = lambda x: x ** 2
add = lambda x, y: x + y

# Used with map, filter
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]
```

---

## File I/O

### Reading Files
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### Writing Files
```python
# Write (overwrites existing)
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)
```

---

## Exception Handling

```python
try:
    # Code that might raise exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:
    # Handle multiple exceptions
    print(f"Error: {e}")
except Exception as e:
    # Catch all exceptions
    print(f"Unexpected error: {e}")
else:
    # Runs if no exception
    print("Success")
finally:
    # Always runs
    print("Cleanup")

# Raise exception
raise ValueError("Invalid value")
```

---

## Classes and Objects

### Basic Class
```python
class ClassName:
    """Class docstring."""
    
    # Class attribute (shared by all instances)
    class_variable = "shared"
    
    def __init__(self, param1, param2):
        """Constructor."""
        self.param1 = param1
        self.param2 = param2
    
    def method(self):
        """Instance method."""
        return self.param1
    
    def __str__(self):
        """String representation."""
        return f"ClassName({self.param1})"

# Create instance
obj = ClassName("value1", "value2")

# Access attributes and methods
obj.param1
obj.method()
```

### Inheritance
```python
class ParentClass:
    def __init__(self, value):
        self.value = value
    
    def method(self):
        return self.value

class ChildClass(ParentClass):
    def __init__(self, value, extra):
        super().__init__(value)  # Call parent constructor
        self.extra = extra
    
    def method(self):
        # Override parent method
        return super().method() + self.extra
```

---

## Common Built-in Functions

```python
# Type conversion
int("10")                # 10
float("3.14")            # 3.14
str(100)                 # "100"
list("abc")              # ['a', 'b', 'c']
tuple([1, 2, 3])         # (1, 2, 3)
set([1, 1, 2])           # {1, 2}

# Math
abs(-5)                  # 5
round(3.7)               # 4
min(1, 2, 3)             # 1
max(1, 2, 3)             # 3
sum([1, 2, 3])           # 6
pow(2, 3)                # 8 (2^3)

# Sequences
len([1, 2, 3])           # 3
sorted([3, 1, 2])        # [1, 2, 3]
reversed([1, 2, 3])      # Iterator
all([True, True])        # True if all true
any([False, True])       # True if any true
zip([1, 2], ['a', 'b'])  # [(1,'a'), (2,'b')]
enumerate(['a', 'b'])    # [(0,'a'), (1,'b')]

# Type checking
type(x)                  # Type of x
isinstance(x, int)       # True if x is int

# Input
name = input("Name: ")   # Read user input as string
```

---

## Common Modules

### math
```python
import math

math.pi                  # 3.14159...
math.sqrt(16)            # 4.0
math.ceil(3.2)           # 4
math.floor(3.8)          # 3
math.sin(math.pi / 2)    # 1.0
```

### random
```python
import random

random.random()          # Float between 0 and 1
random.randint(1, 10)    # Integer between 1 and 10
random.choice([1, 2, 3]) # Random element
random.shuffle(list1)    # Shuffle list in place
random.sample(list1, 3)  # 3 random elements
```

### datetime
```python
from datetime import datetime, date, timedelta

# Current date/time
datetime.now()           # Current datetime
date.today()             # Current date

# Create
datetime(2026, 2, 12, 14, 30)
date(2026, 2, 12)

# Format
now.strftime('%Y-%m-%d') # "2026-02-12"
now.strftime('%B %d, %Y') # "February 12, 2026"

# Parse
datetime.strptime('2026-02-12', '%Y-%m-%d')

# Arithmetic
today + timedelta(days=7)  # One week from now
```

### os and pathlib
```python
import os
from pathlib import Path

# os module
os.getcwd()              # Current directory
os.listdir('.')          # List directory contents
os.path.exists('file')   # Check if exists
os.path.join('a', 'b')   # Join paths

# pathlib (modern approach)
path = Path('file.txt')
path.exists()            # Check existence
path.read_text()         # Read file
path.write_text('data')  # Write file
path.parent              # Parent directory
path.name                # File name
```

---

## Import Statements

```python
# Import module
import module

# Import specific items
from module import function, Class

# Import all (not recommended)
from module import *

# Alias
import module as m
from module import function as f

# Common imports
import sys               # System-specific parameters
import os                # Operating system interface
import json              # JSON encoding/decoding
import csv               # CSV file reading/writing
import re                # Regular expressions
import math              # Mathematical functions
import random            # Random number generation
from datetime import datetime, date
from pathlib import Path
```

---

## Useful Patterns

### List Comprehension
```python
# Basic
[x * 2 for x in range(5)]

# With condition
[x for x in range(10) if x % 2 == 0]

# Nested
[[i * j for j in range(1, 4)] for i in range(1, 4)]
```

### Dictionary Comprehension
```python
{x: x**2 for x in range(5)}

{k: v for k, v in dict1.items() if v > 10}
```

### Generator Expression
```python
# Memory-efficient (doesn't create list)
gen = (x * 2 for x in range(1000000))
```

### Unpacking
```python
# Lists/tuples
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]

# Dictionaries
def func(**kwargs):
    pass

func(**{'a': 1, 'b': 2})
```

### Context Managers (with statement)
```python
# Auto-closes file
with open('file.txt') as f:
    content = f.read()

# Multiple contexts
with open('in.txt') as f_in, open('out.txt', 'w') as f_out:
    f_out.write(f_in.read())
```

---

## String Formatting

```python
name = "Alice"
age = 30

# f-strings (Python 3.6+, preferred)
f"Name: {name}, Age: {age}"
f"2 + 2 = {2 + 2}"
f"Value: {value:.2f}"     # 2 decimal places

# format method
"Name: {}, Age: {}".format(name, age)
"Name: {n}, Age: {a}".format(n=name, a=age)

# % operator (old style)
"Name: %s, Age: %d" % (name, age)
```

---

## Common Mistakes to Avoid

```python
# Mutable default arguments - DON'T
def bad(items=[]):       # Shared across calls!
    items.append(1)
    return items

# DO THIS instead
def good(items=None):
    if items is None:
        items = []
    items.append(1)
    return items

# Comparing to None - DON'T
if x == None:            # Bad

# DO THIS
if x is None:            # Good

# Modifying list while iterating - DON'T
for item in list1:
    list1.remove(item)   # Bad

# DO THIS
list1 = [x for x in list1 if condition]  # Good
```

---

## Keyboard Shortcuts (IDLE/VS Code)

**IDLE:**
- `Ctrl+N` — New file
- `F5` — Run script
- `Alt+P` — Previous command (shell)
- `Alt+N` — Next command (shell)

**VS Code:**
- `Ctrl+Enter` — Run selection
- `F5` — Debug
- `Ctrl+/` — Toggle comment
- `Ctrl+Space` — IntelliSense

---

## Quick Tips

1. **Use `help()`** — `help(str.split)` for documentation
2. **Use `dir()`** — `dir(list)` to see all methods
3. **Use docstrings** — First line in function/class
4. **Follow PEP 8** — Python's style guide
5. **Use `with`** for files — Auto-cleanup
6. **Name meaningfully** — `customer_count` not `c`
7. **Keep functions small** — One purpose per function
8. **Handle exceptions** — Don't let programs crash silently
9. **Use comprehensions** — More Pythonic than loops
10. **Comment why, not what** — Code shows what, comments explain why

---

**For more help:** `python.org/docs` | **Style guide:** PEP 8 | **Practice:** LeetCode, HackerRank, Project Euler
