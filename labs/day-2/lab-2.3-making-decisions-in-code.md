# Lab 2.3: Making decisions in code

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Write `if`, `if/else`, and `if/elif/else` statements to control program flow
- Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (`and`, `or`, `not`)
- Combine multiple conditions to express complex decision logic
- Validate user input and handle edge cases with conditional statements
- Build a menu-driven program that responds to user choices

---

## 3. Prerequisites

**Knowledge prerequisites**: Variables, data types, operators, lists, dictionaries, and `input()` (Chapters 1.1–2.2).

**Previous labs**: Labs 2.1 and 2.2 completed.

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

Every useful program makes decisions. A login system checks whether the password is correct. An online shop applies a discount if the order exceeds a threshold. A thermostat turns on heating when the temperature drops below a target. Without **conditional statements**, a program would execute the same instructions every time, regardless of the data.

Python's `if`, `elif`, and `else` keywords let you express these decisions. Combined with comparison operators (is this value greater?) and logical operators (are both conditions true?), you can model arbitrarily complex decision logic. The key skill is translating real-world rules ("free shipping for orders over $50 from domestic customers") into precise code.

In this lab, you will build a grade calculator, a command-line menu system, and an input validation routine — all requiring you to think carefully about which conditions to check and in what order.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Convert numerical scores to letter grades using multi-branch conditions
- Build an interactive command-line menu that responds to user choices
- Validate user input and handle edge cases with combined conditions
- Design complex decision logic for a practical scenario

---

### Exercise 2.3.1: Grade calculator

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Translate a grading scale into an `if/elif/else` chain.

**Scenario**: A teacher needs a program that converts percentage scores into letter grades. The scale is: A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `grades.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# grades.py - Convert percentage scores to letter grades

scores = [95, 82, 67, 73, 58, 90, 45, 88, 100, 71]

print("=== Grade report ===\n")
print(f"  {'Score':>5}  Grade")
print(f"  {'-' * 5}  -----")

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"  {score:>5}  {grade}")

# Summary statistics
print()
a_count = sum(1 for s in scores if s >= 90)
passing = sum(1 for s in scores if s >= 60)
print(f"  A grades: {a_count}")
print(f"  Passing (D or above): {passing} out of {len(scores)}")
print(f"  Average: {sum(scores) / len(scores):.1f}")
```

3. Save and run with F5.

4. Study the `if/elif/else` chain. The order matters: Python checks each condition from top to bottom and executes the first matching branch. A score of 82 satisfies `score >= 70` and `score >= 80`, but because `>= 80` is checked first, it correctly gets grade "B".

5. Add a "plus/minus" enhancement. Replace the grading logic with:

```python
    if score >= 97:
        grade = "A+"
    elif score >= 93:
        grade = "A"
    elif score >= 90:
        grade = "A-"
    elif score >= 87:
        grade = "B+"
    elif score >= 83:
        grade = "B"
    elif score >= 80:
        grade = "B-"
    elif score >= 77:
        grade = "C+"
    elif score >= 73:
        grade = "C"
    elif score >= 70:
        grade = "C-"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
```

6. Save and run with F5. Verify that the grades are now more specific.

**Verification**: Each score maps to the correct grade. The summary shows the correct count of A grades, passing students, and average score.

**Expected output**: A table with 10 rows. With the original scale, scores 95 and 90 and 100 get "A". With the plus/minus scale, 95 gets "A", 90 gets "A-", and 100 gets "A+".

**Try it yourself**:
- Add an interactive version that reads a score with `input()` and prints the grade
- Add validation: if the score is below 0 or above 100, print "Invalid score" instead of a grade
- Count how many students got each letter grade using a dictionary

---

### Exercise 2.3.2: Command-line menu system

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Build a menu-driven program that performs different actions based on user choices.

**Scenario**: You are building a simple unit converter. The user picks a conversion type from a menu, enters a value, and sees the result.

**Tasks**:

1. In VS Code, create a new file. Save it as `converter.py` in `C:\labs`.

2. Type the following code:

```python
# converter.py - Unit converter with menu

print("=== Unit converter ===")
print()
print("  1. Celsius to Fahrenheit")
print("  2. Kilometers to miles")
print("  3. Kilograms to pounds")
print("  4. Quit")
print()

choice = input("Choose an option (1-4): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"\n  {celsius}°C = {fahrenheit:.1f}°F")

elif choice == "2":
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"\n  {km} km = {miles:.2f} miles")

elif choice == "3":
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print(f"\n  {kg} kg = {pounds:.2f} lbs")

elif choice == "4":
    print("\nGoodbye!")

else:
    print(f"\n  '{choice}' is not a valid option. Please enter 1, 2, 3, or 4.")
```

