# Regular Expressions Essentials

**Target Audience:** Day 3+ students working with text processing  
**Prerequisites:** Strings, functions, basic conditionals  
**Time to Learn:** 45-60 minutes  

---

## Introduction

Regular expressions (regex) are patterns for matching text. Use them for validation, searching, extracting, and replacing text.

**Common Use Cases:**
- Validate email addresses, phone numbers, passwords
- Extract data from logs, HTML, or unstructured text
- Find and replace patterns in files
- Parse structured text formats

**Python's `re` Module:** Built-in module for regex operations.

---

## Basic Pattern Matching

### Simple String Search

```python
import re

text = "The quick brown fox jumps over the lazy dog"

# Check if pattern exists
if re.search('fox', text):
    print("Found 'fox' in text")

# Find first match
match = re.search('brown', text)
if match:
    print(f"Found at position: {match.start()}")  # 10
```

### Exact Match

```python
import re

# Match entire string
if re.match('The', "The quick brown fox"):
    print("String starts with 'The'")

# Fullmatch - must match entire string
if re.fullmatch('cat', 'cat'):
    print("Exact match")

if not re.fullmatch('cat', 'category'):
    print("Not an exact match")
```

**Key Functions:**
- `re.search(pattern, text)` — Find pattern anywhere in text
- `re.match(pattern, text)` — Match at start of text only
- `re.fullmatch(pattern, text)` — Match entire text exactly

---

## Special Characters (Metacharacters)

### Dot (.) - Any Character

```python
import re

# . matches any character except newline
pattern = 'c.t'

print(re.search(pattern, 'cat'))  # Match
print(re.search(pattern, 'cot'))  # Match
print(re.search(pattern, 'cut'))  # Match
print(re.search(pattern, 'ct'))   # No match (need character between)
```

### Star (*) - Zero or More

```python
import re

# * matches 0 or more of preceding character
pattern = 'co*l'

print(re.search(pattern, 'cl'))     # Match (0 o's)
print(re.search(pattern, 'col'))    # Match (1 o)
print(re.search(pattern, 'cool'))   # Match (2 o's)
print(re.search(pattern, 'coool'))  # Match (3 o's)
```

### Plus (+) - One or More

```python
import re

# + matches 1 or more of preceding character
pattern = 'co+l'

print(re.search(pattern, 'cl'))    # No match (need at least 1 o)
print(re.search(pattern, 'col'))   # Match
print(re.search(pattern, 'cool'))  # Match
```

### Question Mark (?) - Zero or One

```python
import re

# ? makes preceding character optional
pattern = 'colou?r'

print(re.search(pattern, 'color'))   # Match (0 u's)
print(re.search(pattern, 'colour'))  # Match (1 u)
print(re.search(pattern, 'colouur'))  # No match (too many u's)
```

---

## Character Classes

### Bracket Notation

```python
import re

# [abc] matches any single character a, b, or c
pattern = '[aeiou]'

text = "hello world"
matches = re.findall(pattern, text)
print(matches)  # ['e', 'o', 'o']

# [0-9] matches any digit
pattern = '[0-9]'
matches = re.findall(pattern, "Room 123")
print(matches)  # ['1', '2', '3']

# [a-z] matches any lowercase letter
pattern = '[a-z]+'
matches = re.findall(pattern, "Hello World")
print(matches)  # ['ello', 'orld']

# [A-Z] matches any uppercase letter
pattern = '[A-Z]'
matches = re.findall(pattern, "Hello World")
print(matches)  # ['H', 'W']
```

### Negation with ^

```python
import re

# [^0-9] matches any character that is NOT a digit
pattern = '[^0-9]+'

matches = re.findall(pattern, "Room 123")
print(matches)  # ['Room ', '']

# [^aeiou] matches any consonant
pattern = '[^aeiou]+'
matches = re.findall(pattern, "hello world")
print(matches)  # ['h', 'll', ' w', 'rld']
```

