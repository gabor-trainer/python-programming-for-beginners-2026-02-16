# Lab 2.2: Dictionaries and sets in practice

**Estimated time**: 60 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Create dictionaries and access values using bracket notation and `.get()`
- Add, update, and remove key-value pairs in a dictionary
- Iterate over dictionary keys, values, and items
- Create sets and perform set operations (union, intersection, difference)
- Choose the appropriate data structure (list, tuple, dictionary, set) for a given problem

---

## 3. Prerequisites

**Knowledge prerequisites**: Lists, tuples, indexing, slicing, and `enumerate()` (Chapter 2.1).

**Previous labs**: Lab 2.1 completed.

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

Lists are great when you care about order and position. But what if you want to look up a phone number by a person's name? Searching through a list of pairs would be slow and awkward. Python's **dictionaries** solve this: they map **keys** to **values**, giving you instant lookup by name, ID, or any other unique identifier.

Dictionaries are everywhere in real programs: configuration settings (key = setting name, value = setting value), API responses (key = field name, value = data), caches, counters, and more.

Sometimes you only care about unique items — for example, "which words appear in this document?" or "which customers are in both lists?" Python's **sets** store unique elements and support mathematical set operations (union, intersection, difference) that would require many lines of code with lists.

In this lab, you will build a contact book with dictionaries, count word frequencies in a text, and use sets to find common elements between collections.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Explore dictionary creation, access, and iteration interactively
- Build a contact book that stores and retrieves phone numbers by name
- Count word frequencies in a paragraph of text
- Use sets to find common and unique elements between two collections

---

### Exercise 2.2.1: Explore dictionaries in the REPL

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Create dictionaries, access values safely, and iterate over keys, values, and items.

**Scenario**: You want to understand how dictionaries work before building a larger application. The REPL lets you test each operation in isolation.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Create a dictionary and inspect it:

```python
>>> person = {"name": "Alice", "age": 30, "city": "Budapest"}
>>> person
{'name': 'Alice', 'age': 30, 'city': 'Budapest'}
>>> type(person)
<class 'dict'>
>>> len(person)
3
```

3. Access values with bracket notation:

```python
>>> person["name"]
'Alice'
>>> person["age"]
30
```

4. Try accessing a key that does not exist:

```python
>>> person["email"]
```

You will see a `KeyError`. This is expected — the key "email" does not exist in the dictionary.

5. Use `.get()` for safe access:

```python
>>> person.get("email")
>>> person.get("email", "not provided")
'not provided'
>>> person.get("name", "not provided")
'Alice'
```

`.get()` returns `None` (shown as nothing in the REPL) when the key is missing, or a default value if you provide one. It never raises an error.

6. Add and update entries:

```python
>>> person["email"] = "alice@example.com"
>>> person
{'name': 'Alice', 'age': 30, 'city': 'Budapest', 'email': 'alice@example.com'}

>>> person["age"] = 31
>>> person["age"]
31
```

7. Remove entries:

```python
>>> del person["city"]
>>> person
{'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

>>> removed_email = person.pop("email")
>>> removed_email
'alice@example.com'
>>> person
{'name': 'Alice', 'age': 31}
```

8. Check membership:

```python
>>> "name" in person
True
>>> "city" in person
False
```

Note: `in` checks **keys**, not values.

9. Iterate over a dictionary:

```python
>>> scores = {"Alice": 92, "Bob": 85, "Charlie": 78}

>>> for name in scores:
...     print(name)
...
Alice
Bob
Charlie

>>> for name, score in scores.items():
...     print(f"{name}: {score}")
...
Alice: 92
Bob: 85
Charlie: 78

>>> list(scores.keys())
['Alice', 'Bob', 'Charlie']
>>> list(scores.values())
[92, 85, 78]
```

10. Exit the REPL:

```python
>>> exit()
```

**Verification**: You created a dictionary, accessed values with `[]` and `.get()`, added and removed entries, checked key membership, and iterated over keys, values, and items.

**Expected output**: Each operation produces the expected result. `.get()` returns `None` or the default for missing keys. Iteration with `.items()` yields key-value pairs.

**Try it yourself**:
- Create an empty dictionary with `d = {}` and add three key-value pairs one by one
- Try `scores.get("Diana", 0)` and think about why a default of `0` is useful for counting
- What happens if you use a list as a dictionary key? Try `d[[1, 2]] = "test"` and read the error

---

### Exercise 2.2.2: Build a contact book

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Build a contact book that stores names mapped to phone numbers, with lookup, addition, and deletion.

