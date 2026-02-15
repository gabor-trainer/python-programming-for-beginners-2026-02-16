# Lab 4.2: Creating your first classes

**Estimated time**: 60 minutes  
**Difficulty level**: Intermediate  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Define a class with `__init__` and create instances from it
- Add methods that operate on instance attributes
- Implement `__str__` to control how objects are displayed
- Build a class that manages a collection of other objects
- Combine classes with list comprehensions for data queries

---

## 3. Prerequisites

**Knowledge prerequisites**: Functions, lists, dictionaries, list comprehensions (Days 1–3 material and Lab 4.1). Chapter 4.2 presentation completed.

**Previous labs**: Labs 3.1 through 4.1 completed.

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

So far, you have stored structured data in dictionaries — a contact as `{"name": "Alice", "email": "alice@example.com"}`, an expense as `{"date": "2024-11-15", "amount": 285.50}`. This works, but every function that processes a contact needs to know the exact key names, and nothing prevents typos like `"emial"` from silently creating a wrong entry.

A **class** bundles data and the functions that operate on it into a single unit. Instead of a dictionary with arbitrary keys, you get an object with defined attributes. Instead of separate functions scattered across your code, you get methods that live with the data they belong to. When you print the object, `__str__` controls what the user sees.

In this lab, you will build a `Contact` class step by step, add validation and formatting methods, then create a `ContactBook` class that manages a collection of contacts. This mirrors the kind of data management you will use in the capstone project.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Define a class with attributes and observe how objects store independent data
- Add methods for formatting, validation, and search
- Implement `__str__` for readable output
- Build a collection class that uses list comprehensions internally

---

### Exercise 4.2.1: Explore classes in the REPL

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Define a simple class, create instances, access attributes, and understand `self`.

**Scenario**: Before building a complete class, you want to experiment with the basic mechanics — defining a class, creating objects, and accessing their attributes.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

2. Define a minimal class and create instances:

```python
>>> class Contact:
...     def __init__(self, name, email):
...         self.name = name
...         self.email = email
...
>>> alice = Contact("Alice Novak", "alice@example.com")
>>> bob = Contact("Bob Dvorak", "bob@example.com")
```

3. Access attributes with dot notation:

```python
>>> print(alice.name)
Alice Novak
>>> print(bob.email)
bob@example.com
```

4. Verify that each object has its own data:

```python
>>> alice.email = "alice.novak@company.com"
>>> print(alice.email)
alice.novak@company.com
>>> print(bob.email)
bob@example.com
```

5. See what printing an object looks like without `__str__`:

```python
>>> print(alice)
<__main__.Contact object at 0x...>
```

6. Check the type:

```python
>>> print(type(alice))
<class '__main__.Contact'>
>>> print(isinstance(alice, Contact))
True
```

7. See what happens when you forget a required argument:

```python
>>> bad = Contact("Charlie")
Traceback (most recent call last):
  ...
TypeError: Contact.__init__() missing 1 required positional argument: 'email'
```

8. Exit the REPL:

```python
>>> exit()
```

**Verification**: You created a class with `__init__`, made instances, accessed attributes independently, observed the default unhelpful `print()` output, and saw the error when arguments are missing.

---

### Exercise 4.2.2: Build a Contact class with methods

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Add methods for formatting, validation, and display to a class, and implement `__str__`.

**Scenario**: You are building a contact management system. Each contact needs a readable display format, email validation, and a search capability.

**Tasks**:

1. In VS Code, create a new file (`Ctrl+N`). Save it as `contact.py` in `C:\labs` (`Ctrl+S`).

2. Type the following code:

```python
# contact.py - Contact class with methods


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def format_label(self):
        """Return a formatted label like 'Alice Novak <alice@example.com>'."""
        return f"{self.name} <{self.email}>"

    def has_valid_email(self):
        """Check if the email contains @ and a dot after it."""
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain

    def matches_search(self, query):
        """Check if query appears in name or email (case-insensitive)."""
        query_lower = query.lower()
        return (
            query_lower in self.name.lower()
            or query_lower in self.email.lower()
        )


# --- Test the Contact class ---

print("=== Creating contacts ===")
contacts = [
    Contact("Alice Novak", "alice@example.com", "+420 111 222 333"),
    Contact("Bob Dvorak", "bob@example.com", "+420 444 555 666"),
    Contact("Charlie Svoboda", "charlie.at" , "+420 777 888 999"),
    Contact("Diana Horak", "diana@mail.server.org", "+420 000 111 222"),
]

for c in contacts:
    print(f"  {c}")
print()

print("=== Format labels ===")
for c in contacts:
    print(f"  {c.format_label()}")
print()

print("=== Email validation ===")
for c in contacts:
    valid = "valid" if c.has_valid_email() else "INVALID"
    print(f"  {c.name}: {c.email} -> {valid}")
print()

print("=== Search for 'alice' ===")
results = [c for c in contacts if c.matches_search("alice")]
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
print()

print("=== Search for 'example' ===")
results = [c for c in contacts if c.matches_search("example")]
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
```

3. Run the script:

```
C:\labs> python contact.py
```

**Expected output**: Four sections. The "Creating contacts" section prints each contact using `__str__`. Format labels show the `Name <email>` format. Email validation flags Charlie's entry as invalid (missing `@`). Search results for "alice" return one contact; search for "example" returns contacts whose email contains "example".

**Verification**: `__str__` is called automatically by `print()`. The `has_valid_email` method correctly identifies the malformed email. The `matches_search` method uses case-insensitive matching. The list comprehension `[c for c in contacts if c.matches_search(...)]` filters contacts cleanly.

**Try it yourself**:
- Add a method `get_domain()` that returns the domain part of the email (everything after `@`), or `"N/A"` if the email is invalid.
- Add a method `matches_any(queries)` that takes a list of search terms and returns `True` if any of them match.

---

### Exercise 4.2.3: Build a ContactBook class

**Time**: 20 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Create a class that manages a collection of `Contact` objects, using methods and list comprehensions.

**Scenario**: Individual contacts are useful, but you need a container to add, search, list, and summarise them. A `ContactBook` class wraps a list of contacts and provides a clean interface.

**Tasks**:

1. In VS Code, create a new file. Save it as `contact_book.py` in `C:\labs`.

2. Type the following code:

```python
# contact_book.py - ContactBook class managing a collection of contacts


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def has_valid_email(self):
        """Check if the email contains @ and a dot after it."""
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain

    def matches_search(self, query):
        """Check if query appears in name or email (case-insensitive)."""
        query_lower = query.lower()
        return (
            query_lower in self.name.lower()
            or query_lower in self.email.lower()
        )


class ContactBook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        return f"ContactBook({len(self.contacts)} contacts)"

    def add(self, name, email, phone):
        """Create a Contact and add it to the book."""
        contact = Contact(name, email, phone)
        self.contacts.append(contact)
        print(f"  Added: {contact.name}")

    def show_all(self):
        """Print all contacts."""
        if not self.contacts:
            print("  Contact book is empty.")
            return
        for contact in self.contacts:
            print(f"  {contact}")

    def search(self, query):
        """Return contacts matching the query."""
        return [c for c in self.contacts if c.matches_search(query)]

    def get_invalid_emails(self):
        """Return contacts with invalid email addresses."""
        return [c for c in self.contacts if not c.has_valid_email()]

    def get_domains(self):
        """Return a sorted list of unique email domains."""
        domains = set()
        for c in self.contacts:
            if "@" in c.email:
                domains.add(c.email.split("@")[1])
        return sorted(domains)

    def count(self):
        """Return the number of contacts."""
        return len(self.contacts)


# --- Test the ContactBook ---

book = ContactBook()
print("=== Adding contacts ===")
book.add("Alice Novak", "alice@example.com", "+420 111 222 333")
book.add("Bob Dvorak", "bob@company.cz", "+420 444 555 666")
book.add("Charlie Svoboda", "charlie-bad-email", "+420 777 888 999")
book.add("Diana Horak", "diana@example.com", "+420 000 111 222")
book.add("Eva Marek", "eva@company.cz", "+420 333 444 555")
print()

print(f"=== {book} ===")
book.show_all()
print()

print("=== Search: 'company' ===")
results = book.search("company")
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
print()

print("=== Invalid emails ===")
invalid = book.get_invalid_emails()
if invalid:
    for c in invalid:
        print(f"  {c.name}: {c.email}")
else:
    print("  All emails are valid.")
print()

print("=== Email domains ===")
domains = book.get_domains()
print(f"  {domains}")
```