3. Save and run with F5. Test each menu option.

4. Now enhance the converter with a loop so the menu repeats until the user quits. Replace the entire content with:

```python
# converter.py - Unit converter with repeating menu

print("=== Unit converter ===")

while True:
    print()
    print("  1. Celsius to Fahrenheit")
    print("  2. Kilometers to miles")
    print("  3. Kilograms to pounds")
    print("  4. Quit")
    print()

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        value_str = input("Enter temperature in Celsius: ")
        celsius = float(value_str)
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"\n  Result: {celsius}°C = {fahrenheit:.1f}°F")

    elif choice == "2":
        value_str = input("Enter distance in kilometers: ")
        km = float(value_str)
        miles = km * 0.621371
        print(f"\n  Result: {km} km = {miles:.2f} miles")

    elif choice == "3":
        value_str = input("Enter weight in kilograms: ")
        kg = float(value_str)
        pounds = kg * 2.20462
        print(f"\n  Result: {kg} kg = {pounds:.2f} lbs")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print(f"\n  '{choice}' is not a valid option. Please enter 1, 2, 3, or 4.")
```

5. Save and run with F5. Try several conversions in a row, then enter "4" to quit.

**Verification**: The menu repeats after each conversion. Invalid choices display a helpful message. Entering "4" prints "Goodbye!" and stops the program.

**Expected output**: The menu appears, the user picks an option, enters a value, and sees the result. The menu appears again until the user picks "4".

**Try it yourself**:
- Add a fifth option: Fahrenheit to Celsius (the reverse conversion)
- Add input validation: if the user enters text instead of a number, catch the error and show a message instead of crashing
- Keep a count of how many conversions were performed and display it when the user quits

---

### Exercise 2.3.3: Input validation with combined conditions

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Validate user input by combining multiple conditions with `and`, `or`, and `not`.

**Scenario**: An event registration system needs to validate attendee data: age must be between 18 and 65, name must not be empty, and email must contain "@". You need to check all these conditions and provide specific feedback for each failure.

**Tasks**:

1. In VS Code, create a new file. Save it as `registration.py` in `C:\labs`.

2. Type the following code:

```python
# registration.py - Event registration with input validation

print("=== Event registration ===\n")

name = input("Full name: ").strip()
age_str = input("Age: ").strip()
email = input("Email: ").strip()

# Validate each field
errors = []

if not name:
    errors.append("Name cannot be empty.")

if not age_str.isdigit():
    errors.append("Age must be a whole number.")
else:
    age = int(age_str)
    if age < 18 or age > 65:
        errors.append(f"Age must be between 18 and 65 (you entered {age}).")

if "@" not in email or "." not in email:
    errors.append("Email must contain '@' and '.' (e.g., user@example.com).")

# Show results
print()
if errors:
    print("Registration FAILED. Please fix the following:")
    for error in errors:
        print(f"  - {error}")
else:
    age = int(age_str)
    print("Registration successful!")
    print(f"  Name:  {name}")
    print(f"  Age:   {age}")
    print(f"  Email: {email}")
```

3. Save and run with F5. Test with valid data first:

```
Full name: Alice Smith
Age: 30
Email: alice@example.com
```

4. Run again with invalid data to trigger each validation:

```
Full name:
Age: seventeen
Email: alice-at-example
```

5. Run again with an out-of-range age:

```
Full name: Bob
Age: 15
Email: bob@test.com
```

**Verification**: Valid data produces a success message. Each type of invalid data produces a specific error message. Multiple errors are displayed at once (the program collects all errors, not just the first one).

**Expected output**: Either a success message with the registration details, or a failure message listing all validation errors found.

**Hints**:
- `.strip()` removes leading and trailing whitespace from the input
- `.isdigit()` returns `True` if the string contains only digits
- Collecting errors in a list lets you show all problems at once rather than stopping at the first one

**Try it yourself**:
- Add a phone number field that must be at least 9 digits
- Add a "VIP" option that allows ages 16-70 instead of 18-65
- Wrap the entire registration in a loop that asks "Try again? (y/n)" after a failed validation

---

### Exercise 2.3.4: Ticket pricing with complex rules

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Implement multi-factor decision logic that combines age, membership, and time of day.