**Scenario**: You need a simple way to store and retrieve phone numbers. A dictionary maps each name (key) to a phone number (value), allowing instant lookup.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `contacts.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# contacts.py - Simple contact book using dictionaries

contacts = {
    "Alice": "+36-20-111-2222",
    "Bob": "+36-30-333-4444",
    "Charlie": "+36-70-555-6666",
}


def show_contacts(book):
    """Display all contacts in a formatted list."""
    if not book:
        print("  (no contacts)")
        return
    for name, phone in sorted(book.items()):
        print(f"  {name:<12} {phone}")
    print(f"\n  Total: {len(book)} contact(s)")


def lookup(book, name):
    """Look up a contact by name using .get() for safe access."""
    phone = book.get(name)
    if phone:
        print(f"  {name}: {phone}")
    else:
        print(f"  '{name}' not found in contacts.")


# Display all contacts
print("=== Contact book ===\n")
show_contacts(contacts)

# Look up contacts
print("\n--- Lookups ---")
lookup(contacts, "Alice")
lookup(contacts, "Diana")

# Add a new contact
print("\n--- Adding Diana ---")
contacts["Diana"] = "+36-20-777-8888"
show_contacts(contacts)

# Update an existing contact
print("\n--- Updating Bob's number ---")
contacts["Bob"] = "+36-30-999-0000"
lookup(contacts, "Bob")

# Remove a contact
print("\n--- Removing Charlie ---")
del contacts["Charlie"]
show_contacts(contacts)

# Safe removal with pop (no error if missing)
print("\n--- Safe removal of 'Eve' (not in contacts) ---")
removed = contacts.pop("Eve", None)
if removed:
    print(f"  Removed Eve: {removed}")
else:
    print("  'Eve' was not in contacts — nothing removed.")
```

3. Save and run with F5.

**Verification**: The script displays contacts alphabetically, looks up existing and missing contacts, adds and updates entries, and removes contacts without errors.

**Expected output**: Multiple sections of output. The initial list has three contacts. After adding Diana, there are four. After removing Charlie, there are three again. The lookup for "Diana" first shows "not found", then succeeds after adding.

**Try it yourself**:
- Add a feature to search contacts by partial name (check if the search term is in the name)
- Store multiple phone numbers per person using a list as the value
- Add an `input()` loop that lets the user type commands like "add", "lookup", "delete", "list", and "quit"

---

### Exercise 2.2.3: Word frequency counter

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Count how many times each word appears in a text using a dictionary.

**Scenario**: You are analysing customer feedback and want to know which words appear most frequently. A dictionary with words as keys and counts as values is the standard approach.

**Tasks**:

1. In VS Code, create a new file. Save it as `word_count.py` in `C:\labs`.

2. Type the following code:

```python
# word_count.py - Count word frequencies in a text

text = """Python is a powerful programming language.
Python is used for web development, data science, and automation.
Learning Python is a great investment for any developer.
Python makes complex tasks simple and simple tasks trivial."""

# Clean and split the text into words
words = text.lower().replace(".", "").replace(",", "").split()

# Count frequencies using a dictionary
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display all words sorted by frequency (highest first)
print("=== Word frequency analysis ===\n")

sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words:
    bar = "#" * count
    print(f"  {word:<15} {count:>2}  {bar}")

print(f"\n  Unique words: {len(frequency)}")
print(f"  Total words:  {len(words)}")
```

3. Save and run with F5.

4. Examine the key line: `frequency[word] = frequency.get(word, 0) + 1`. This uses `.get()` with a default of `0` so that the first occurrence of any word starts counting from 0 + 1 = 1, without raising a `KeyError`.

**Verification**: The output shows each word with its frequency count and a simple bar chart. "python" should have the highest frequency. The unique word count should be less than the total word count.

**Expected output**: A sorted list of words with frequency counts. The most frequent word appears first. Each line shows the word, its count, and a visual bar of `#` characters.

**Hints**:
- `.lower()` normalises case so "Python" and "python" are counted together
- `.replace(".", "").replace(",", "")` removes punctuation before splitting
- `.get(word, 0)` is the key pattern for safe counting — it returns 0 for new words

**Try it yourself**:
- Modify the script to only show words that appear more than once
- Add more punctuation removal (semicolons, exclamation marks, etc.)
- Try counting character frequencies instead of word frequencies

---

### Exercise 2.2.4: Finding common elements with sets

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Use sets to find common, unique, and different elements between collections.

