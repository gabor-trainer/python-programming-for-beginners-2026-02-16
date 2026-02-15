# Lab 1.2: Working with variables and operators

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Create variables of different types (int, float, str, bool) and inspect them with `type()`
- Perform calculations using arithmetic operators
- Compare values using comparison and logical operators
- Convert between types with `int()`, `float()`, `str()`
- Read user input with `input()` and produce formatted output with f-strings

---

## 3. Prerequisites

**Knowledge prerequisites**: Understanding of the Python REPL, VS Code, and how to run scripts (Chapter 1.1).

**Previous labs**: Lab 1.1 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] VS Code installed with the Python extension
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Navigate to your working directory: `cd C:\labs`
- [ ] Verify the REPL works: `python` -> `>>> print("Ready")` -> `exit()`

No additional setup is required for this lab.

---

## 5. Concept overview

Every program works with data: names, prices, quantities, measurements, yes/no decisions. Python stores data in **variables** — named references that you can create, change, and combine. The type of data (number, text, true/false) determines what operations are available.

Variables become powerful when combined with **operators** — symbols that perform calculations, comparisons, and logical decisions. A unit converter multiplies a distance by a conversion factor. A login check compares a password. A discount calculator uses conditions and arithmetic together.

In this lab, you will build small programs that store data in variables, perform calculations, read user input, and display formatted results. These are the building blocks of every Python program.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Explore Python's type system interactively
- Build a temperature converter that calculates and formats results
- Create an interactive program that reads user input and performs calculations
- Write a program that uses comparison and logical operators

---

### Exercise 1.2.1: Explore variables and types in the REPL

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Create variables of each fundamental type and inspect them.

**Scenario**: Before writing scripts, you want to understand how Python handles different data types. The REPL is the fastest way to experiment.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Create variables of each type and check them with `type()`:

```python
>>> age = 25
>>> type(age)
<class 'int'>

>>> temperature = 36.6
>>> type(temperature)
<class 'float'>

>>> city = "Budapest"
>>> type(city)
<class 'str'>

>>> is_student = True
>>> type(is_student)
<class 'bool'>
```

3. Observe dynamic typing — reassign a variable to a different type:

```python
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> x = 3.14
>>> type(x)
<class 'float'>
```

4. Try arithmetic with different types:

```python
>>> 10 + 5
15
>>> 10 + 5.0
15.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 2 ** 8
256
```

5. Try string operations:

```python
>>> first = "Hello"
>>> second = "World"
>>> first + " " + second
'Hello World'
>>> first * 3
'HelloHelloHello'
```

6. Test type conversion:

```python
>>> int("42")
42
>>> float("3.14")
3.14
>>> str(100)
'100'
>>> int(3.9)
3
```

7. See what happens with an invalid conversion:

```python
>>> int("hello")
```

You will see a `ValueError`. This is expected — Python cannot convert the text "hello" to an integer.

8. Exit the REPL:

```python
>>> exit()
```

**Verification**: You created variables of all four types and successfully converted between types.

**Expected output**: Each `type()` call shows the correct class. Arithmetic results match the expected values. The invalid conversion raises a `ValueError`.

**Try it yourself**:
- Check what `type(True + 1)` returns and think about why
- Try `bool(0)`, `bool(1)`, `bool("")`, `bool("hello")` — observe the pattern

---

### Exercise 1.2.2: Build a temperature converter

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Write a script that converts Celsius to Fahrenheit using variables, arithmetic, and f-strings.

**Scenario**: Weather reports in different countries use different scales. A quick converter saves time and avoids mistakes.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `temperature.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# temperature.py - Celsius to Fahrenheit converter

celsius = 25.0

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
```

3. Save the file as `temperature.py` in `C:\labs`.

4. Run it with F5. You should see:

```
25.0°C = 77.0°F
```

5. Now extend the script to convert several temperatures. Replace the content with:

