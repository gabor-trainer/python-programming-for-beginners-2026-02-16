# Python Style Guide for Beginners

**Target Audience:** Day 1+ students learning to write clean, readable code  
**Prerequisites:** Basic Python syntax  
**Reference:** PEP 8 – Python's official style guide

---

## Why Style Matters

Consistent style makes code easier to read, debug, and maintain. Python's community follows PEP 8 conventions, making code recognizable across projects.

**Benefits:**
- Faster code reviews by teammates
- Fewer bugs from misreading code
- Professional code that matches industry standards

---

## Naming Conventions

### Variables and Functions: `snake_case`

```python
# Good
user_name = "Alice"
total_price = 99.99

def calculate_tax(amount):
    return amount * 0.08

# Bad
userName = "Alice"        # camelCase (use in JavaScript, not Python)
TotalPrice = 99.99        # PascalCase (reserved for classes)
```

### Classes: `PascalCase`

```python
# Good
class BankAccount:
    pass

class UserProfile:
    pass

# Bad
class bank_account:       # snake_case
    pass

class USERPROFILE:        # ALL_CAPS (reserved for constants)
    pass
```

### Constants: `ALL_CAPS`

```python
# Good
MAX_CONNECTIONS = 100
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30

# Bad
max_connections = 100     # Looks like a variable
MaxConnections = 100      # Looks like a class
```

### Private Attributes: Leading underscore

```python
class BankAccount:
    def __init__(self):
        self._balance = 0           # "Private" by convention
        self.account_number = "123" # Public
    
    def _validate(self):            # "Private" method
        pass
```

---

## Indentation and Spacing

### Use 4 Spaces (Never Tabs)

```python
# Good
def greet(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, stranger")

# Bad
def greet(name):
  if name:        # Only 2 spaces
    print(f"Hello, {name}")
```

**VS Code Tip:** Set Editor: Tab Size to 4 and Editor: Insert Spaces to true.

### Blank Lines

```python
# Good - Two blank lines between top-level definitions
def function_one():
    pass


def function_two():
    pass


class MyClass:
    pass


# Good - One blank line between methods
class MyClass:
    def method_one(self):
        pass
    
    def method_two(self):
        pass


# Good - Use blank lines within functions for logical sections
def process_data(data):
    # Validate input
    if not data:
        return None
    
    # Transform data
    cleaned = [x.strip() for x in data]
    
    # Return result
    return cleaned
```

### Operators and Assignment

```python
# Good - Spaces around operators
x = 5
y = x + 10
is_valid = x > 0 and y < 100

result = function(arg1, arg2)

# Bad - No spaces or inconsistent
x=5
y=x+10
is_valid=x>0and y<100

result=function( arg1,arg2 )


# Good - No space for keyword arguments
result = function(name="Alice", age=30)

# Bad
result = function(name = "Alice", age = 30)
```

---

## Line Length

Keep lines under 79 characters (PEP 8 recommends 79, but 88-100 is acceptable in modern editors).

```python
# Good - Natural line break
def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    payment = (principal * monthly_rate * 
               (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return payment


# Good - Parentheses for implicit continuation
result = some_function(
    argument_one,
    argument_two,
    argument_three,
    argument_four
)


# Good - List continuation
numbers = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]
```

---

## Imports

### Order and Grouping

```python
# Good - Three groups separated by blank lines
# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import requests
from flask import Flask, render_template

# 3. Local application
from myapp.models import User
from myapp.utils import format_date


# Bad - Mixed order, no grouping
from myapp.models import User
import sys
import requests
from datetime import datetime
```

### Import Style

```python
# Good - One import per line for readability
import os
import sys

from datetime import datetime, timedelta

# Bad - Multiple imports on one line
import os, sys, json


# Good - Import specific names
from math import sqrt, pi

# Acceptable - Import module for many items
import math

# Bad - Wildcard imports (unclear what's imported)
from math import *
```

---

## String Quotes

Use single or double quotes consistently. Python doesn't care, but pick one style.

```python
# Good - Consistent single quotes
name = 'Alice'
message = 'Hello, world'

# Good - Consistent double quotes
name = "Alice"
message = "Hello, world"

# Good - Use opposite quote to avoid escaping
greeting = "It's a beautiful day"
sql = 'SELECT * FROM users WHERE name = "Alice"'

# Bad - Mixed without reason
name = 'Alice'
message = "Hello, world"
```

**Recommendation:** Use double quotes as primary (matches JSON, SQL, other languages).

---

## Comparisons

### Boolean Comparisons

```python
# Good - Direct boolean check
if is_valid:
    process()

if not is_empty:
    continue

# Bad - Explicit comparison to True/False
if is_valid == True:
    process()

if is_empty != False:
    continue


# Good - Check for None
if value is None:
    handle_missing()

# Bad - == for None
if value == None:
    handle_missing()


# Good - Check for empty containers
if not items:
    print("No items")

# Awkward - Length check
if len(items) == 0:
    print("No items")
```

### Use `in` for Membership

```python
# Good
if user_type in ['admin', 'moderator']:
    grant_access()

# Bad
if user_type == 'admin' or user_type == 'moderator':
    grant_access()
```

---

## Comments and Docstrings

### Inline Comments