**Scenario**: You have two teams working on a project and want to find which skills overlap, which are unique to each team, and which skills exist across both teams combined.

**Tasks**:

1. In VS Code, create a new file. Save it as `team_skills.py` in `C:\labs`.

2. Type the following code:

```python
# team_skills.py - Compare team skills using sets

team_a_skills = ["Python", "SQL", "Excel", "Git", "Docker", "Python", "SQL"]
team_b_skills = ["JavaScript", "SQL", "React", "Git", "CSS", "SQL", "Git"]

# Convert to sets (duplicates are removed automatically)
skills_a = set(team_a_skills)
skills_b = set(team_b_skills)

print("=== Team skill analysis ===\n")

print(f"Team A skills: {sorted(skills_a)}")
print(f"Team B skills: {sorted(skills_b)}")

# Common skills (intersection)
common = skills_a & skills_b
print(f"\nShared skills:      {sorted(common)}")

# All skills combined (union)
all_skills = skills_a | skills_b
print(f"All skills combined: {sorted(all_skills)}")

# Only in Team A (difference)
only_a = skills_a - skills_b
print(f"Only in Team A:     {sorted(only_a)}")

# Only in Team B (difference)
only_b = skills_b - skills_a
print(f"Only in Team B:     {sorted(only_b)}")

# Skills in one team but not both (symmetric difference)
exclusive = skills_a ^ skills_b
print(f"Exclusive to one:   {sorted(exclusive)}")

# Summary
print(f"\n=== Summary ===")
print(f"  Team A: {len(skills_a)} unique skill(s)")
print(f"  Team B: {len(skills_b)} unique skill(s)")
print(f"  Shared: {len(common)}")
print(f"  Total unique across both: {len(all_skills)}")
```

3. Save and run with F5.

4. Notice that the original lists had duplicates ("Python" twice in Team A, "SQL" and "Git" twice in Team B). Converting to sets removed them automatically.

**Verification**: The output shows the correct set operations. Shared skills should include "SQL" and "Git". Only-A should include "Python", "Excel", "Docker". Only-B should include "JavaScript", "React", "CSS". The union should contain all unique skills from both teams.

**Expected output**: Sorted lists for each operation. The summary shows correct counts. The total unique skills should equal Team A unique + Team B unique - shared.

**Try it yourself**:
- Add a third team and find skills that all three teams share (use `skills_a & skills_b & skills_c`)
- Use `skills_a.issubset(all_skills)` to check if one set is entirely contained in another
- Find how many duplicate entries were removed by comparing `len(team_a_skills)` with `len(skills_a)`

---

## 7. Validation checklist

- [ ] You can create a dictionary, access values with `[]` and `.get()`, and handle missing keys safely
- [ ] `contacts.py` adds, updates, looks up, and removes contacts correctly
- [ ] `word_count.py` counts word frequencies and displays them sorted by frequency
- [ ] You understand the `.get(key, default)` pattern for safe access and counting
- [ ] `team_skills.py` correctly computes intersection, union, and difference of two sets
- [ ] You understand that sets automatically remove duplicates

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `KeyError: 'x'` | Accessing a dictionary key that does not exist with `[]` | Use `.get("x")` or `.get("x", default)` for safe access |
| `TypeError: unhashable type: 'list'` | Using a list as a dictionary key or set element | Use a tuple instead — lists are mutable and cannot be hashed |
| `AttributeError: 'dict' object has no attribute 'add'` | Calling a set method on a dictionary | Dictionaries use `d[key] = value`; sets use `s.add(value)` |
| `TypeError: 'set' object is not subscriptable` | Trying to index a set with `my_set[0]` | Sets are unordered — convert to a list first if you need indexing |
| `ValueError: dictionary update sequence element #0 has length 1` | Passing a string instead of key-value pairs to `dict()` | Use `dict(name="Alice")` or `{"name": "Alice"}` |

**Common beginner pitfalls:**
- Using `[]` on a dictionary without checking if the key exists. Always use `.get()` when the key might be missing.
- Confusing `in` behaviour: for dictionaries, `in` checks keys, not values. To check values, use `value in my_dict.values()`.
- Forgetting that sets are unordered — you cannot rely on elements being in any particular position.
- Trying to put mutable objects (lists, other dictionaries) into a set. Set elements must be hashable (strings, numbers, tuples).

---

## 9. Questions

1. You are building a program to track inventory: product names and their quantities. Would you use a list of tuples `[("apple", 50), ("banana", 30)]` or a dictionary `{"apple": 50, "banana": 30}`? Explain the trade-offs. What operations are easier with each approach?

