# Lab 2.1: Working with lists and tuples

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Create lists, access elements by index, and extract sub-lists with slicing
- Modify lists using `append()`, `insert()`, `remove()`, `pop()`, and `sort()`
- Use `enumerate()` to iterate over a list with numbered indices
- Create tuples and use tuple unpacking to assign multiple variables at once
- Choose between a list and a tuple based on whether data should change

---

## 3. Prerequisites

**Knowledge prerequisites**: Variables, data types, basic operators, strings, and f-strings (Day 1 material).

**Previous labs**: Labs 1.1 through 1.4 completed.

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

Programs rarely work with a single value. A shopping list has many items. A class has many students. A log file has many entries. Python's **lists** let you store multiple values in a single variable and work with them as a group — adding, removing, sorting, and slicing as needed.

Sometimes data should not change after creation. GPS coordinates, RGB colour values, and database records are fixed by nature. Python's **tuples** serve this purpose — they look like lists but cannot be modified. This immutability signals intent ("this data is final") and prevents accidental changes.

In this lab, you will build a to-do list application step by step, exploring list operations along the way. You will then work with tuples to store fixed records and practise unpacking them into individual variables.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Explore list creation, indexing, and slicing interactively
- Build a to-do list manager that adds, removes, sorts, and displays numbered items
- Store fixed records as tuples and unpack them into variables
- Combine lists and tuples in a practical mini-application

---

### Exercise 2.1.1: Explore lists in the REPL

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Create lists, access elements by index, and use slicing to extract sub-lists.

**Scenario**: Before building a full application, you want to understand how Python lists behave. The REPL is ideal for quick exploration.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Create a list and inspect it:

```python
>>> fruits = ["apple", "banana", "cherry", "date", "elderberry"]
>>> fruits
['apple', 'banana', 'cherry', 'date', 'elderberry']
>>> len(fruits)
5
>>> type(fruits)
<class 'list'>
```

3. Access individual elements by index (indices start at 0):

```python
>>> fruits[0]
'apple'
>>> fruits[2]
'cherry'
>>> fruits[-1]
'elderberry'
>>> fruits[-2]
'date'
```

4. Use slicing to extract sub-lists:

```python
>>> fruits[1:3]
['banana', 'cherry']
>>> fruits[:3]
['apple', 'banana', 'cherry']
>>> fruits[2:]
['cherry', 'date', 'elderberry']
>>> fruits[::2]
['apple', 'cherry', 'elderberry']
>>> fruits[::-1]
['elderberry', 'date', 'cherry', 'banana', 'apple']
```

5. Modify the list:

```python
>>> fruits.append("fig")
>>> fruits
['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

>>> fruits.insert(1, "blueberry")
>>> fruits
['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig']

>>> fruits.remove("date")
>>> fruits
['apple', 'blueberry', 'banana', 'cherry', 'elderberry', 'fig']

>>> last = fruits.pop()
>>> last
'fig'
>>> fruits
['apple', 'blueberry', 'banana', 'cherry', 'elderberry']
```

6. Sort and check membership:

```python
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'blueberry', 'cherry', 'elderberry']

>>> "cherry" in fruits
True
>>> "mango" in fruits
False
```

7. Create a list of numbers and use `sorted()` (non-destructive):

```python
>>> scores = [85, 92, 78, 95, 88]
>>> sorted(scores)
[78, 85, 88, 92, 95]
>>> scores
[85, 92, 78, 95, 88]
>>> sorted(scores, reverse=True)
[95, 92, 88, 85, 78]
```

8. Exit the REPL:

```python
>>> exit()
```

**Verification**: You created a list, accessed elements by positive and negative index, extracted sub-lists with slicing, modified the list with append/insert/remove/pop, sorted it, and checked membership with `in`.

**Expected output**: Each command returns the expected value. Slicing produces the correct sub-list. After `sort()`, the list is in alphabetical order. Membership checks return `True` or `False` correctly.