3. Run the script:

```
C:\labs> python contact_book.py
```

**Expected output**: Contacts are added with confirmation messages. The full list displays all five contacts. Searching for "company" returns contacts with "company" in their email. The invalid emails section identifies Charlie. The domains list shows unique domains sorted alphabetically.

**Verification**: The `ContactBook` internally uses a list but exposes a clean interface. Methods like `search()` and `get_invalid_emails()` use list comprehensions. The `__str__` method on `ContactBook` shows the count. All operations work through the class methods, not by accessing `book.contacts` directly.

**Try it yourself**:
- Add a `remove(name)` method that removes the first contact matching the given name (case-insensitive). Print a confirmation or a "not found" message.
- Add a `summary()` method that prints the total count, number of valid/invalid emails, and the list of unique domains.

---

### Exercise 4.2.4: Classes versus dictionaries

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: VS Code  
**Objective**: Compare the dictionary approach to the class approach and observe the practical differences.

**Scenario**: A colleague argues that dictionaries are simpler and classes are unnecessary overhead. You want to demonstrate the trade-offs with a concrete example.

**Tasks**:

1. In VS Code, create a new file. Save it as `class_vs_dict.py` in `C:\labs`.

2. Type the following code:

```python
# class_vs_dict.py - Compare classes and dictionaries


# --- Dictionary approach ---
print("=== Dictionary approach ===\n")

contact_dict = {
    "name": "Alice Novak",
    "email": "alice@example.com",
    "phone": "+420 111 222 333",
}

# Typo in key name — silently creates a new entry
contact_dict["emial"] = "alice.novak@company.com"
print(f"Keys: {list(contact_dict.keys())}")
print(f"  Notice 'emial' alongside 'email' — silent bug")
print()

# No built-in validation
bad_dict = {"name": "", "email": "not-an-email", "phone": "abc"}
print(f"Bad contact (dict): {bad_dict}")
print(f"  No error — dictionary accepts anything")
print()


# --- Class approach ---
print("=== Class approach ===\n")


class Contact:
    def __init__(self, name, email, phone):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def has_valid_email(self):
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain


alice = Contact("Alice Novak", "alice@example.com", "+420 111 222 333")
print(f"Contact: {alice}")
print(f"  Valid email: {alice.has_valid_email()}")
print()

# Trying to create a contact with empty name
try:
    bad_contact = Contact("", "test@example.com", "123")
except ValueError as e:
    print(f"Validation caught: {e}")
print()


# --- Comparison: working with collections ---
print("=== Collection comparison ===\n")

# Dictionary approach: external function needed
def format_dict_contact(d):
    return f"{d['name']} <{d['email']}>"

dict_contacts = [
    {"name": "Alice", "email": "alice@ex.com", "phone": "111"},
    {"name": "Bob", "email": "bob@ex.com", "phone": "222"},
]
print("Dict labels:")
for d in dict_contacts:
    print(f"  {format_dict_contact(d)}")
print()

# Class approach: method is part of the object
class ContactWithLabel:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def format_label(self):
        return f"{self.name} <{self.email}>"

obj_contacts = [
    ContactWithLabel("Alice", "alice@ex.com", "111"),
    ContactWithLabel("Bob", "bob@ex.com", "222"),
]
print("Class labels:")
for c in obj_contacts:
    print(f"  {c.format_label()}")
print()

print("Key difference: with classes, data and behaviour live together.")
print("With dictionaries, functions are separate from the data they operate on.")
```

3. Run the script:

```
C:\labs> python class_vs_dict.py
```

**Expected output**: The dictionary section shows that a typo creates a new key silently and that no validation occurs. The class section catches the empty name with a `ValueError`. The collection comparison shows that dictionary-based code needs external functions, while class-based code keeps methods with the data.