### Predefined Character Classes

```python
import re

text = "Contact: john@example.com or call 555-1234"

# \d matches any digit (equivalent to [0-9])
digits = re.findall(r'\d', text)
print(digits)  # ['5', '5', '5', '1', '2', '3', '4']

# \d+ matches one or more digits
numbers = re.findall(r'\d+', text)
print(numbers)  # ['555', '1234']

# \w matches word characters (letters, digits, underscore)
words = re.findall(r'\w+', text)
print(words)  # ['Contact', 'john', 'example', 'com', 'or', 'call', '555', '1234']

# \s matches whitespace
spaces = re.findall(r'\s', text)
print(len(spaces))  # 5

# \D matches non-digits
non_digits = re.findall(r'\D+', text)
print(non_digits)  # ['Contact: john@example.com or call ', '-']
```

**Common Character Classes:**
- `\d` — Digit [0-9]
- `\D` — Non-digit
- `\w` — Word character [a-zA-Z0-9_]
- `\W` — Non-word character
- `\s` — Whitespace (space, tab, newline)
- `\S` — Non-whitespace

**Note:** Use raw strings (`r'pattern'`) to avoid escaping backslashes.

---

## Anchors

### Start and End of String

```python
import re

# ^ matches start of string
if re.search(r'^Hello', "Hello world"):
    print("Starts with Hello")

if not re.search(r'^Hello', "Say Hello"):
    print("Does not start with Hello")

# $ matches end of string
if re.search(r'world$', "Hello world"):
    print("Ends with world")

if not re.search(r'world$', "world peace"):
    print("Does not end with world")

# Combined: match entire string
if re.search(r'^Hello world$', "Hello world"):
    print("Exact match")
```

### Word Boundaries

```python
import re

text = "The cat in the cathedral"

# \b matches word boundary
cats = re.findall(r'\bcat\b', text)
print(cats)  # ['cat']

# Without boundary, matches partial words
cats_no_boundary = re.findall(r'cat', text)
print(cats_no_boundary)  # ['cat', 'cat'] (cat + cat from cathedral)
```

---

## Quantifiers

### Specific Counts

```python
import re

# {n} - exactly n times
pattern = r'\d{3}'
matches = re.findall(pattern, "123 45 67890")
print(matches)  # ['123', '678']

# {n,m} - between n and m times
pattern = r'\d{2,4}'
matches = re.findall(pattern, "1 12 123 1234 12345")
print(matches)  # ['12', '123', '1234', '1234']

# {n,} - n or more times
pattern = r'\d{3,}'
matches = re.findall(pattern, "12 123 1234")
print(matches)  # ['123', '1234']
```

### Greedy vs Non-Greedy

```python
import re

html = "<div>First</div><div>Second</div>"

# Greedy (default) - matches as much as possible
greedy = re.findall(r'<div>.*</div>', html)
print(greedy)  # ['<div>First</div><div>Second</div>']

# Non-greedy - matches as little as possible
non_greedy = re.findall(r'<div>.*?</div>', html)
print(non_greedy)  # ['<div>First</div>', '<div>Second</div>']
```

**Quantifiers:**
- `*` — 0 or more (greedy)
- `*?` — 0 or more (non-greedy)
- `+` — 1 or more (greedy)
- `+?` — 1 or more (non-greedy)
- `?` — 0 or 1 (greedy)
- `??` — 0 or 1 (non-greedy)

---

## Groups and Capturing

### Parentheses for Grouping

```python
import re

# Capture groups with ()
text = "Email: john@example.com"

match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(f"Username: {match.group(1)}")  # john
    print(f"Domain: {match.group(2)}")    # example.com
    print(f"Full match: {match.group(0)}")  # john@example.com
```

### Multiple Captures