**Try it yourself**:
- Create a list of numbers and try `sum()`, `min()`, and `max()` on it
- Try `fruits.index("cherry")` to find the position of an element
- What happens if you access `fruits[100]`? Read the error message carefully.

---

### Exercise 2.1.2: Build a to-do list manager

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Build a script that manages a to-do list using list operations and `enumerate()`.

**Scenario**: You want a simple to-do list that starts with a few tasks, lets you add, remove, and sort tasks, and displays numbered items.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `todo.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# todo.py - To-do list manager

tasks = ["Buy groceries", "Write report", "Call dentist", "Clean kitchen"]

print("=== To-do list ===")
print()

# Display numbered tasks using enumerate
for number, task in enumerate(tasks, start=1):
    print(f"  {number}. {task}")

print()
print(f"Total tasks: {len(tasks)}")
```

3. Save and run with F5. You should see a numbered list of four tasks.

4. Now extend the script. Replace the content with the full manager:

```python
# todo.py - To-do list manager (extended)

tasks = ["Buy groceries", "Write report", "Call dentist", "Clean kitchen"]


def show_tasks(task_list):
    """Display all tasks with numbers."""
    if not task_list:
        print("  (no tasks)")
        return
    for number, task in enumerate(task_list, start=1):
        print(f"  {number}. {task}")
    print(f"\n  Total: {len(task_list)} task(s)")


print("=== To-do list manager ===")
print()

# Show original list
print("Current tasks:")
show_tasks(tasks)

# Add tasks
print("\n--- Adding tasks ---")
tasks.append("Pay electricity bill")
tasks.append("Read chapter 5")
show_tasks(tasks)

# Insert a high-priority task at the top
print("\n--- Inserting urgent task at position 1 ---")
tasks.insert(0, "URGENT: Submit tax forms")
show_tasks(tasks)

# Remove a completed task
print("\n--- Completing 'Call dentist' ---")
tasks.remove("Call dentist")
show_tasks(tasks)

# Remove the last task
print("\n--- Removing last task ---")
removed = tasks.pop()
print(f"  Removed: {removed}")
show_tasks(tasks)

# Sort alphabetically
print("\n--- Sorted list ---")
tasks.sort()
show_tasks(tasks)

# Extract first 3 tasks as a "priority" sub-list
print("\n--- Top 3 priority tasks (first 3 after sorting) ---")
priority = tasks[:3]
show_tasks(priority)
```

5. Save and run with F5.

**Verification**: The script displays the list after each operation. The count updates correctly. The urgent task appears at position 1. "Call dentist" disappears after removal. The sorted list is alphabetical. The priority sub-list contains exactly three items.

**Expected output**: Multiple sections of output, each showing the task list after an operation. The total count changes with each add/remove. After sorting, tasks appear in alphabetical order.

**Try it yourself**:
- Add a feature that removes a task by its number (index) instead of its name
- Use `tasks.reverse()` to show the list in reverse order
- Try `tasks.count("Buy groceries")` to count how many times a task appears

---

### Exercise 2.1.3: Working with tuples and unpacking

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Create tuples, use tuple unpacking, and store fixed records.

**Scenario**: You have a list of employees with fixed data (name, department, salary). Each record should not be modified accidentally, so you store them as tuples.

**Tasks**:

1. In VS Code, create a new file. Save it as `records.py` in `C:\labs`.

2. Type the following code:

```python
# records.py - Working with tuples

# A single tuple
point = (10, 20)
print(f"Point: {point}")
print(f"X: {point[0]}, Y: {point[1]}")
print()

# Tuple unpacking
x, y = point
print(f"Unpacked - X: {x}, Y: {y}")
print()

# Employee records as a list of tuples
employees = [
    ("Alice", "Engineering", 75000),
    ("Bob", "Marketing", 62000),
    ("Charlie", "Engineering", 80000),
    ("Diana", "Sales", 58000),
    ("Eve", "Marketing", 65000),
]

print("=== Employee records ===")
print()

for name, department, salary in employees:
    print(f"  {name:<10} {department:<15} ${salary:>8,}")

print()

# Use enumerate for numbered display
print("Numbered list:")
for i, (name, department, salary) in enumerate(employees, start=1):
    print(f"  {i}. {name} ({department}) - ${salary:,}")

print()

# Sorting tuples - by salary (third element)
by_salary = sorted(employees, key=lambda emp: emp[2], reverse=True)
print("Sorted by salary (highest first):")
for name, department, salary in by_salary:
    print(f"  {name}: ${salary:,}")

print()

# Filtering - only Engineering department
engineering = [emp for emp in employees if emp[1] == "Engineering"]
print("Engineering department:")
for name, department, salary in engineering:
    print(f"  {name}: ${salary:,}")
```

3. Save and run with F5.

4. Try modifying a tuple to see what happens. Add this at the end of the script:

```python
# Uncomment the next line to see the error:
# employees[0][2] = 90000  # TypeError: tuples are immutable
```

Uncomment the line, run the script, and read the error message. Then comment it out again.

**Verification**: The script displays employee records in aligned columns, a numbered list, a salary-sorted list, and a filtered list. Attempting to modify a tuple raises a `TypeError`.

**Expected output**: Four sections of output. The salary column should be right-aligned with comma separators. The sorted list shows Charlie first (highest salary). The Engineering filter shows only Alice and Charlie.

**Hints**:
- The `lambda emp: emp[2]` expression tells `sorted()` to use the third element (salary) as the sort key
- The `:,` format specifier adds comma separators to numbers (e.g., `75,000`)
- The list comprehension `[emp for emp in employees if ...]` filters based on a condition

**Try it yourself**:
- Add a total salary calculation using `sum()` and a generator expression
- Sort employees by name instead of salary
- Create a tuple of tuples (instead of a list of tuples) and think about when you would choose one over the other

---

### Exercise 2.1.4: To-do list with categories

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Combine lists and tuples to build a categorized task tracker.

**Scenario**: Your to-do list has grown. You want to tag each task with a category (work, personal, errands) and display them grouped.

**Tasks**:

1. In VS Code, create a new file. Save it as `categorized_tasks.py` in `C:\labs`.

2. Write a script that:
   - Stores tasks as a list of tuples: `(task_name, category)`
   - Uses a loop with unpacking to group and display tasks by category
   - Shows a count of tasks per category

**Hints**:
- Start with a list of 8-10 task tuples with 3 categories
- Use `sorted()` with a `key` to sort by category
- Use a variable to track the current category and print a header when it changes

3. Here is a starting structure to build on:

```python
# categorized_tasks.py - Tasks grouped by category

tasks = [
    ("Buy groceries", "errands"),
    ("Finish project proposal", "work"),
    ("Call plumber", "errands"),
    ("Read Python chapter", "personal"),
    ("Send invoice", "work"),
    ("Go for a run", "personal"),
    ("Pick up dry cleaning", "errands"),
    ("Review pull request", "work"),
]

# Sort tasks by category
tasks_sorted = sorted(tasks, key=lambda t: t[1])

# Display grouped by category
print("=== Tasks by category ===\n")
current_category = ""

for task, category in tasks_sorted:
    if category != current_category:
        current_category = category
        print(f"\n  [{current_category.upper()}]")
    print(f"    - {task}")

# Count per category
print("\n\n=== Summary ===")
categories = [category for _, category in tasks]
for cat in sorted(set(categories)):
    count = categories.count(cat)
    print(f"  {cat}: {count} task(s)")

print(f"\n  Total: {len(tasks)} task(s)")
```

4. Save and run with F5. Verify that tasks appear grouped under their category heading and the summary counts are correct.