**Verification**: The dictionary accepts `"emial"` without error. The class raises `ValueError` for invalid data. Both approaches work, but the class provides structure, validation, and co-located behaviour.

---

## 7. Validation checklist

- [ ] Exercise 4.2.1: You explored class creation and attribute access in the REPL
- [ ] Exercise 4.2.2: `contact.py` creates contacts, validates emails, and searches by query
- [ ] Exercise 4.2.3: `contact_book.py` manages a collection with add, search, and validation methods
- [ ] Exercise 4.2.4: `class_vs_dict.py` demonstrates trade-offs between dictionaries and classes

```
C:\labs> python contact.py
# Four sections: creation, labels, validation, search results

C:\labs> python contact_book.py
# Adding contacts, full list, search results, invalid emails, domains

C:\labs> python class_vs_dict.py
# Dictionary pitfalls, class validation, collection comparison
```

---

## 8. Troubleshooting guide

**Common Python errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| `TypeError: __init__() missing required positional argument` | Forgot an argument when creating an object | Check how many parameters `__init__` expects (excluding `self`) |
| `NameError: name 'self' is not defined` | Missing `self` as first parameter of a method | Add `self` as the first parameter of every method |
| `AttributeError: 'Contact' object has no attribute 'X'` | Accessing an attribute that was not set in `__init__` | Check spelling, ensure `self.X = ...` is in `__init__` |
| `TypeError: Contact() takes no arguments` | Missing `__init__` method | Add `def __init__(self, ...):` to the class |
| `SyntaxError` near `class` | Missing colon after `class Name` or after `def` | Ensure both `class Name:` and `def method(self):` end with `:` |

**Common beginner pitfalls:**
- Forgetting `self` as the first parameter of every method
- Using `name` instead of `self.name` inside a method — refers to a local variable, not the attribute
- Calling a method on the class instead of an instance: `Contact.format_label()` vs `alice.format_label()`
- Printing an object without defining `__str__` and seeing `<__main__.Contact object at 0x...>`

**Environment issues:**
- `python` not recognised → Check PATH, try `py` on Windows
- File not found → Verify you are in `C:\labs` with `cd C:\labs`

---

## 9. Questions

1. You store employee records as dictionaries: `{"name": "Alice", "dept": "Engineering", "salary": 75000}`. A colleague accidentally writes `emp["salry"] = 80000` (typo). Explain how using a class would prevent or reveal this bug earlier, and discuss whether the extra code is worth it.

2. A function `format_contact(contact_dict)` takes a dictionary and returns a formatted string. Contrast this with a method `contact.format_label()` on a `Contact` object. Why does the method approach scale better as the number of operations on contacts grows?

3. You have 500 `Contact` objects in a list and need to find all contacts at a specific email domain. Write the comprehension that does this. Now explain why having `matches_search` as a method on `Contact` (rather than a standalone function) makes the comprehension more readable.

4. The `__str__` method returns a string but does not print it. Explain why this design decision matters. What would you lose if `__str__` called `print()` directly instead of returning a string?

5. Consider a `BankAccount` class with a `balance` attribute and `deposit(amount)` / `withdraw(amount)` methods. Why is it important that the balance is modified only through these methods, rather than allowing `account.balance = account.balance - 100` directly?

6. Your `ContactBook.add()` method creates the `Contact` object internally. An alternative design accepts a `Contact` object as a parameter: `book.add(contact)`. Compare the two approaches. When would you prefer each?

7. Explain the relationship between a class and its instances using an analogy from a real-world scenario you encounter daily. Make sure your analogy covers attributes (data that varies per instance) and methods (behaviour shared by all instances).

---

## 10. Clean-up

Remove the files created during this lab:

```
C:\labs> del contact.py
C:\labs> del contact_book.py
C:\labs> del class_vs_dict.py
```

Verify your working directory is clean:

```
C:\labs> dir *.py
```

**Note**: Do NOT uninstall Python or VS Code.

---

## 11. Key takeaways