```python
import re

text = "John Doe, age 30, lives in New York"

pattern = r'(\w+) (\w+), age (\d+), lives in (.+)'
match = re.search(pattern, text)

if match:
    first_name = match.group(1)
    last_name = match.group(2)
    age = match.group(3)
    city = match.group(4)
    
    print(f"Name: {first_name} {last_name}")
    print(f"Age: {age}")
    print(f"City: {city}")
```

### Named Groups

```python
import re

text = "Date: 2026-02-12"

pattern = r'Date: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, text)

if match:
    print(f"Year: {match.group('year')}")    # 2026
    print(f"Month: {match.group('month')}")  # 02
    print(f"Day: {match.group('day')}")      # 12
```

### Non-Capturing Groups

```python
import re

# (?:...) groups without capturing
text = "apple pie, banana pie"

# Capture the fruit but not 'pie'
matches = re.findall(r'(\w+)(?: pie)', text)
print(matches)  # ['apple', 'banana']
```

---

## Common Validation Patterns

### Email Address

```python
import re

def validate_email(email):
    """Basic email validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Test
print(validate_email("user@example.com"))     # True
print(validate_email("user.name@example.com"))  # True
print(validate_email("user@domain.co.uk"))    # True
print(validate_email("invalid.email"))        # False
print(validate_email("@example.com"))         # False
```

### Phone Number

```python
import re

def validate_phone(phone):
    """Validate US phone number (various formats)."""
    # Matches: 555-1234, (555) 123-4567, 555.123.4567, etc.
    pattern = r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return bool(re.match(pattern, phone))


# Test
print(validate_phone("555-1234"))        # True
print(validate_phone("(555) 123-4567"))  # True
print(validate_phone("555.123.4567"))    # True
print(validate_phone("5551234567"))      # True
print(validate_phone("123"))             # False
```

### Password Strength

```python
import re

def validate_password(password):
    """
    Validate password:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    """
    if len(password) < 8:
        return False, "Must be at least 8 characters"
    
    if not re.search(r'[A-Z]', password):
        return False, "Must contain uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Must contain lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Must contain digit"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Must contain special character"
    
    return True, "Password is valid"


# Test
print(validate_password("weak"))              # False
print(validate_password("Str0ng!Pass"))       # True
print(validate_password("NoSpecialChar123"))  # False
```

### URL

```python
import re

def validate_url(url):
    """Basic URL validation."""
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))


# Test
print(validate_url("https://example.com"))           # True
print(validate_url("http://example.com/path"))       # True
print(validate_url("https://sub.example.com"))       # True
print(validate_url("ftp://example.com"))             # False
print(validate_url("not-a-url"))                     # False
```

---

## Finding and Extracting Data

### findall - Get All Matches

```python
import re

text = "Prices: $10.99, $25.50, $100.00"

# Extract all prices
prices = re.findall(r'\$\d+\.\d{2}', text)
print(prices)  # ['$10.99', '$25.50', '$100.00']

# Extract just the numbers
numbers = re.findall(r'\$(\d+\.\d{2})', text)
print(numbers)  # ['10.99', '25.50', '100.00']
```

### finditer - Get Match Objects

```python
import re

text = "Contact: alice@example.com or bob@test.org"

pattern = r'(\w+)@([\w.]+)'

for match in re.finditer(pattern, text):
    username = match.group(1)
    domain = match.group(2)
    position = match.start()
    print(f"Found {username}@{domain} at position {position}")

# Output:
# Found alice@example.com at position 9
# Found bob@test.org at position 31
```

### Extracting from Structured Text

```python
import re

log_entry = "2026-02-12 14:30:45 ERROR UserService: Failed to login user_id=1234"

# Extract timestamp
timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_entry)
print(f"Timestamp: {timestamp.group()}")

# Extract log level
level = re.search(r'\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b', log_entry)
print(f"Level: {level.group()}")

# Extract user ID
user_id = re.search(r'user_id=(\d+)', log_entry)
print(f"User ID: {user_id.group(1)}")
```