```python
# temperature.py - Celsius to Fahrenheit converter (extended)

temperatures_celsius = [0, 10, 20, 25, 30, 37, 100]

print("Celsius to Fahrenheit conversion table")
print("-" * 35)

for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"  {celsius:>6}°C  =  {fahrenheit:>6.1f}°F")
```

6. Save and run with F5. You should see a formatted table with seven rows.

**Verification**: The output shows a header, a separator line, and seven rows of conversions. Each row has the Celsius value right-aligned and the Fahrenheit value formatted to one decimal place.

**Expected output**: A neatly aligned table. The 0°C row should show 32.0°F. The 100°C row should show 212.0°F. The 37°C row should show 98.6°F.

**Try it yourself**:
- Add negative temperatures (-40, -20, -10) to the list and notice anything special about -40
- Modify the script to also show the Kelvin value (Kelvin = Celsius + 273.15)

---

### Exercise 1.2.3: Interactive calculator with user input

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Read user input, convert types, perform calculations, and display formatted results.

**Scenario**: You need to build a tool that calculates the total cost of an order, including tax. The user enters the item price and quantity.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `order_calculator.py` in `C:\labs`.

2. Type the following code:

```python
# order_calculator.py - Calculate order total with tax

TAX_RATE = 0.20  # 20% tax rate

print("=== Order calculator ===")
print()

item_name = input("Item name: ")
price_str = input("Price per unit: ")
quantity_str = input("Quantity: ")

price = float(price_str)
quantity = int(quantity_str)

subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f"Item:     {item_name}")
print(f"Price:    ${price:.2f} x {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (20%): ${tax:.2f}")
print(f"Total:    ${total:.2f}")
```

3. Save as `order_calculator.py` in `C:\labs`.

4. Run with F5. Enter sample values when prompted:

```
=== Order calculator ===

Item name: Notebook
Price per unit: 4.99
Quantity: 3

Item:     Notebook
Price:    $4.99 x 3
Subtotal: $14.97
Tax (20%): $2.99
Total:    $17.96
```

5. Run the script again from the command line to confirm it works there too:

```
C:\labs> python order_calculator.py
```

**Verification**: The program asks for three inputs and displays a correctly calculated receipt. The subtotal equals price times quantity. The tax equals 20% of the subtotal. The total equals subtotal plus tax.

**Expected output**: A receipt-style output with dollar amounts formatted to two decimal places. The tax and total should be mathematically correct for the values you entered.

**Hints**:
- If you get a `ValueError`, check that you enter a valid number (not text) for price and quantity
- The `:.2f` format specifier forces two decimal places in the output

**Try it yourself**:
- Add a discount feature: if quantity is 10 or more, apply a 10% discount before tax
- Add a second item to the order and calculate the combined total

---

### Exercise 1.2.4: Comparison and logical operators

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use comparison and logical operators to evaluate conditions and display results.

**Scenario**: An online store determines shipping costs based on order value and customer location. You will write expressions that evaluate these business rules.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `shipping.py` in `C:\labs`.

2. Type the following code:

```python
# shipping.py - Determine shipping details based on order

order_total = 75.00
is_domestic = True
is_member = False

# Comparison operators
print("=== Order analysis ===")
print(f"Order total: ${order_total:.2f}")
print(f"Domestic: {is_domestic}")
print(f"Member: {is_member}")
print()

# Business rules
free_shipping = order_total >= 50.00 and is_domestic
express_available = order_total >= 100.00 or is_member
needs_customs = not is_domestic

print("=== Shipping rules ===")
print(f"Free shipping eligible: {free_shipping}")
print(f"Express available: {express_available}")
print(f"Customs required: {needs_customs}")
print()

# Shipping cost calculation
if free_shipping:
    shipping_cost = 0.00
elif is_domestic:
    shipping_cost = 5.99
else:
    shipping_cost = 15.99

grand_total = order_total + shipping_cost

print("=== Final calculation ===")
print(f"Shipping: ${shipping_cost:.2f}")
print(f"Grand total: ${grand_total:.2f}")
```