**Scenario**: A cinema has a complex pricing model. The base ticket price is $12.00. Discounts and surcharges apply based on age, membership status, and show time. Your task is to implement the pricing logic and display a breakdown.

**Tasks**:

1. In VS Code, create a new file. Save it as `ticket_price.py` in `C:\labs`.

2. Write a script that applies these rules:
   - **Children** (under 12): 50% discount
   - **Seniors** (65 and over): 30% discount
   - **Members**: additional $2.00 off (applied after age discount)
   - **Evening shows** (18:00 or later): $3.00 surcharge (applied to everyone)
   - Minimum price is $0.00 (never negative)

3. Use these test cases to verify your logic:

```python
# ticket_price.py - Cinema ticket pricing

BASE_PRICE = 12.00

test_cases = [
    {"name": "Adult, non-member, afternoon", "age": 30, "is_member": False, "hour": 14},
    {"name": "Child, non-member, afternoon", "age": 8, "is_member": False, "hour": 15},
    {"name": "Senior, member, evening", "age": 70, "is_member": True, "hour": 20},
    {"name": "Adult, member, evening", "age": 35, "is_member": True, "hour": 19},
    {"name": "Child, member, morning", "age": 10, "is_member": True, "hour": 10},
]

print("=== Cinema ticket pricing ===\n")

for case in test_cases:
    name = case["name"]
    age = case["age"]
    is_member = case["is_member"]
    hour = case["hour"]

    price = BASE_PRICE
    details = []

    # Age discount
    if age < 12:
        discount = price * 0.50
        price -= discount
        details.append(f"child discount: -${discount:.2f}")
    elif age >= 65:
        discount = price * 0.30
        price -= discount
        details.append(f"senior discount: -${discount:.2f}")

    # Membership discount
    if is_member:
        price -= 2.00
        details.append("member discount: -$2.00")

    # Evening surcharge
    if hour >= 18:
        price += 3.00
        details.append("evening surcharge: +$3.00")

    # Ensure minimum price
    if price < 0:
        price = 0.00

    # Display
    print(f"  {name}")
    print(f"    Base: ${BASE_PRICE:.2f}")
    for detail in details:
        print(f"    {detail}")
    print(f"    Final: ${price:.2f}")
    print()
```

4. Save and run with F5. Verify each test case produces the expected price.

**Verification**: The adult afternoon ticket is $12.00 (no discounts). The child afternoon ticket is $6.00 (50% off). The senior member evening ticket is $8.40 - $2.00 + $3.00 = $9.40. Each case shows a breakdown of applied rules.

**Expected output**: Five blocks of output, each showing the case name, base price, any discounts/surcharges, and the final price. The details vary based on which rules apply.

**Try it yourself**:
- Add a "student" category (ages 12-25) with a 20% discount
- Add a "group discount" (5+ tickets): 10% off the final price for each ticket
- Convert the logic into an interactive program where the user enters age, membership, and show time

---

## 7. Validation checklist