**Verification**: Tasks are grouped by category in alphabetical order. Each category has a header. The summary shows the correct count for each category.

**Expected output**: Three category groups (errands, personal, work) with their tasks listed below each header. The summary shows the count for each category and the total.

**Try it yourself**:
- Add a "priority" element to each tuple (high/medium/low) and sort within each category by priority
- Add a new task interactively using `input()` and append it to the list
- Use `enumerate()` to give each task a global number across all categories

---

## 7. Validation checklist

- [ ] You can create a list, access elements by index, and extract sub-lists with slicing
- [ ] `todo.py` adds, removes, inserts, and sorts tasks correctly
- [ ] You can use `enumerate()` to display numbered items
- [ ] `records.py` displays employee records sorted and filtered
- [ ] You understand that tuples are immutable — attempting to change one raises a `TypeError`
- [ ] `categorized_tasks.py` groups tasks by category and displays correct counts

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `IndexError: list index out of range` | Accessing an index beyond the list length | Check `len()` first. Remember: a 5-element list has indices 0-4. |
| `ValueError: list.remove(x): x not in list` | Trying to remove an element that does not exist | Check with `if item in my_list:` before calling `remove()` |
| `TypeError: 'tuple' object does not support item assignment` | Trying to modify a tuple element | Tuples are immutable. Use a list if you need to change values. |
| `ValueError: not enough values to unpack` | Tuple unpacking with wrong number of variables | Ensure the number of variables matches the tuple length |
| `TypeError: '<' not supported between instances of 'str' and 'int'` | Sorting a list with mixed types | Ensure all elements have the same type, or provide a `key` function |

**Common beginner pitfalls:**
- Forgetting that indices start at 0. The first element is `my_list[0]`, not `my_list[1]`.
- Confusing `sort()` (modifies the list in place, returns `None`) with `sorted()` (returns a new sorted list, original unchanged).
- Writing `my_list = my_list.sort()` — this sets `my_list` to `None` because `sort()` returns `None`.
- Using `append()` with a list argument adds the entire list as a single element. Use `extend()` to add individual elements from another list.

---

## 9. Questions

1. You have a program that stores a user's five most recent search queries. Should you use a list or a tuple? Now imagine a different program that stores the latitude and longitude of a city. Which would you choose for that? Explain your reasoning for both cases.

2. The expression `my_list[1:4]` returns elements at indices 1, 2, and 3, but not 4. Why do you think Python was designed with this "start-inclusive, end-exclusive" convention? What practical advantages does it provide?

3. A colleague writes `sorted_list = tasks.sort()` and later prints `sorted_list`, getting `None`. Explain what happened and how to fix it. Why does Python design `.sort()` to return `None` instead of the sorted list?

4. You have a list of 10,000 items and need to frequently check if a specific value exists. You use `if value in my_list:` and notice the program is slow. What is happening under the hood, and what alternative data structure (from Chapter 2.2) might be more efficient for this purpose?

5. Explain the difference between `my_list.append([4, 5, 6])` and `my_list.extend([4, 5, 6])`. If you started with `my_list = [1, 2, 3]`, what would the list contain after each operation?

6. When you unpack a tuple with `name, department, salary = employee`, Python assigns each element to the corresponding variable. What would happen if you tried to unpack a tuple of three elements into two variables? Why is this a useful safety feature?