3. Save as `shipping.py` in `C:\labs`.

4. Run with F5.

5. Now modify the values at the top of the script to test different scenarios:

   - Set `order_total = 30.00` — does free shipping change?
   - Set `is_domestic = False` — what happens to customs and shipping cost?
   - Set `is_member = True` and `order_total = 40.00` — is express available?

Run the script after each change and observe how the results change.

**Verification**: The boolean results match the logic: free shipping requires both a $50+ order and domestic shipping. Express requires either a $100+ order or membership. Customs applies only to non-domestic orders.

**Expected output**: Three sections of output. The boolean values should be `True` or `False` based on the rules. The shipping cost should be $0.00, $5.99, or $15.99 depending on the conditions.

**Try it yourself**:
- Add a new rule: "priority handling" is available if the order is over $200 or the customer is a member with a domestic order
- Convert the script to use `input()` so the user enters the order total and answers yes/no for domestic and member status

---

## 7. Validation checklist

- [ ] You can create variables of type int, float, str, and bool and verify them with `type()`
- [ ] `temperature.py` displays a formatted conversion table with correct values
- [ ] `order_calculator.py` reads user input and calculates a correct total with tax
- [ ] `shipping.py` evaluates boolean conditions correctly for different input combinations
- [ ] You understand the difference between `=` (assignment) and `==` (comparison)
- [ ] You can use f-strings with format specifiers like `:.2f`

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `ValueError: invalid literal for int()` | Entered text instead of a number for `input()` | Enter only digits. For float, use a decimal point. |
| `TypeError: can only concatenate str to str` | Tried to add a number to a string with `+` | Use `str()` to convert or use an f-string |
| `NameError: name 'x' is not defined` | Variable not created or misspelled | Check spelling, ensure variable is assigned before use |
| `SyntaxError: invalid syntax` near `=` in `if` | Used `=` instead of `==` in a comparison | Use `==` for comparisons, `=` for assignment |
| Numbers display too many decimals | Float precision | Use `:.2f` in f-strings to limit decimal places |

**Common beginner pitfalls:**
- Forgetting to convert `input()` results. `input()` always returns a string — you must use `int()` or `float()` for arithmetic.
- Using `=` when you mean `==`. The first assigns, the second compares.
- Assuming `int(3.9)` rounds to 4. It truncates to 3 (drops the decimal part).

---

## 9. Questions

1. Python allows you to reassign a variable to a completely different type (for example, `x = 10` then `x = "hello"`). Explain why this flexibility could be both an advantage and a risk. How might it cause subtle bugs in a larger program?

2. When you divide two integers with `/`, Python returns a float (for example, `10 / 2` gives `5.0`). Why do you think Python was designed this way, rather than returning an integer when the division is exact?

3. The expression `0.1 + 0.2` does not equal `0.3` in Python (it gives `0.30000000000000004`). Explain why this happens and what approach you would use if exact decimal arithmetic mattered (for example, in financial calculations).

4. You are building a program that reads a user's age from the keyboard and determines if they are eligible to vote (18+). What could go wrong if the user enters "twenty" instead of "20"? How would you design the program to handle this?

5. Compare using `int()` versus `float()` to convert user input for a calculator program. What trade-offs are involved in choosing one over the other?