2. The `.get()` method returns a default value for missing keys instead of raising an error. In what real-world programming scenarios is this behaviour essential? Can you think of a situation where you would actually want the `KeyError` instead?

3. Explain why `frequency.get(word, 0) + 1` works for counting word occurrences. What would happen if you wrote `frequency[word] += 1` instead, and the word had not been seen before? How else could you solve this problem?

4. Sets automatically remove duplicates. Explain why this makes set operations (union, intersection, difference) mathematically clean. What would go wrong if sets allowed duplicates?

5. You need to check whether a username already exists in a system with 100,000 users. Would you store usernames in a list or a set? Explain the performance difference and why it matters at scale.

6. A dictionary's keys must be immutable (strings, numbers, tuples), but its values can be anything. Why do you think Python enforces this restriction on keys? What would go wrong if mutable objects (like lists) were allowed as keys?

7. Compare iterating over a dictionary with `for key in my_dict:` versus `for key, value in my_dict.items():`. When would you use each approach? Is there a performance difference?

---

## 10. Clean-up

Keep all files for future reference:
- `C:\labs\contacts.py`
- `C:\labs\word_count.py`
- `C:\labs\team_skills.py`

These files demonstrate key dictionary and set patterns that you will use frequently.

**Note**: Do NOT uninstall Python or remove any system files.

---

## 11. Key takeaways

- Dictionaries map keys to values: `{"name": "Alice", "age": 30}`
- Access values with `d["key"]` (raises `KeyError` if missing) or `d.get("key", default)` (safe)
- Add/update with `d["key"] = value`; remove with `del d["key"]` or `d.pop("key")`
- Iterate with `for key, value in d.items():` to get both keys and values
- The `.get(key, 0) + 1` pattern is the standard way to count occurrences
- Sets store unique elements: `{1, 2, 3}` or `set(my_list)`
- Set operations: `&` (intersection), `|` (union), `-` (difference), `^` (symmetric difference)
- `in` checks keys for dictionaries and elements for sets — both are fast lookups
- Use a dictionary when you need key-value mapping; use a set when you need unique elements and fast membership testing

---

## 12. Additional resources

- Python dictionaries: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Python sets: https://docs.python.org/3/tutorial/datastructures.html#sets
- Dictionary methods: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
- Set methods: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
- PEP 8 — Style guide for Python code: https://peps.python.org/pep-0008/

---

## 13. Appendices

### Appendix A: Quick reference — Dictionary operations

| Operation | Syntax | Effect |
|-----------|--------|--------|
| Create | `d = {"a": 1, "b": 2}` | New dictionary |
| Access (unsafe) | `d["a"]` | Returns value or raises `KeyError` |
| Access (safe) | `d.get("a", default)` | Returns value or default |
| Add / Update | `d["c"] = 3` | Adds new or updates existing |
| Delete | `del d["a"]` | Removes key-value pair |
| Pop | `d.pop("a", None)` | Removes and returns value |
| Membership | `"a" in d` | Checks if key exists |
| Keys | `d.keys()` | View of all keys |
| Values | `d.values()` | View of all values |
| Items | `d.items()` | View of `(key, value)` pairs |
| Length | `len(d)` | Number of key-value pairs |

### Appendix B: Quick reference — Set operations

| Operation | Syntax | Equivalent method | Effect |
|-----------|--------|-------------------|--------|
| Create | `s = {1, 2, 3}` | — | New set |
| From list | `s = set([1, 2, 2, 3])` | — | `{1, 2, 3}` (deduped) |
| Add | `s.add(4)` | — | Add element |
| Remove | `s.remove(4)` | — | Remove (error if missing) |
| Discard | `s.discard(4)` | — | Remove (no error if missing) |
| Union | `a \| b` | `a.union(b)` | All elements from both |
| Intersection | `a & b` | `a.intersection(b)` | Common elements |
| Difference | `a - b` | `a.difference(b)` | In a but not in b |
| Symmetric diff | `a ^ b` | `a.symmetric_difference(b)` | In one but not both |
| Membership | `x in s` | — | Fast lookup |

### Appendix C: Choosing the right data structure

| Need | Data structure | Reason |
|------|---------------|--------|
| Ordered collection, may change | List | Indexed, mutable, allows duplicates |
| Fixed collection of related values | Tuple | Immutable, can be dict key / set element |
| Key-value mapping | Dictionary | Fast lookup by key |
| Unique elements, membership testing | Set | Auto-deduplication, fast `in` |

