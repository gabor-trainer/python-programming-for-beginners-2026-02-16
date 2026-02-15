# Working with CSV and JSON Files

**Target Audience:** Day 3+ students working with structured data  
**Prerequisites:** File I/O, dictionaries, lists, loops  
**Time to Learn:** 30-45 minutes  

---

## Introduction

CSV and JSON are the most common formats for data exchange. CSV (Comma-Separated Values) is simple and universal. JSON (JavaScript Object Notation) handles complex nested structures.

**When to Use Each:**
- **CSV:** Tabular data, spreadsheet exports, database dumps, simple lists
- **JSON:** API responses, configuration files, nested data, mixed types

---

## CSV Files

### Reading CSV Files

Python's `csv` module handles CSV parsing:

```python
import csv

# Basic reading
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)  # Each row is a list

# Example output:
# ['Name', 'Age', 'City']
# ['Alice', '30', 'New York']
# ['Bob', '25', 'Boston']
```

### Using DictReader for Named Columns

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)  # Each row is a dictionary
        print(f"{row['Name']} is {row['Age']} years old")

# Example output:
# {'Name': 'Alice', 'Age': '30', 'City': 'New York'}
# Alice is 30 years old
# {'Name': 'Bob', 'Age': '25', 'City': 'Boston'}
# Bob is 25 years old
```

**Advantage:** Access columns by name instead of index.

### Writing CSV Files

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Boston']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once
```

**Important:** Use `newline=''` on Windows to avoid extra blank lines.

### Writing with DictWriter

```python
import csv

data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Boston'}
]

with open('output.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write column names
    writer.writerows(data)
```

### Handling Different Delimiters

```python
import csv

# Read TSV (tab-separated values)
with open('data.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)

# Read pipe-delimited file
with open('data.txt', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        print(row)
```

### Handling Quotes and Special Characters

```python
import csv

# Data with commas and quotes
data = [
    ['Name', 'Description'],
    ['Product A', 'A "premium" item, now on sale'],
    ['Product B', 'Contains, commas']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

# Output in file:
# Name,Description
# Product A,"A ""premium"" item, now on sale"
# Product B,"Contains, commas"
```

### Real-World Example: Sales Report

```python
import csv

def load_sales(filename):
    """Load sales data from CSV file."""
    sales = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Convert numeric fields
            row['Price'] = float(row['Price'])
            row['Quantity'] = int(row['Quantity'])
            row['Total'] = row['Price'] * row['Quantity']
            sales.append(row)
    
    return sales


def generate_report(sales):
    """Calculate sales statistics."""
    total_revenue = sum(sale['Total'] for sale in sales)
    total_items = sum(sale['Quantity'] for sale in sales)
    
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Items: {total_items}")
    print(f"Average Sale: ${total_revenue / len(sales):.2f}")


def save_summary(sales, output_file):
    """Save sales summary to new CSV."""
    with open(output_file, 'w', newline='') as file:
        fieldnames = ['Product', 'Quantity', 'Total']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for sale in sales:
            writer.writerow({
                'Product': sale['Product'],
                'Quantity': sale['Quantity'],
                'Total': sale['Total']
            })


# Usage
sales = load_sales('sales.csv')
generate_report(sales)
save_summary(sales, 'summary.csv')
```

**Input file (sales.csv):**
```
Product,Price,Quantity
Laptop,899.99,5
Mouse,24.99,20
Keyboard,79.99,10
```

**Output:**
```
Total Revenue: $5,499.75
Total Items: 35
Average Sale: $1,833.25
```

---

## JSON Files

### Reading JSON Files

```python
import json

# Read JSON from file
with open('data.json', 'r') as file:
    data = json.load(file)  # Parse JSON to Python objects

print(data)
print(type(data))  # dict or list
```

### Writing JSON Files

```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'SQL', 'Excel']
}

# Write JSON to file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 for readability
```

**Output file (output.json):**
```json
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": [
        "Python",
        "SQL",
        "Excel"
    ]
}
```

### Working with JSON Strings

```python
import json

# Parse JSON string
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)  # Note: loads (string), not load (file)
print(data['name'])  # Bob

# Convert to JSON string
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data, indent=2)
print(json_string)
```

### Nested JSON Structures