- A class defines a new type with `class Name:` — instances are created by calling `Name(args)`
- `__init__(self, ...)` initialises the object's attributes when it is created
- `self` refers to the current instance — use `self.attribute` to access data inside methods
- Methods are functions defined inside a class that operate on the instance's data
- `__str__(self)` controls what `print()` displays — without it, you get an unreadable memory address
- Classes bundle data and behaviour together — methods live with the data they operate on
- For structured data with operations (contacts, products, expenses), classes are clearer and safer than dictionaries

---

## 12. Additional resources

- Python Tutorial — Classes: https://docs.python.org/3/tutorial/classes.html
- Python Tutorial — A First Look at Classes: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
- PEP 8 — Class Names: https://peps.python.org/pep-0008/#class-names
- Real Python — Object-Oriented Programming in Python: https://realpython.com/python3-object-oriented-programming/

---

## 13. Appendices

### Appendix A: Quick reference — class syntax

```python
class ClassName:
    def __init__(self, param1, param2):
        self.attr1 = param1
        self.attr2 = param2

    def __str__(self):
        return f"ClassName({self.attr1}, {self.attr2})"

    def some_method(self):
        return self.attr1 + self.attr2

    def method_with_args(self, other):
        return self.attr1 == other


# Create an instance
obj = ClassName("value1", "value2")

# Access attributes
print(obj.attr1)

# Call methods
print(obj.some_method())
print(obj)  # calls __str__
```

### Appendix B: Built-in functions that work with objects

| Function | Purpose |
|----------|---------|
| `type(obj)` | Return the type (class) of an object |
| `isinstance(obj, cls)` | Check if an object is an instance of a class |
| `str(obj)` | Call `__str__` and return the string |
| `print(obj)` | Call `__str__` and print the result |
| `hasattr(obj, "name")` | Check if an object has a given attribute |
| `getattr(obj, "name")` | Get an attribute value by name |

### Appendix C: Environment information