---

## 14. Answers

**Answer 1:**

A list of tuples preserves insertion order and allows duplicates (you could have two entries for "apple" with different quantities). It is a good choice if you need to iterate over items in a specific order or store a log of inventory changes. However, looking up a product by name requires a linear search through all tuples — slow for large inventories.

A dictionary gives instant lookup by product name. `inventory["apple"]` returns the quantity immediately, regardless of how many products are stored. Adding, updating, and removing products is straightforward: `inventory["apple"] = 50`. The trade-off is that dictionary keys must be unique, so you can only store one quantity per product name (which is usually what you want for current inventory).

For a real inventory system, a dictionary is almost always the better choice because the primary operation (look up quantity by product name) is exactly what dictionaries optimise for.

**Answer 2:**

The `.get()` method is essential whenever a missing key is a normal, expected situation — not an error. For example, when counting word frequencies, most words will not be in the dictionary the first time they appear. Using `.get(word, 0)` treats the absence as a zero count rather than an error. Similarly, when reading configuration with optional settings, `.get("timeout", 30)` provides a sensible default.

You would want the `KeyError` when a missing key indicates a genuine bug. For example, if your code expects a dictionary with the keys "name", "email", and "role" (from a validated API response), a missing key means something went wrong upstream. Crashing immediately with a `KeyError` makes the bug visible right away. Silently substituting a default could mask the problem and cause incorrect behaviour elsewhere.

**Answer 3:**

`frequency.get(word, 0)` returns the current count for `word` if it exists, or `0` if the word has not been seen yet. Adding `1` gives the new count, which is then stored back with `frequency[word] = ...`. This pattern works for the very first occurrence (0 + 1 = 1) and every subsequent one.

If you wrote `frequency[word] += 1` directly, Python would first try to read `frequency[word]` to get the current value. For a word that has not been seen, this raises a `KeyError` because the key does not exist yet. The `+=` operator requires the key to already have a value.

Alternative approaches include: using `if word in frequency:` / `else:` to check before incrementing, using `frequency.setdefault(word, 0)` followed by `+= 1`, or using `collections.Counter` from the standard library, which handles counting automatically with `Counter(words)`.

**Answer 4:**

Mathematical set operations are defined for collections of distinct elements. Union means "all distinct elements from both sets." If a set contained duplicates, "union" would be ambiguous — should duplicates from both sets add up? Should they be merged? The mathematical definition becomes unclear.

With unique elements, the operations are clean and predictable. `{1, 2, 3} | {2, 3, 4}` gives `{1, 2, 3, 4}` — every element appears exactly once. Intersection (`{2, 3}`) means elements present in both, not "elements present at least twice in either." Difference (`{1}`) means elements in one but not the other.

If duplicates were allowed, you would need multiset operations (which Python supports via `collections.Counter`), where union takes the maximum count and intersection takes the minimum count. This is useful in some contexts but more complex than what most programmers need for everyday membership and comparison tasks.

**Answer 5:**

With a list, the `in` operator performs a linear search — it checks each element one by one until it finds a match or reaches the end. For 100,000 usernames, this means up to 100,000 string comparisons per lookup. If you are checking many usernames (e.g., during registration validation), this becomes very slow.

With a set, the `in` operator uses a hash table internally. It computes a hash of the username and jumps directly to where it should be stored, checking one or a few elements. This takes roughly the same time regardless of whether the set contains 100 or 100,000 items. For username existence checks, a set is the clear choice.

The trade-off is that sets are unordered and do not store extra data (just the username, not associated account information). If you also need to look up user data, a dictionary (username → user data) provides both fast lookup and associated information.

**Answer 6:**

Dictionary keys are stored in a hash table. The hash of a key determines where it is placed in the table. When you look up `d["alice"]`, Python hashes the string "alice" to find its location instantly. This only works if the hash of a key never changes after it is stored.

If a list were allowed as a key, its hash would be based on its contents. If you then modified the list (e.g., appended an element), its hash would change — but the dictionary would still have it stored at the old hash location. The key would become "lost": looking it up with the modified list would search the wrong location, and the original entry would be unreachable. This would silently corrupt the dictionary.

Immutable objects (strings, numbers, tuples) guarantee that the hash never changes, so the dictionary's internal structure remains consistent. This is why Python requires dictionary keys (and set elements) to be hashable, which in practice means immutable.

**Answer 7:**