```python
import json

# Complex nested data
data = {
    'company': 'TechCorp',
    'employees': [
        {
            'name': 'Alice',
            'role': 'Developer',
            'skills': ['Python', 'JavaScript'],
            'contact': {
                'email': 'alice@techcorp.com',
                'phone': '555-0001'
            }
        },
        {
            'name': 'Bob',
            'role': 'Designer',
            'skills': ['Photoshop', 'Figma'],
            'contact': {
                'email': 'bob@techcorp.com',
                'phone': '555-0002'
            }
        }
    ]
}

# Save with pretty printing
with open('company.json', 'w') as file:
    json.dump(data, file, indent=4)

# Read and navigate
with open('company.json', 'r') as file:
    company = json.load(file)

# Access nested data
for employee in company['employees']:
    print(f"{employee['name']} - {employee['role']}")
    print(f"Email: {employee['contact']['email']}")
    print(f"Skills: {', '.join(employee['skills'])}")
    print()
```

### Handling Type Conversions

```python
import json

# Python → JSON type mapping
data = {
    'string': 'text',
    'integer': 42,
    'float': 3.14,
    'boolean': True,
    'none': None,
    'list': [1, 2, 3],
    'dict': {'key': 'value'}
}

json_string = json.dumps(data)
print(json_string)

# Output:
# {"string": "text", "integer": 42, "float": 3.14, 
#  "boolean": true, "none": null, "list": [1, 2, 3], 
#  "dict": {"key": "value"}}
```

**Note:** Python's `True`/`False`/`None` become JSON's `true`/`false`/`null`.

### Real-World Example: Configuration File

```python
import json
from pathlib import Path

class Config:
    """Application configuration manager."""
    
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load()
    
    def load(self):
        """Load configuration from file or create default."""
        if Path(self.config_file).exists():
            with open(self.config_file, 'r') as file:
                return json.load(file)
        else:
            return self.create_default()
    
    def create_default(self):
        """Create default configuration."""
        default = {
            'app_name': 'MyApp',
            'version': '1.0.0',
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'mydb'
            },
            'features': {
                'debug_mode': False,
                'auto_save': True,
                'theme': 'dark'
            }
        }
        self.save(default)
        return default
    
    def save(self, settings=None):
        """Save configuration to file."""
        if settings is None:
            settings = self.settings
        
        with open(self.config_file, 'w') as file:
            json.dump(settings, file, indent=4)
    
    def get(self, key, default=None):
        """Get configuration value by dot notation."""
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Set configuration value by dot notation."""
        keys = key.split('.')
        current = self.settings
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
        self.save()


# Usage
config = Config('app_config.json')

# Get settings
print(config.get('app_name'))  # MyApp
print(config.get('database.host'))  # localhost
print(config.get('features.debug_mode'))  # False

# Update settings
config.set('features.debug_mode', True)
config.set('database.port', 3306)

print(config.get('features.debug_mode'))  # True
```

---

## CSV vs JSON Comparison

### Use CSV When:

✅ Data is tabular (rows and columns)  
✅ Opening in Excel or Google Sheets  
✅ Simple data types (strings, numbers)  
✅ Large datasets (CSV is more memory efficient)  
✅ Exchanging data with non-programmers  

**Example:**
```csv
Name,Email,Department,Salary
Alice,alice@company.com,Engineering,95000
Bob,bob@company.com,Marketing,75000
```

### Use JSON When:

✅ Nested or hierarchical data  
✅ Working with APIs  
✅ Configuration files  
✅ Mixed data types (strings, numbers, booleans, nulls)  
✅ Need to preserve structure  

**Example:**
```json
{
    "employees": [
        {
            "name": "Alice",
            "email": "alice@company.com",
            "department": "Engineering",
            "salary": 95000,
            "skills": ["Python", "SQL"],
            "active": true
        }
    ]
}
```

---

## Converting Between CSV and JSON

### CSV to JSON

```python
import csv
import json

def csv_to_json(csv_file, json_file):
    """Convert CSV file to JSON."""
    data = []
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


# Usage
csv_to_json('employees.csv', 'employees.json')
```

**Input (employees.csv):**
```csv
Name,Age,Department
Alice,30,Engineering
Bob,25,Marketing
```