- [ ] `grades.py` maps each score to the correct letter grade with the plus/minus scale
- [ ] `converter.py` presents a repeating menu and handles all choices correctly, including invalid input
- [ ] `registration.py` collects all validation errors and displays them together
- [ ] `ticket_price.py` applies age, membership, and time-based pricing rules correctly
- [ ] You understand the difference between `if/elif/else` (one branch executes) and multiple `if` statements (all matching branches execute)
- [ ] You can combine conditions with `and`, `or`, and `not`

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: expected ':'` | Missing colon after `if`, `elif`, or `else` | Add `:` at the end of the condition line |
| `IndentationError: expected an indented block` | No code inside the `if` block | Add at least one indented statement (or `pass` as placeholder) |
| `TypeError: '<' not supported between 'str' and 'int'` | Comparing `input()` result (string) to a number | Convert with `int()` or `float()` first |
| Grade always returns "C" or lower | `elif` conditions in wrong order | Check from highest to lowest: `>= 90`, then `>= 80`, etc. |
| Condition always `True` or always `False` | Logic error with `and`/`or` | Test each sub-condition separately in the REPL |

**Common beginner pitfalls:**
- Using `=` instead of `==` in a condition. `if x = 5:` is a syntax error; use `if x == 5:`.
- Writing `if score >= 60 and <= 69:` instead of `if score >= 60 and score <= 69:`. Each side of `and`/`or` must be a complete expression.
- Forgetting that `elif` is checked only if all previous conditions were `False`. The order of `elif` branches matters.
- Using `input()` without converting: `if choice == 1:` will never match because `input()` returns a string. Use `if choice == "1":` or convert with `int()`.

---

## 9. Questions

1. You write an `if/elif/else` chain with five branches. Your colleague rewrites it as five separate `if` statements (no `elif`). The results differ for some inputs. Explain why, and describe a scenario where the difference matters.

2. Python evaluates `and` and `or` using short-circuit evaluation. Explain what this means and provide an example where short-circuiting prevents an error that would otherwise occur.

3. In the registration exercise, we collected all errors in a list before displaying them. An alternative approach would be to check each field and immediately return (or print) on the first error. Compare these two approaches from the user's perspective and the programmer's perspective.

4. The expression `not (age >= 18 and age <= 65)` can be rewritten as `age < 18 or age > 65` (De Morgan's law). Which version is more readable and why? Are there situations where using `not` with a compound condition is clearer?

5. Python treats certain values as "falsy" (`0`, `""`, `[]`, `None`, `False`) and all others as "truthy". Explain how this feature simplifies input validation. For example, what does `if not name:` do, and why is it preferable to `if name == ""`?

6. You are designing a discount system: members get 10% off, orders over $100 get 15% off, and if both apply, the customer gets 20% off (not 25%). How would you structure the `if/elif/else` logic? What happens if you apply the discounts independently?

7. A program checks `if temperature > 30 and humidity > 80:` to issue a heat warning. Under what circumstances would `or` be more appropriate than `and`? How does changing the operator affect when warnings are issued?

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\grades.py`
- `C:\labs\converter.py`
- `C:\labs\registration.py`
- `C:\labs\ticket_price.py`

These files demonstrate conditional logic patterns you will use throughout the course.

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- `if` executes a block when its condition is `True`; `else` handles the opposite case
- `elif` adds additional branches — only the first matching branch executes
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and` (both true), `or` (at least one true), `not` (inverts)
- The order of `elif` branches matters — Python checks top to bottom
- `input()` returns a string — compare with strings (`"1"`) or convert to int/float
- Collecting errors in a list allows showing all validation issues at once
- Python's truthiness means `if not name:` catches empty strings, `None`, and other falsy values
- Multiple separate `if` statements check independently; `if/elif/else` checks one path

---

## 12. Additional resources

- Python `if` statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements
- Truth value testing: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
- Comparison operations: https://docs.python.org/3/library/stdtypes.html#comparisons
- Boolean operations: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- PEP 8 — Style guide for Python code: https://peps.python.org/pep-0008/

---

## 13. Appendices

### Appendix A: Quick reference — Comparison operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 6` | `False` |

### Appendix B: Quick reference — Logical operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both true | `True and False` | `False` |
| `or` | At least one true | `True or False` | `True` |
| `not` | Invert | `not True` | `False` |

**Precedence** (highest to lowest): `not` → `and` → `or`

Use parentheses to make complex conditions explicit: `(a and b) or c`.

### Appendix C: Truthiness / falsiness

| Falsy values | Truthy values |
|-------------|---------------|
| `False` | `True` |
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]` (empty list) | Any non-empty list |
| `{}` (empty dict) | Any non-empty dict |
| `None` | Everything else |

### Appendix D: Conditional patterns

```python
# Pattern 1: Simple check
if condition:
    action()

# Pattern 2: Either/or
if condition:
    action_a()
else:
    action_b()

# Pattern 3: Multi-branch
if condition_1:
    action_1()
elif condition_2:
    action_2()
elif condition_3:
    action_3()
else:
    default_action()

# Pattern 4: Guard clause (validate early, return or continue)
if not valid_input:
    print("Error")
else:
    # proceed with valid input
    process(input)