6. Explain the difference between `10 / 3`, `10 // 3`, and `10 % 3`. Give a real-world example where floor division and modulus are useful together (for example, converting seconds to minutes and remaining seconds).

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\temperature.py`
- `C:\labs\order_calculator.py`
- `C:\labs\shipping.py`

These files are small and will serve as reference examples.

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- Variables are created with `=` and Python infers the type from the value
- The four fundamental types are `int`, `float`, `str`, and `bool`
- `type()` reveals the type of any value or variable
- `input()` always returns a string — convert with `int()` or `float()` for numbers
- f-strings (`f"..."`) embed variables and expressions directly in strings
- `:.2f` inside f-strings formats numbers to two decimal places
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) return booleans
- Logical operators (`and`, `or`, `not`) combine boolean conditions
- Use `=` for assignment, `==` for comparison — never confuse them

---

## 12. Additional resources

- Python data types reference: https://docs.python.org/3/library/stdtypes.html
- Python built-in functions (type, int, float, str): https://docs.python.org/3/library/functions.html
- Python f-string formatting: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
- PEP 8 — Style guide for Python code: https://peps.python.org/pep-0008/
- Python operators reference: https://docs.python.org/3/library/operator.html

---

## 13. Appendices

### Appendix A: Quick reference — Variables and types

| Type | Example | Created by |
|------|---------|------------|
| `int` | `42` | Whole number literal or `int()` |
| `float` | `3.14` | Decimal literal or `float()` |
| `str` | `"hello"` | Quotes or `str()` |
| `bool` | `True` | Literal or comparison result |

### Appendix B: Operator reference

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `7 * 6` | `42` |
| `/` | Division (float) | `10 / 3` | `3.333...` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Power | `2 ** 10` | `1024` |
| `==` | Equal | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `and` | Logical AND | `True and False` | `False` |
| `or` | Logical OR | `True or False` | `True` |
| `not` | Logical NOT | `not True` | `False` |

### Appendix C: f-string format specifiers

| Specifier | Meaning | Example | Result |
|-----------|---------|---------|--------|
| `:.2f` | 2 decimal places | `f"{3.1:.2f}"` | `3.10` |
| `:.0f` | No decimal places | `f"{3.7:.0f}"` | `4` |
| `:>10` | Right-align in 10 chars | `f"{'hi':>10}"` | `"        hi"` |
| `:<10` | Left-align in 10 chars | `f"{'hi':<10}"` | `"hi        "` |
| `:^10` | Center in 10 chars | `f"{'hi':^10}"` | `"    hi    "` |

---

## 14. Answers

**Answer 1:**

The advantage of dynamic typing is speed of development. You do not need to declare types, write type annotations, or satisfy a compiler before running code. This makes Python ideal for scripting, data exploration, and rapid prototyping. You can quickly test ideas without boilerplate.

The risk is that a variable's type can change unexpectedly. For example, a function might return an integer in one case and a string in another. Code that later adds 1 to that variable will fail with a `TypeError` if it happens to be a string. In a small script, this is easy to spot. In a large program with many functions, the error might surface far from where the type changed, making debugging difficult.

To mitigate this risk, experienced Python developers use descriptive variable names (so the expected type is clear), write tests, and optionally use type hints (like `age: int = 25`) that tools can check without changing Python's dynamic nature.

**Answer 2:**

Python 3 was designed so that `/` always returns a float to avoid a common source of bugs. In Python 2, `10 / 3` returned `3` (integer division), which led to incorrect results when programmers expected a decimal answer. By always returning a float, Python 3 ensures that `10 / 2` gives `5.0` — mathematically correct, with no silent truncation.

If you specifically want integer division (discarding the remainder), Python provides `//` for that purpose. This makes the programmer's intent explicit: `/` means exact division, `//` means floor division. Having separate operators eliminates ambiguity.

**Answer 3:**

This is a well-known limitation of floating-point arithmetic, not a Python bug. Computers store numbers in binary (base 2). The decimal value 0.1 has no exact binary representation — it becomes a repeating fraction, like 1/3 in decimal (0.333...). When Python adds two approximate values, the small errors accumulate.

For most applications, the difference is negligible (on the order of $10^{-16}$). For financial calculations where exact decimal arithmetic matters, Python provides the `decimal` module. You can write `from decimal import Decimal` and use `Decimal("0.1") + Decimal("0.2")`, which gives exactly `0.3`. The `decimal` module uses base-10 arithmetic internally, avoiding binary representation errors.