7. Consider a function that returns multiple values: `return min_val, max_val, average`. What is Python actually returning here, and why is tuple unpacking a natural fit for working with the result?

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\todo.py`
- `C:\labs\records.py`
- `C:\labs\categorized_tasks.py`

These files are small and will serve as reference examples for list and tuple operations.

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- Lists are ordered, mutable collections: create with `[]`, access by index, modify freely
- Indices start at 0; negative indices count from the end (`-1` is the last element)
- Slicing syntax `[start:end:step]` extracts sub-lists without modifying the original
- `append()` adds to the end, `insert()` adds at a position, `remove()` deletes by value, `pop()` removes and returns
- `sort()` modifies the list in place (returns `None`); `sorted()` returns a new list
- `in` checks membership: `"apple" in fruits` returns `True` or `False`
- `enumerate()` gives you both the index and the value in a loop
- Tuples are immutable — use them for data that should not change
- Tuple unpacking (`a, b, c = my_tuple`) assigns each element to a variable in one line

---

## 12. Additional resources

- Python lists: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- Python tuples: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- Built-in `sorted()` function: https://docs.python.org/3/library/functions.html#sorted
- `enumerate()` function: https://docs.python.org/3/library/functions.html#enumerate
- PEP 8 — Style guide for Python code: https://peps.python.org/pep-0008/

---

## 13. Appendices

### Appendix A: Quick reference — List operations

| Operation | Syntax | Effect |
|-----------|--------|--------|
| Create | `my_list = [1, 2, 3]` | New list with three elements |
| Access | `my_list[0]` | First element |
| Negative index | `my_list[-1]` | Last element |
| Slice | `my_list[1:3]` | Elements at index 1 and 2 |
| Length | `len(my_list)` | Number of elements |
| Append | `my_list.append(4)` | Add to end |
| Insert | `my_list.insert(0, "x")` | Add at position |
| Remove | `my_list.remove("x")` | Remove first occurrence |
| Pop | `my_list.pop()` | Remove and return last |
| Sort (in place) | `my_list.sort()` | Sort, returns `None` |
| Sorted (new) | `sorted(my_list)` | Returns new sorted list |
| Membership | `"x" in my_list` | `True` / `False` |
| Enumerate | `enumerate(my_list, start=1)` | Yields `(index, value)` pairs |

### Appendix B: Quick reference — Tuple operations

| Operation | Syntax | Effect |
|-----------|--------|--------|
| Create | `t = (1, 2, 3)` | New tuple |
| Single element | `t = (1,)` | Note the trailing comma |
| Access | `t[0]` | First element |
| Unpack | `a, b, c = t` | Assign each element |
| Length | `len(t)` | Number of elements |
| Membership | `1 in t` | `True` / `False` |
| Concatenate | `t1 + t2` | New tuple combining both |

### Appendix C: Slice notation

| Notation | Meaning | Example with `[0,1,2,3,4]` | Result |
|----------|---------|----------------------------|--------|
| `[a:b]` | From a (inclusive) to b (exclusive) | `[1:3]` | `[1, 2]` |
| `[:b]` | From start to b | `[:3]` | `[0, 1, 2]` |
| `[a:]` | From a to end | `[2:]` | `[2, 3, 4]` |
| `[::n]` | Every n-th element | `[::2]` | `[0, 2, 4]` |
| `[::-1]` | Reversed | `[::-1]` | `[4, 3, 2, 1, 0]` |

---

## 14. Answers

**Answer 1:**

For the five most recent search queries, a list is the right choice. The data changes over time — new queries are added, old ones are removed. A list supports `append()`, `pop(0)`, and slicing to maintain a rolling window of recent items. You might also want to reorder the list or remove duplicates.

For a city's latitude and longitude, a tuple is more appropriate. These coordinates are fixed facts — Budapest is at (47.4979, 19.0402), and that should never change during program execution. A tuple signals this intent. Additionally, tuples can be used as dictionary keys (because they are hashable), so you could use `(47.4979, 19.0402)` as a key in a mapping. A list cannot serve as a dictionary key because it is mutable.

The general principle: use a list when the collection will change; use a tuple when the data is fixed.

**Answer 2:**

The start-inclusive, end-exclusive convention has several practical advantages. First, `len(my_list[a:b])` always equals `b - a`, making length calculations simple. Second, adjacent slices can be written without overlap: `my_list[:n]` and `my_list[n:]` together cover the entire list with no duplication and no gap. Third, `my_list[:n]` gives the first n elements, which is intuitive.

This convention is consistent across Python — `range(1, 5)` produces `1, 2, 3, 4` using the same logic. Once you internalize it, you avoid off-by-one errors that plague languages with inclusive-both-ends ranges. The design was a deliberate choice by Python's creator, influenced by similar conventions in mathematics (half-open intervals) and the C language.

**Answer 3:**

The `.sort()` method sorts the list in place and returns `None`. This is a Python design convention for methods that modify an object: they return `None` to make it clear that the original object was changed, not a new one created. So `sorted_list = tasks.sort()` sorts `tasks` correctly but assigns `None` to `sorted_list`.

To fix it, either use `tasks.sort()` and then work with `tasks` directly, or use `sorted_list = sorted(tasks)` which returns a new sorted list and leaves `tasks` unchanged. The choice depends on whether you need to keep the original order. This convention prevents a subtle bug: if `.sort()` returned the sorted list, you might mistakenly think it created a new list and that the original was still unsorted.

**Answer 4:**

When you use `if value in my_list:`, Python performs a linear search — it checks each element one by one from the beginning until it finds a match or reaches the end. For 10,000 items, this means up to 10,000 comparisons each time. If you do this check frequently (say, inside a loop that runs thousands of times), the total number of comparisons becomes enormous.

A `set` (covered in Chapter 2.2) stores elements in a hash table, which allows membership checks in roughly constant time regardless of the collection's size. Converting the list to a set with `my_set = set(my_list)` and then using `if value in my_set:` is dramatically faster for repeated lookups. The trade-off is that sets are unordered and do not allow duplicates, so this approach works only when you need fast membership testing, not when you need to preserve order or allow repeated values.

**Answer 5:**

Starting with `my_list = [1, 2, 3]`:

`my_list.append([4, 5, 6])` adds the entire list `[4, 5, 6]` as a single element at the end. The result is `[1, 2, 3, [4, 5, 6]]` — a four-element list where the last element is itself a list (a nested list).

`my_list.extend([4, 5, 6])` adds each element of `[4, 5, 6]` individually. The result is `[1, 2, 3, 4, 5, 6]` — a six-element flat list.

The key distinction is that `append()` always adds one element (whatever you pass), while `extend()` iterates over the argument and adds each item. This is a common source of bugs for beginners — if you want to merge two lists, use `extend()` or the `+` operator (`list1 + list2`), not `append()`.

**Answer 6:**

Python raises a `ValueError: not enough values to unpack (expected 2, got 3)`. The number of variables on the left must match the number of elements in the tuple. This is a useful safety feature because it catches structural mismatches immediately.

Imagine reading records from a file where each line has three fields. If one line is malformed and has only two fields, the unpacking error tells you right away that the data does not match your expected format. Without this check, a missing value would silently shift into the wrong variable, causing incorrect results that are much harder to debug.

Python does support extended unpacking with `*` (for example, `first, *rest = my_tuple`), but that is an explicit opt-in — you must deliberately write the `*` to say "collect the remaining values here."

**Answer 7:**

Python is returning a single tuple. The expression `return min_val, max_val, average` is equivalent to `return (min_val, max_val, average)`. Python automatically packs comma-separated values into a tuple. This is called implicit tuple packing.

Tuple unpacking is a natural fit because you can write `lo, hi, avg = get_stats(data)` at the call site, which reads clearly and gives each value a meaningful name. Without unpacking, you would need to access elements by index (`result[0]`, `result[1]`, `result[2]`), which is less readable and more error-prone.

This pattern is used extensively in the Python standard library. For example, `str.partition()` returns a three-element tuple, and `divmod()` returns a two-element tuple. The combination of implicit packing (in the `return`) and unpacking (at the call site) makes multi-value returns feel natural and lightweight in Python.

---

## 15. Code solutions

### Exercise 2.1.2: todo.py

```python
# todo.py - To-do list manager (extended)