```

---

## 14. Answers

**Answer 1:**

With `if/elif/else`, only the first matching branch executes. Once Python finds a true condition, it skips all remaining `elif` and `else` branches. This is efficient and ensures mutual exclusivity.

With five separate `if` statements, each condition is checked independently. If multiple conditions are true, multiple blocks execute. For example, in a grading system: `if score >= 90: grade = "A"` followed by `if score >= 80: grade = "B"` — a score of 95 satisfies both conditions, so `grade` would first be set to "A" then overwritten to "B". The final result would be wrong.

This matters whenever conditions overlap. If each condition describes a mutually exclusive case (like grade ranges), `if/elif/else` is correct. Separate `if` statements are appropriate only when each condition should be checked independently (like applying multiple independent discounts).

**Answer 2:**

Short-circuit evaluation means Python stops evaluating a compound condition as soon as the result is determined. For `and`, if the left side is `False`, the right side is not evaluated (because `False and anything` is `False`). For `or`, if the left side is `True`, the right side is not evaluated.

A practical example: `if my_list and my_list[0] > 10:`. If `my_list` is empty (falsy), Python short-circuits and never evaluates `my_list[0] > 10`. Without short-circuiting, accessing `my_list[0]` on an empty list would raise an `IndexError`. This pattern — checking if a collection is non-empty before accessing its elements — is common and relies on short-circuit evaluation.

Similarly, `if divisor != 0 and numerator / divisor > 5:` prevents a `ZeroDivisionError` when `divisor` is zero.

**Answer 3:**

From the user's perspective, collecting all errors is better. If a form has three mistakes, the user sees all three at once and can fix them in a single attempt. With "stop at first error", the user fixes one problem, resubmits, discovers the next error, fixes it, resubmits again — a frustrating cycle.

From the programmer's perspective, collecting errors requires a more complex structure (a list to accumulate errors, then a final check). The "stop at first error" approach is simpler — each check can immediately print a message and exit. However, the collection approach scales better: you can later add severity levels, group errors by field, or even provide auto-fix suggestions.

In practice, web forms and APIs almost always collect and return all validation errors at once. The extra complexity is justified by the improved user experience.

**Answer 4:**

The expression `age < 18 or age > 65` is more readable for most people because it directly states the boundary conditions: "younger than 18 or older than 65." You can visualise a number line with the valid range (18–65) and the two excluded regions.

`not (age >= 18 and age <= 65)` requires the reader to mentally invert the condition. They must first understand "age is between 18 and 65", then negate it. This extra mental step makes it harder to parse quickly.

Using `not` with a compound condition is sometimes clearer when the positive version is the natural way to think about it. For example, `not (is_admin and has_permission)` might read more naturally than `not is_admin or not has_permission` in a security context where the combined condition "is an authorized admin" is a well-understood concept.

**Answer 5:**

Python's truthiness allows concise validation without explicit comparison. `if not name:` catches empty strings (`""`), strings with only whitespace after `.strip()`, and `None` — all cases where a name is effectively missing. Writing `if name == "":` catches only the exact empty string and would miss `None` or other falsy values.

For lists, `if not my_list:` is Pythonic for "if the list is empty". For numbers, `if not count:` means "if count is zero or None." This pattern reduces boilerplate and lets you write conditions that naturally express intent: "if there is no name" rather than "if the name equals an empty string."

The PEP 8 style guide explicitly recommends using truthiness for empty collection checks: write `if not my_list:` rather than `if len(my_list) == 0:`.

**Answer 6:**

You need an `if/elif/else` structure that checks the combined condition first:

```python
if is_member and order > 100:
    discount = 0.20  # Combined: 20%
elif order > 100:
    discount = 0.15  # Order size only
elif is_member:
    discount = 0.10  # Membership only
else:
    discount = 0.00
```

The combined condition must come first because `if/elif` stops at the first match. If you checked `is_member` first, a member with a $150 order would get 10% instead of 20%.

If you applied the discounts independently (10% then 15%), a member with a $100+ order would get both: the price would drop to 90% × 85% = 76.5% of the original — a 23.5% discount, not 20%. The business rule says 20%, so independent application gives the wrong result. This illustrates why understanding the difference between exclusive (`elif`) and independent (`if`) branches is critical.

**Answer 7:**

With `and`, the warning triggers only when both conditions are true simultaneously — temperature above 30 AND humidity above 80. This is appropriate for a "heat index" warning where the combination is dangerous.

With `or`, the warning triggers when either condition is true — temperature above 30 OR humidity above 80. This produces far more warnings because each condition alone is sufficient.

Changing from `and` to `or` dramatically broadens the alert criteria. A hot but dry day (35°C, 40% humidity) would trigger with `or` but not with `and`. A cool but humid day (25°C, 90% humidity) would also trigger with `or`. The choice depends on what hazard you are warning about: if the combination is dangerous, use `and`; if either condition alone is a concern, use `or`.

---

## 15. Code solutions

### Exercise 2.3.1: grades.py (plus/minus version)

```python
# grades.py - Convert percentage scores to letter grades

scores = [95, 82, 67, 73, 58, 90, 45, 88, 100, 71]