```python
# Good - Explain why, not what
x = x + 1  # Compensate for border width

# Bad - States the obvious
x = x + 1  # Increment x


# Good - Update comments when code changes
# Check if user has admin privileges
if user.role == 'admin':
    grant_access()

# Bad - Outdated comment
# Check if user is logged in
if user.role == 'admin':
    grant_access()
```

### Docstrings for Functions

```python
# Good - Clear docstring
def calculate_area(radius):
    """Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle (positive number).
    
    Returns:
        The area as a float.
    """
    return 3.14159 * radius ** 2


# Good - Simple one-liner for obvious functions
def get_name(self):
    """Return the user's full name."""
    return f"{self.first_name} {self.last_name}"


# Bad - No docstring
def calculate_area(radius):
    return 3.14159 * radius ** 2
```

### Module Docstrings

```python
"""User authentication and authorization utilities.

This module provides functions for user login, password hashing,
and permission checking.
"""

import hashlib
import secrets
```

---

## Function and Method Design

### Function Length

Keep functions focused. If a function exceeds ~25 lines, consider splitting it.

```python
# Good - Focused function
def validate_email(email):
    """Check if email address is valid."""
    if not email or '@' not in email:
        return False
    
    username, domain = email.split('@')
    
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True


# Good - Split complex logic
def process_order(order):
    """Process a customer order."""
    if not validate_order(order):
        return None
    
    total = calculate_total(order)
    apply_discount(order, total)
    charge_customer(order)
    send_confirmation(order)
    
    return order


def validate_order(order):
    """Check if order is valid."""
    # Validation logic
    pass


def calculate_total(order):
    """Calculate order total."""
    # Calculation logic
    pass
```

### Default Arguments

```python
# Good - Immutable defaults
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Dangerous - Mutable defaults
def add_item(item, items=[]):  # Same list shared across calls!
    items.append(item)
    return items

# Fix - Use None and create new list
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Common Anti-Patterns to Avoid

### 1. Using `==` Instead of `is` for None

```python
# Good
if value is None:
    handle_missing()

# Bad
if value == None:
    handle_missing()
```

### 2. Checking Type with Strings

```python
# Good
if isinstance(value, int):
    process_integer(value)

# Bad
if type(value) == type(1):
    process_integer(value)

# Worse
if str(type(value)) == "<class 'int'>":
    process_integer(value)
```

### 3. Concatenating Lists with `+` in Loops

```python
# Good - Append, then process once
items = []
for i in range(1000):
    items.append(i)

# Bad - Creates new list each iteration
items = []
for i in range(1000):
    items = items + [i]
```

### 4. Not Using `with` for Files

```python
# Good - Automatic cleanup
with open('data.txt', 'r') as f:
    data = f.read()

# Bad - Manual cleanup required
f = open('data.txt', 'r')
data = f.read()
f.close()  # Easy to forget, especially with errors
```

### 5. Bare `except` Clauses

```python
# Good - Catch specific exceptions
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")

# Bad - Catches everything (including Ctrl+C!)
try:
    value = int(user_input)
except:
    print("Invalid number")
```

---

## Tools for Checking Style

### Built-in to VS Code

1. **Python extension** provides automatic formatting with Black or autopep8
2. **Pylance** shows style warnings in real-time

### Enable Auto-Formatting

In VS Code settings:
```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### Manual Formatting

```powershell
# Install Black formatter
uv add black --dev

# Format all Python files
black .

# Check without modifying
black --check .
```

### Linting

```powershell
# Install flake8 for style checking
uv add flake8 --dev

# Check all files
flake8 .

# Check specific file
flake8 myfile.py
```

---

## Quick Reference Checklist

**Naming:**
- [ ] Variables and functions: `snake_case`
- [ ] Classes: `PascalCase`
- [ ] Constants: `ALL_CAPS`

**Spacing:**
- [ ] 4 spaces for indentation
- [ ] Spaces around operators: `x = 5`, not `x=5`
- [ ] Two blank lines between functions/classes
- [ ] One blank line between methods

**Imports:**
- [ ] Standard library first, then third-party, then local
- [ ] One import per line
- [ ] Blank lines between groups

**Best Practices:**
- [ ] Lines under 79-100 characters
- [ ] Use `is` for None comparisons
- [ ] Use `with` for file handling
- [ ] Catch specific exceptions
- [ ] Write docstrings for functions

---

## When to Break the Rules

Style guides are suggestions, not laws. Break rules when:

1. **Legacy code:** Match existing style in the codebase
2. **Readability:** If following a rule makes code less clear
3. **Team conventions:** Your team has different standards

**Example where breaking the rule is better:**

```python
# PEP 8 would want this split, but it's less readable
result = function_with_long_name(
    argument_one,
    argument_two
)

# More readable on one line (if under 100 characters)
result = function_with_long_name(argument_one, argument_two)
```

---

## Next Steps

1. **Install formatter:** Add Black to your project with `uv add black --dev`
2. **Enable auto-format:** Set VS Code to format on save
3. **Practice:** Apply these rules to your existing code
4. **Review:** Read full PEP 8 at python.org/dev/peps/pep-0008/

**Remember:** Consistency matters more than perfection. Pick a style and stick with it throughout your project.