Using `for key in my_dict:` iterates over keys only. This is appropriate when you only need the keys (e.g., checking if certain keys exist) or when you access values selectively inside the loop with `my_dict[key]`.

Using `for key, value in my_dict.items()` iterates over key-value pairs. This is the right choice when you need both the key and the value for every entry — the common case for processing dictionary data.

There is no significant performance difference between the two approaches. The `.items()` method returns a view object that does not create a copy of the data. Both iterate over the same underlying hash table. The choice is about clarity and convenience: if you need the value, use `.items()` rather than looking up each key separately inside the loop.

---

## 15. Code solutions

### Exercise 2.2.2: contacts.py

```python
# contacts.py - Simple contact book using dictionaries

contacts = {
    "Alice": "+36-20-111-2222",
    "Bob": "+36-30-333-4444",
    "Charlie": "+36-70-555-6666",
}


def show_contacts(book):
    """Display all contacts in a formatted list."""
    if not book:
        print("  (no contacts)")
        return
    for name, phone in sorted(book.items()):
        print(f"  {name:<12} {phone}")
    print(f"\n  Total: {len(book)} contact(s)")


def lookup(book, name):
    """Look up a contact by name using .get() for safe access."""
    phone = book.get(name)
    if phone:
        print(f"  {name}: {phone}")
    else:
        print(f"  '{name}' not found in contacts.")


# Display all contacts
print("=== Contact book ===\n")
show_contacts(contacts)

# Look up contacts
print("\n--- Lookups ---")
lookup(contacts, "Alice")
lookup(contacts, "Diana")

# Add a new contact
print("\n--- Adding Diana ---")
contacts["Diana"] = "+36-20-777-8888"
show_contacts(contacts)

# Update an existing contact
print("\n--- Updating Bob's number ---")
contacts["Bob"] = "+36-30-999-0000"
lookup(contacts, "Bob")

# Remove a contact
print("\n--- Removing Charlie ---")
del contacts["Charlie"]
show_contacts(contacts)

# Safe removal with pop (no error if missing)
print("\n--- Safe removal of 'Eve' (not in contacts) ---")
removed = contacts.pop("Eve", None)
if removed:
    print(f"  Removed Eve: {removed}")
else:
    print("  'Eve' was not in contacts — nothing removed.")
```

### Exercise 2.2.3: word_count.py

```python
# word_count.py - Count word frequencies in a text

text = """Python is a powerful programming language.
Python is used for web development, data science, and automation.
Learning Python is a great investment for any developer.
Python makes complex tasks simple and simple tasks trivial."""

# Clean and split the text into words
words = text.lower().replace(".", "").replace(",", "").split()

# Count frequencies using a dictionary
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display all words sorted by frequency (highest first)
print("=== Word frequency analysis ===\n")

sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words:
    bar = "#" * count
    print(f"  {word:<15} {count:>2}  {bar}")

print(f"\n  Unique words: {len(frequency)}")
print(f"  Total words:  {len(words)}")
```

### Exercise 2.2.4: team_skills.py

```python
# team_skills.py - Compare team skills using sets

team_a_skills = ["Python", "SQL", "Excel", "Git", "Docker", "Python", "SQL"]
team_b_skills = ["JavaScript", "SQL", "React", "Git", "CSS", "SQL", "Git"]

# Convert to sets (duplicates are removed automatically)
skills_a = set(team_a_skills)
skills_b = set(team_b_skills)

print("=== Team skill analysis ===\n")

print(f"Team A skills: {sorted(skills_a)}")
print(f"Team B skills: {sorted(skills_b)}")

# Common skills (intersection)
common = skills_a & skills_b
print(f"\nShared skills:      {sorted(common)}")

# All skills combined (union)
all_skills = skills_a | skills_b
print(f"All skills combined: {sorted(all_skills)}")

# Only in Team A (difference)
only_a = skills_a - skills_b
print(f"Only in Team A:     {sorted(only_a)}")

# Only in Team B (difference)
only_b = skills_b - skills_a
print(f"Only in Team B:     {sorted(only_b)}")

# Skills in one team but not both (symmetric difference)
exclusive = skills_a ^ skills_b
print(f"Exclusive to one:   {sorted(exclusive)}")

# Summary
print(f"\n=== Summary ===")
print(f"  Team A: {len(skills_a)} unique skill(s)")
print(f"  Team B: {len(skills_b)} unique skill(s)")
print(f"  Shared: {len(common)}")
print(f"  Total unique across both: {len(all_skills)}")
```