tasks = ["Buy groceries", "Write report", "Call dentist", "Clean kitchen"]


def show_tasks(task_list):
    """Display all tasks with numbers."""
    if not task_list:
        print("  (no tasks)")
        return
    for number, task in enumerate(task_list, start=1):
        print(f"  {number}. {task}")
    print(f"\n  Total: {len(task_list)} task(s)")


print("=== To-do list manager ===")
print()

# Show original list
print("Current tasks:")
show_tasks(tasks)

# Add tasks
print("\n--- Adding tasks ---")
tasks.append("Pay electricity bill")
tasks.append("Read chapter 5")
show_tasks(tasks)

# Insert a high-priority task at the top
print("\n--- Inserting urgent task at position 1 ---")
tasks.insert(0, "URGENT: Submit tax forms")
show_tasks(tasks)

# Remove a completed task
print("\n--- Completing 'Call dentist' ---")
tasks.remove("Call dentist")
show_tasks(tasks)

# Remove the last task
print("\n--- Removing last task ---")
removed = tasks.pop()
print(f"  Removed: {removed}")
show_tasks(tasks)

# Sort alphabetically
print("\n--- Sorted list ---")
tasks.sort()
show_tasks(tasks)

# Extract first 3 tasks as a "priority" sub-list
print("\n--- Top 3 priority tasks (first 3 after sorting) ---")
priority = tasks[:3]
show_tasks(priority)
```

### Exercise 2.1.3: records.py

```python
# records.py - Working with tuples