**Answer 4:**

If the user enters "twenty", the `int()` conversion will raise a `ValueError` because "twenty" is not a valid integer string. The program will crash with a traceback, and the user will see an error message that may be confusing.

To handle this, you would use a `try`/`except` block (covered in Chapter 3.4) to catch the `ValueError` and display a helpful message: "Please enter a number." You could also put the input in a loop that keeps asking until the user enters a valid number. This is defensive programming — anticipating user mistakes and handling them gracefully.

**Answer 5:**

Using `int()` restricts input to whole numbers. This is appropriate when fractional values make no sense (for example, "How many items?" — you cannot buy 2.5 items). If the user enters "3.5", `int("3.5")` raises a `ValueError`, which acts as built-in validation.

Using `float()` accepts both whole numbers and decimals. `float("3")` works (gives `3.0`) and `float("3.5")` also works. This is more flexible but may allow unexpected inputs. A calculator generally should use `float()` since users expect to enter decimals. A quantity field should use `int()` since fractional quantities may not be valid.

The trade-off is flexibility versus strictness. Choose the type that matches the real-world meaning of the data.

**Answer 6:**

`10 / 3` returns `3.3333333333333335` — the exact (well, floating-point approximate) result of dividing 10 by 3. `10 // 3` returns `3` — the integer quotient, discarding the remainder. `10 % 3` returns `1` — the remainder after dividing 10 by 3.

A practical example: converting a total number of seconds to minutes and remaining seconds. If you have 195 seconds: `195 // 60` gives `3` (minutes), and `195 % 60` gives `15` (remaining seconds). Together: 195 seconds = 3 minutes and 15 seconds. This pattern applies to any unit conversion: total cents to dollars and cents, total months to years and months, and so on.

---

## 15. Code solutions

### Exercise 1.2.2: temperature.py

```python
# temperature.py - Celsius to Fahrenheit converter (extended)

temperatures_celsius = [0, 10, 20, 25, 30, 37, 100]

print("Celsius to Fahrenheit conversion table")
print("-" * 35)

for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"  {celsius:>6}°C  =  {fahrenheit:>6.1f}°F")
```

### Exercise 1.2.3: order_calculator.py

```python
# order_calculator.py - Calculate order total with tax

TAX_RATE = 0.20  # 20% tax rate

print("=== Order calculator ===")
print()

item_name = input("Item name: ")
price_str = input("Price per unit: ")
quantity_str = input("Quantity: ")

price = float(price_str)
quantity = int(quantity_str)

subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f"Item:     {item_name}")
print(f"Price:    ${price:.2f} x {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (20%): ${tax:.2f}")
print(f"Total:    ${total:.2f}")
```

### Exercise 1.2.4: shipping.py

```python
# shipping.py - Determine shipping details based on order

order_total = 75.00
is_domestic = True
is_member = False

# Comparison operators
print("=== Order analysis ===")
print(f"Order total: ${order_total:.2f}")
print(f"Domestic: {is_domestic}")
print(f"Member: {is_member}")
print()

# Business rules
free_shipping = order_total >= 50.00 and is_domestic
express_available = order_total >= 100.00 or is_member
needs_customs = not is_domestic

print("=== Shipping rules ===")
print(f"Free shipping eligible: {free_shipping}")
print(f"Express available: {express_available}")
print(f"Customs required: {needs_customs}")
print()

# Shipping cost calculation
if free_shipping:
    shipping_cost = 0.00
elif is_domestic:
    shipping_cost = 5.99
else:
    shipping_cost = 15.99

grand_total = order_total + shipping_cost

print("=== Final calculation ===")
print(f"Shipping: ${shipping_cost:.2f}")
print(f"Grand total: ${grand_total:.2f}")
```