---

## Replacing Text

### Basic Replacement

```python
import re

text = "The quick brown fox jumps over the lazy dog"

# Replace first occurrence
result = re.sub(r'fox', 'cat', text)
print(result)  # The quick brown cat jumps over the lazy dog

# Replace all occurrences
text = "foo bar foo baz foo"
result = re.sub(r'foo', 'qux', text)
print(result)  # qux bar qux baz qux

# Limit replacements
result = re.sub(r'foo', 'qux', text, count=2)
print(result)  # qux bar qux baz foo
```

### Using Captured Groups in Replacement

```python
import re

# Swap first and last name
text = "John Doe"
result = re.sub(r'(\w+) (\w+)', r'\2, \1', text)
print(result)  # Doe, John

# Format phone numbers
text = "Call 5551234567 or 5559876543"
result = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', text)
print(result)  # Call (555) 123-4567 or (555) 987-6543
```

### Using Functions for Replacement

```python
import re

def uppercase_match(match):
    """Convert matched text to uppercase."""
    return match.group(0).upper()


text = "hello world"
result = re.sub(r'\w+', uppercase_match, text)
print(result)  # HELLO WORLD


def mask_credit_card(match):
    """Mask all but last 4 digits."""
    number = match.group(0)
    return '*' * (len(number) - 4) + number[-4:]


text = "Card: 1234567812345678"
result = re.sub(r'\d{16}', mask_credit_card, text)
print(result)  # Card: ************5678
```

---

## Splitting Text

### Split by Pattern

```python
import re

# Split by whitespace
text = "one   two\tthree\nfour"
words = re.split(r'\s+', text)
print(words)  # ['one', 'two', 'three', 'four']

# Split by comma or semicolon
text = "apple,banana;orange,grape"
fruits = re.split(r'[,;]', text)
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# Split but keep delimiters
text = "Hello. World! How are you?"
parts = re.split(r'([.!?])', text)
print(parts)  # ['Hello', '.', ' World', '!', ' How are you', '?', '']
```

---

## Real-World Examples

### Log Parser

```python
import re
from datetime import datetime

def parse_log_line(line):
    """Parse a log entry."""
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+): (.+)'
    
    match = re.match(pattern, line)
    if not match:
        return None
    
    return {
        'timestamp': datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S'),
        'level': match.group(2),
        'component': match.group(3),
        'message': match.group(4)
    }


# Usage
log_lines = [
    "2026-02-12 14:30:45 ERROR Database: Connection failed",
    "2026-02-12 14:30:46 INFO AuthService: User logged in",
    "2026-02-12 14:30:47 WARNING Cache: Memory usage high"
]

for line in log_lines:
    entry = parse_log_line(line)
    if entry:
        print(f"[{entry['level']}] {entry['component']}: {entry['message']}")
```

### URL Extractor

```python
import re

def extract_urls(text):
    """Extract all URLs from text."""
    pattern = r'https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'
    return re.findall(pattern, text)


# Usage
text = """
Check out https://example.com for more info.
Also visit http://test.org/path/to/page and
https://subdomain.example.com/page?query=value
"""

urls = extract_urls(text)
for url in urls:
    print(url)
```

### Data Cleaner

```python
import re

def clean_text(text):
    """Clean and normalize text."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters (keep letters, numbers, basic punctuation)
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)
    
    # Trim
    text = text.strip()
    
    return text


# Usage
dirty_text = """
<p>Hello    world!</p>
<div>This  has   extra   spaces   and <b>HTML</b>.</div>
Special chars: @#$%^&*
"""

clean = clean_text(dirty_text)
print(clean)
# Hello world! This has extra spaces and HTML. Special chars
```

### Form Validator