**Output (employees.json):**
```json
[
    {
        "Name": "Alice",
        "Age": "30",
        "Department": "Engineering"
    },
    {
        "Name": "Bob",
        "Age": "25",
        "Department": "Marketing"
    }
]
```

### JSON to CSV

```python
import csv
import json

def json_to_csv(json_file, csv_file):
    """Convert JSON file to CSV."""
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Assume data is a list of dictionaries
    if not data:
        return
    
    fieldnames = data[0].keys()
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Usage
json_to_csv('employees.json', 'employees.csv')
```

---

## Practical Example: Data Processing Pipeline

```python
import csv
import json
from datetime import datetime


def load_transactions(csv_file):
    """Load transaction data from CSV."""
    transactions = []
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            transactions.append({
                'id': int(row['TransactionID']),
                'date': row['Date'],
                'amount': float(row['Amount']),
                'category': row['Category'],
                'description': row['Description']
            })
    
    return transactions


def analyze_transactions(transactions):
    """Calculate statistics by category."""
    categories = {}
    
    for trans in transactions:
        category = trans['category']
        
        if category not in categories:
            categories[category] = {
                'count': 0,
                'total': 0,
                'transactions': []
            }
        
        categories[category]['count'] += 1
        categories[category]['total'] += trans['amount']
        categories[category]['transactions'].append(trans)
    
    return categories


def generate_report(categories, output_file):
    """Save analysis results to JSON."""
    report = {
        'generated': datetime.now().isoformat(),
        'summary': {},
        'details': []
    }
    
    # Summary
    for category, data in categories.items():
        report['summary'][category] = {
            'count': data['count'],
            'total': round(data['total'], 2),
            'average': round(data['total'] / data['count'], 2)
        }
    
    # Top transactions by category
    for category, data in categories.items():
        top_trans = sorted(
            data['transactions'],
            key=lambda x: x['amount'],
            reverse=True
        )[:3]
        
        report['details'].append({
            'category': category,
            'top_transactions': top_trans
        })
    
    # Save to JSON
    with open(output_file, 'w') as file:
        json.dump(report, file, indent=4)


# Usage
transactions = load_transactions('transactions.csv')
categories = analyze_transactions(transactions)
generate_report(categories, 'financial_report.json')

print("Report generated: financial_report.json")
```

**Input (transactions.csv):**
```csv
TransactionID,Date,Amount,Category,Description
1,2026-01-15,45.50,Food,Grocery shopping
2,2026-01-16,120.00,Entertainment,Movie tickets
3,2026-01-17,35.20,Food,Restaurant
```

**Output (financial_report.json):**
```json
{
    "generated": "2026-02-12T14:30:00",
    "summary": {
        "Food": {
            "count": 2,
            "total": 80.70,
            "average": 40.35
        },
        "Entertainment": {
            "count": 1,
            "total": 120.00,
            "average": 120.00
        }
    },
    "details": [...]
}
```

---

## Error Handling

### CSV Error Handling

```python
import csv

def safe_load_csv(filename):
    """Load CSV with error handling."""
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    
    except csv.Error as e:
        print(f"CSV error: {e}")
        return []
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
```

### JSON Error Handling

```python
import json

def safe_load_json(filename):
    """Load JSON with error handling."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

---

## Best Practices

### CSV Best Practices

1. **Always use `newline=''` in `open()` on Windows**
2. **Use `DictReader` for readable code**
3. **Specify encoding for non-ASCII characters:** `open('file.csv', encoding='utf-8')`
4. **Handle missing fields gracefully**
5. **Strip whitespace from values when needed**

### JSON Best Practices

1. **Use `indent` parameter for human-readable files**
2. **Validate JSON structure after loading**
3. **Use `.get()` for dictionaries to avoid KeyError**
4. **Consider `ensure_ascii=False` for non-English text**
5. **Don't store large binary data in JSON**

---

## Next Steps

1. **Practice:** Convert between CSV and JSON formats
2. **Explore:** Try reading files from real-world sources (government data, APIs)
3. **Extend:** Add data validation and cleaning
4. **Learn:** Explore pandas library for advanced data manipulation

---

## Additional Resources

- **csv module documentation:** Built-in CSV handling
- **json module documentation:** Built-in JSON handling
- **pandas library:** Professional data analysis (handles both CSV and JSON)
- **jsonschema library:** Validate JSON structure against schemas