- Python: `python --version`
- Run scripts: `python script.py`
- VS Code: `Ctrl+N` (new file), `Ctrl+S` (save), `` Ctrl+` `` (terminal)

---

## 14. Answers

**Answer 1:**

With a dictionary, `emp["salry"] = 80000` silently creates a new key called `"salry"` alongside the existing `"salary"`. The original salary is unchanged, and the typo goes undetected until something downstream reads `"salary"` and gets the old value. Finding this bug requires inspecting every place that writes to the dictionary.

With a class, you would define attributes in `__init__`: `self.salary = salary`. If code later tries to set `self.salry = 80000`, Python creates a new attribute on that specific instance — which is still a bug, but it is easier to catch with code review or tools like linters. More importantly, if you access `self.salry` somewhere else, you get an `AttributeError` immediately instead of silent incorrect data. For structured records like employee data, the upfront cost of defining a class pays off in fewer silent bugs.

**Answer 2:**

With the dictionary approach, every operation on a contact is a standalone function: `format_contact(d)`, `validate_email(d)`, `search_contact(d, query)`. As operations multiply, these functions scatter across the codebase with no obvious grouping. A new developer looking at the code has to search for all functions that accept a contact dictionary.

With a class, all operations are methods: `contact.format_label()`, `contact.has_valid_email()`, `contact.matches_search(query)`. They are defined together in one place, discoverable through the class definition, and IDE autocomplete shows them when you type `contact.`. As the system grows from 3 to 20 operations, the class keeps them organised. The dictionary approach becomes increasingly hard to manage because nothing ties the functions to the data they operate on.

**Answer 3:**

The comprehension: `matches = [c for c in contacts if c.email.split("@")[1] == "example.com"]` — or, if using the method: `matches = [c for c in contacts if c.matches_search("@example.com")]`.

Having `matches_search` as a method makes the comprehension self-documenting: "get contacts where the contact matches this search." The logic of how matching works (case-insensitive, checks name and email) is encapsulated inside the method. If the matching logic changes later — for example, adding phone number search — you update the method once, and every comprehension that uses it automatically gets the improvement.

With a standalone function, the comprehension reads `[c for c in contacts if matches_search(c, query)]` — slightly less natural, and the connection between the function and the data it operates on is not explicit.

**Answer 4:**

`__str__` returns a string so the caller can decide what to do with it. You might want to print it, write it to a file, include it in a larger string, send it over a network, or store it in a list. Returning a string keeps all options open.

If `__str__` called `print()` directly, you would lose that flexibility. `print(contact)` would print twice (once inside `__str__`, once from the outer `print`). Writing contacts to a file with `f.write(str(contact))` would print to the screen as a side effect. Building a comma-separated string of all contacts would be impossible without refactoring. The return-a-value pattern keeps functions composable — each function does one thing, and the caller combines them as needed.

**Answer 5:**

Direct access like `account.balance -= 100` has no safeguards. You could set the balance to a negative number, subtract a string, or assign `None` — all silently. There is no audit trail, no validation, no error handling.

Methods like `withdraw(amount)` can validate the input (is the amount positive?), check business rules (is the balance sufficient?), log the transaction, and raise meaningful errors (`InsufficientFundsError`). They create a controlled interface: the only way to change the balance is through methods that enforce the rules. This is a core benefit of OOP — the class protects its data by controlling how it is accessed and modified. Even if you do not need validation today, adding it to a method is a one-line change; adding it to every place that directly modifies `balance` requires finding and updating every occurrence.

**Answer 6:**

The internal creation approach `book.add("Alice", "alice@example.com", "123")` is simpler for the caller — they pass raw data and the `ContactBook` handles object creation. This is convenient when the book is the only place contacts are created. It also lets the book enforce consistency: it controls which class is used and can add validation.

The parameter approach `book.add(contact)` is more flexible. The contact can be created elsewhere, configured, validated, or created from a factory function. It also decouples `ContactBook` from `Contact` creation — the book only needs to know how to store contacts, not how to create them. This is better when contacts come from different sources (user input, file parsing, API responses) and are constructed differently. In practice, many systems offer both: an `add(contact)` method for flexibility, and a convenience method like `add_new(name, email, phone)` for the common case.

**Answer 7:**

A good analogy: a class is like a blueprint for an apartment in a building. The blueprint (class) defines the layout: every apartment has a kitchen, a bathroom, and a living room (attributes). It also defines what you can do: open a door, turn on the lights, adjust the thermostat (methods).

Each actual apartment (instance) built from the blueprint has the same layout, but the contents differ: apartment 3A has blue curtains, apartment 5B has green curtains. The curtain colour is instance data — it varies per apartment. The door-opening mechanism is shared behaviour — it works the same way in every apartment. You do not need a separate blueprint for each apartment; you create many instances from one class, each with its own specific data.

---

## 15. Code solutions

### Exercise 4.2.2: contact.py

```python
# contact.py - Contact class with methods


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def format_label(self):
        """Return a formatted label like 'Alice Novak <alice@example.com>'."""
        return f"{self.name} <{self.email}>"

    def has_valid_email(self):
        """Check if the email contains @ and a dot after it."""
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain

    def matches_search(self, query):
        """Check if query appears in name or email (case-insensitive)."""
        query_lower = query.lower()
        return (
            query_lower in self.name.lower()
            or query_lower in self.email.lower()
        )


print("=== Creating contacts ===")
contacts = [
    Contact("Alice Novak", "alice@example.com", "+420 111 222 333"),
    Contact("Bob Dvorak", "bob@example.com", "+420 444 555 666"),
    Contact("Charlie Svoboda", "charlie.at", "+420 777 888 999"),
    Contact("Diana Horak", "diana@mail.server.org", "+420 000 111 222"),
]

for c in contacts:
    print(f"  {c}")
print()

print("=== Format labels ===")
for c in contacts:
    print(f"  {c.format_label()}")
print()

print("=== Email validation ===")
for c in contacts:
    valid = "valid" if c.has_valid_email() else "INVALID"
    print(f"  {c.name}: {c.email} -> {valid}")
print()

print("=== Search for 'alice' ===")
results = [c for c in contacts if c.matches_search("alice")]
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
print()