```python
import re

class FormValidator:
    """Validate form inputs."""
    
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone):
        # Remove formatting
        digits = re.sub(r'\D', '', phone)
        return len(digits) == 10
    
    @staticmethod
    def validate_zip_code(zip_code):
        # US ZIP code: 12345 or 12345-6789
        pattern = r'^\d{5}(-\d{4})?$'
        return bool(re.match(pattern, zip_code))
    
    @staticmethod
    def validate_username(username):
        # 3-20 chars, letters, numbers, underscore
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return bool(re.match(pattern, username))


# Usage
validator = FormValidator()

print(validator.validate_email("user@example.com"))  # True
print(validator.validate_phone("(555) 123-4567"))    # True
print(validator.validate_zip_code("12345"))          # True
print(validator.validate_username("john_doe_123"))   # True
```

---

## Compilation and Performance

### Compiling Patterns

```python
import re

# Compile pattern once for reuse
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Use compiled pattern
emails = ["user@example.com", "invalid", "test@test.org"]

for email in emails:
    if email_pattern.match(email):
        print(f"✓ {email}")
    else:
        print(f"✗ {email}")
```

**When to Compile:**
- Pattern used multiple times
- Performance-critical code
- Want to set flags (e.g., `re.IGNORECASE`)

---

## Common Flags

```python
import re

text = "Hello World"

# Case-insensitive
matches = re.findall(r'hello', text, re.IGNORECASE)
print(matches)  # ['Hello']

# Multiline mode (^ and $ match line boundaries)
text = "Line 1\nLine 2\nLine 3"
matches = re.findall(r'^Line', text, re.MULTILINE)
print(matches)  # ['Line', 'Line', 'Line']

# Dot matches newline
text = "First\nSecond"
match = re.search(r'First.Second', text, re.DOTALL)
print(match.group())  # First\nSecond
```

**Common Flags:**
- `re.IGNORECASE` or `re.I` — Case-insensitive
- `re.MULTILINE` or `re.M` — ^ and $ match line boundaries
- `re.DOTALL` or `re.S` — . matches newline
- `re.VERBOSE` or `re.X` — Allow comments in pattern

---

## Best Practices

1. **Use raw strings** for patterns: `r'\d+'` instead of `'\\d+'`
2. **Compile frequently-used patterns** for better performance
3. **Keep patterns simple** — complex regex is hard to maintain
4. **Test thoroughly** with edge cases
5. **Use named groups** for readability: `(?P<name>...)`
6. **Comment complex patterns** using `re.VERBOSE`
7. **Don't use regex for HTML/XML** — use proper parsers (BeautifulSoup)

---

## Quick Reference

### Special Characters
- `.` — Any character except newline
- `^` — Start of string
- `$` — End of string
- `*` — 0 or more
- `+` — 1 or more
- `?` — 0 or 1
- `{n}` — Exactly n times
- `{n,m}` — Between n and m times

### Character Classes
- `[abc]` — Match a, b, or c
- `[^abc]` — Not a, b, or c
- `[a-z]` — Range a to z
- `\d` — Digit [0-9]
- `\w` — Word character [a-zA-Z0-9_]
- `\s` — Whitespace

### Functions
```python
re.search(pattern, text)    # Find first match
re.match(pattern, text)     # Match at start
re.findall(pattern, text)   # Find all matches
re.finditer(pattern, text)  # Iterator of matches
re.sub(pattern, repl, text) # Replace matches
re.split(pattern, text)     # Split by pattern
```

---

## Next Steps

1. **Practice:** Build validators for your application
2. **Try:** Parse real log files or CSV data
3. **Learn:** Study regex101.com for interactive testing
4. **Read:** Official `re` module documentation
5. **Challenge:** Parse HTML (then learn why you shouldn't use regex for HTML)

---

## Additional Resources

- **regex101.com:** Interactive regex tester with explanations
- **regexr.com:** Another great online regex tool
- **re module documentation:** Official Python docs
- **Regular Expressions Cookbook:** O'Reilly book for advanced patterns