print("=== Grade report ===\n")
print(f"  {'Score':>5}  Grade")
print(f"  {'-' * 5}  -----")

for score in scores:
    if score >= 97:
        grade = "A+"
    elif score >= 93:
        grade = "A"
    elif score >= 90:
        grade = "A-"
    elif score >= 87:
        grade = "B+"
    elif score >= 83:
        grade = "B"
    elif score >= 80:
        grade = "B-"
    elif score >= 77:
        grade = "C+"
    elif score >= 73:
        grade = "C"
    elif score >= 70:
        grade = "C-"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"  {score:>5}  {grade}")

# Summary statistics
print()
a_count = sum(1 for s in scores if s >= 90)
passing = sum(1 for s in scores if s >= 60)
print(f"  A grades: {a_count}")
print(f"  Passing (D or above): {passing} out of {len(scores)}")
print(f"  Average: {sum(scores) / len(scores):.1f}")
```

### Exercise 2.3.2: converter.py

```python
# converter.py - Unit converter with repeating menu

print("=== Unit converter ===")

while True:
    print()
    print("  1. Celsius to Fahrenheit")
    print("  2. Kilometers to miles")
    print("  3. Kilograms to pounds")
    print("  4. Quit")
    print()

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        value_str = input("Enter temperature in Celsius: ")
        celsius = float(value_str)
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"\n  Result: {celsius}°C = {fahrenheit:.1f}°F")

    elif choice == "2":
        value_str = input("Enter distance in kilometers: ")
        km = float(value_str)
        miles = km * 0.621371
        print(f"\n  Result: {km} km = {miles:.2f} miles")

    elif choice == "3":
        value_str = input("Enter weight in kilograms: ")
        kg = float(value_str)
        pounds = kg * 2.20462
        print(f"\n  Result: {kg} kg = {pounds:.2f} lbs")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print(f"\n  '{choice}' is not a valid option. Please enter 1, 2, 3, or 4.")
```

### Exercise 2.3.3: registration.py

```python
# registration.py - Event registration with input validation

print("=== Event registration ===\n")

name = input("Full name: ").strip()
age_str = input("Age: ").strip()
email = input("Email: ").strip()

# Validate each field
errors = []

if not name:
    errors.append("Name cannot be empty.")

if not age_str.isdigit():
    errors.append("Age must be a whole number.")
else:
    age = int(age_str)
    if age < 18 or age > 65:
        errors.append(f"Age must be between 18 and 65 (you entered {age}).")

if "@" not in email or "." not in email:
    errors.append("Email must contain '@' and '.' (e.g., user@example.com).")

# Show results
print()
if errors:
    print("Registration FAILED. Please fix the following:")
    for error in errors:
        print(f"  - {error}")
else:
    age = int(age_str)
    print("Registration successful!")
    print(f"  Name:  {name}")
    print(f"  Age:   {age}")
    print(f"  Email: {email}")
```

### Exercise 2.3.4: ticket_price.py

```python
# ticket_price.py - Cinema ticket pricing

BASE_PRICE = 12.00

test_cases = [
    {"name": "Adult, non-member, afternoon", "age": 30, "is_member": False, "hour": 14},
    {"name": "Child, non-member, afternoon", "age": 8, "is_member": False, "hour": 15},
    {"name": "Senior, member, evening", "age": 70, "is_member": True, "hour": 20},
    {"name": "Adult, member, evening", "age": 35, "is_member": True, "hour": 19},
    {"name": "Child, member, morning", "age": 10, "is_member": True, "hour": 10},
]

print("=== Cinema ticket pricing ===\n")

for case in test_cases:
    name = case["name"]
    age = case["age"]
    is_member = case["is_member"]
    hour = case["hour"]

    price = BASE_PRICE
    details = []

    # Age discount
    if age < 12:
        discount = price * 0.50
        price -= discount
        details.append(f"child discount: -${discount:.2f}")
    elif age >= 65:
        discount = price * 0.30
        price -= discount
        details.append(f"senior discount: -${discount:.2f}")

    # Membership discount
    if is_member:
        price -= 2.00
        details.append("member discount: -$2.00")

    # Evening surcharge
    if hour >= 18:
        price += 3.00
        details.append("evening surcharge: +$3.00")

    # Ensure minimum price
    if price < 0:
        price = 0.00

    # Display
    print(f"  {name}")
    print(f"    Base: ${BASE_PRICE:.2f}")
    for detail in details:
        print(f"    {detail}")
    print(f"    Final: ${price:.2f}")
    print()
```