print("=== Search for 'example' ===")
results = [c for c in contacts if c.matches_search("example")]
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
```

### Exercise 4.2.3: contact_book.py

```python
# contact_book.py - ContactBook class managing a collection of contacts


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def has_valid_email(self):
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain

    def matches_search(self, query):
        query_lower = query.lower()
        return (
            query_lower in self.name.lower()
            or query_lower in self.email.lower()
        )


class ContactBook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        return f"ContactBook({len(self.contacts)} contacts)"

    def add(self, name, email, phone):
        contact = Contact(name, email, phone)
        self.contacts.append(contact)
        print(f"  Added: {contact.name}")

    def show_all(self):
        if not self.contacts:
            print("  Contact book is empty.")
            return
        for contact in self.contacts:
            print(f"  {contact}")

    def search(self, query):
        return [c for c in self.contacts if c.matches_search(query)]

    def get_invalid_emails(self):
        return [c for c in self.contacts if not c.has_valid_email()]

    def get_domains(self):
        domains = set()
        for c in self.contacts:
            if "@" in c.email:
                domains.add(c.email.split("@")[1])
        return sorted(domains)

    def count(self):
        return len(self.contacts)


book = ContactBook()
print("=== Adding contacts ===")
book.add("Alice Novak", "alice@example.com", "+420 111 222 333")
book.add("Bob Dvorak", "bob@company.cz", "+420 444 555 666")
book.add("Charlie Svoboda", "charlie-bad-email", "+420 777 888 999")
book.add("Diana Horak", "diana@example.com", "+420 000 111 222")
book.add("Eva Marek", "eva@company.cz", "+420 333 444 555")
print()

print(f"=== {book} ===")
book.show_all()
print()

print("=== Search: 'company' ===")
results = book.search("company")
print(f"  Found {len(results)} result(s):")
for c in results:
    print(f"    {c}")
print()

print("=== Invalid emails ===")
invalid = book.get_invalid_emails()
if invalid:
    for c in invalid:
        print(f"  {c.name}: {c.email}")
else:
    print("  All emails are valid.")
print()

print("=== Email domains ===")
domains = book.get_domains()
print(f"  {domains}")
```

### Exercise 4.2.4: class_vs_dict.py

```python
# class_vs_dict.py - Compare classes and dictionaries

print("=== Dictionary approach ===\n")

contact_dict = {
    "name": "Alice Novak",
    "email": "alice@example.com",
    "phone": "+420 111 222 333",
}

contact_dict["emial"] = "alice.novak@company.com"
print(f"Keys: {list(contact_dict.keys())}")
print(f"  Notice 'emial' alongside 'email' — silent bug")
print()

bad_dict = {"name": "", "email": "not-an-email", "phone": "abc"}
print(f"Bad contact (dict): {bad_dict}")
print(f"  No error — dictionary accepts anything")
print()

print("=== Class approach ===\n")


class Contact:
    def __init__(self, name, email, phone):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

    def has_valid_email(self):
        if "@" not in self.email:
            return False
        local, domain = self.email.split("@", 1)
        return bool(local) and "." in domain


alice = Contact("Alice Novak", "alice@example.com", "+420 111 222 333")
print(f"Contact: {alice}")
print(f"  Valid email: {alice.has_valid_email()}")
print()

try:
    bad_contact = Contact("", "test@example.com", "123")
except ValueError as e:
    print(f"Validation caught: {e}")
print()

print("=== Collection comparison ===\n")


def format_dict_contact(d):
    return f"{d['name']} <{d['email']}>"


dict_contacts = [
    {"name": "Alice", "email": "alice@ex.com", "phone": "111"},
    {"name": "Bob", "email": "bob@ex.com", "phone": "222"},
]
print("Dict labels:")
for d in dict_contacts:
    print(f"  {format_dict_contact(d)}")
print()


class ContactWithLabel:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def format_label(self):
        return f"{self.name} <{self.email}>"


obj_contacts = [
    ContactWithLabel("Alice", "alice@ex.com", "111"),
    ContactWithLabel("Bob", "bob@ex.com", "222"),
]
print("Class labels:")
for c in obj_contacts:
    print(f"  {c.format_label()}")
print()

print("Key difference: with classes, data and behaviour live together.")
print("With dictionaries, functions are separate from the data they operate on.")
```