# A single tuple
point = (10, 20)
print(f"Point: {point}")
print(f"X: {point[0]}, Y: {point[1]}")
print()

# Tuple unpacking
x, y = point
print(f"Unpacked - X: {x}, Y: {y}")
print()

# Employee records as a list of tuples
employees = [
    ("Alice", "Engineering", 75000),
    ("Bob", "Marketing", 62000),
    ("Charlie", "Engineering", 80000),
    ("Diana", "Sales", 58000),
    ("Eve", "Marketing", 65000),
]

print("=== Employee records ===")
print()

for name, department, salary in employees:
    print(f"  {name:<10} {department:<15} ${salary:>8,}")

print()

# Use enumerate for numbered display
print("Numbered list:")
for i, (name, department, salary) in enumerate(employees, start=1):
    print(f"  {i}. {name} ({department}) - ${salary:,}")

print()

# Sorting tuples - by salary (third element)
by_salary = sorted(employees, key=lambda emp: emp[2], reverse=True)
print("Sorted by salary (highest first):")
for name, department, salary in by_salary:
    print(f"  {name}: ${salary:,}")

print()

# Filtering - only Engineering department
engineering = [emp for emp in employees if emp[1] == "Engineering"]
print("Engineering department:")
for name, department, salary in engineering:
    print(f"  {name}: ${salary:,}")
```

### Exercise 2.1.4: categorized_tasks.py

```python
# categorized_tasks.py - Tasks grouped by category

tasks = [
    ("Buy groceries", "errands"),
    ("Finish project proposal", "work"),
    ("Call plumber", "errands"),
    ("Read Python chapter", "personal"),
    ("Send invoice", "work"),
    ("Go for a run", "personal"),
    ("Pick up dry cleaning", "errands"),
    ("Review pull request", "work"),
]

# Sort tasks by category
tasks_sorted = sorted(tasks, key=lambda t: t[1])

# Display grouped by category
print("=== Tasks by category ===\n")
current_category = ""

for task, category in tasks_sorted:
    if category != current_category:
        current_category = category
        print(f"\n  [{current_category.upper()}]")
    print(f"    - {task}")

# Count per category
print("\n\n=== Summary ===")
categories = [category for _, category in tasks]
for cat in sorted(set(categories)):
    count = categories.count(cat)
    print(f"  {cat}: {count} task(s)")

print(f"\n  Total: {len(tasks)} task(s)")
```
