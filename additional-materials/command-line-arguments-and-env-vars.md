# Command-Line Arguments and Environment Variables

**Target Audience:** Day 3+ students building flexible scripts  
**Prerequisites:** Functions, strings, dictionaries, basic modules  
**Time to Learn:** 30-40 minutes  

---

## Introduction

Command-line arguments and environment variables make scripts flexible without editing code. Arguments customize behavior per execution. Environment variables configure behavior across multiple runs.

**Use Cases:**
- **Arguments:** File paths, processing options, flags
- **Environment Variables:** API keys, database URLs, configuration settings

---

## Command-Line Arguments with `sys.argv`

### Basic Usage

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Number of arguments:", len(sys.argv) - 1)

# Run: python script.py hello world 123
# Output:
# Script name: script.py
# Arguments: ['hello', 'world', '123']
# Number of arguments: 3
```

**Key Points:**
- `sys.argv[0]` is the script name
- `sys.argv[1:]` are the arguments
- All arguments are strings

### Simple File Processor

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python process.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        content = file.read()
    print(f"File {filename} has {len(content)} characters")
except FileNotFoundError:
    print(f"Error: {filename} not found")
    sys.exit(1)
```

**Usage:**
```powershell
python process.py data.txt
# File data.txt has 1234 characters

python process.py missing.txt
# Error: missing.txt not found
```

### Converting Argument Types

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python calculate.py <number1> <number2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    
    print(f"Sum: {num1 + num2}")
    print(f"Product: {num1 * num2}")

except ValueError:
    print("Error: Arguments must be numbers")
    sys.exit(1)
```

**Usage:**
```powershell
python calculate.py 10 5
# Sum: 15.0
# Product: 50.0

python calculate.py 3.5 2
# Sum: 5.5
# Product: 7.0
```

---

## Better Arguments with `argparse`

### Basic Setup

```python
import argparse

parser = argparse.ArgumentParser(description='Process a file')
parser.add_argument('filename', help='File to process')

args = parser.parse_args()

print(f"Processing: {args.filename}")
```

**Usage:**
```powershell
python script.py data.txt
# Processing: data.txt

python script.py --help
# usage: script.py [-h] filename
# Process a file
# positional arguments:
#   filename    File to process
```

### Optional Arguments

```python
import argparse

parser = argparse.ArgumentParser(description='File processor')

# Positional argument (required)
parser.add_argument('input', help='Input file')

# Optional arguments with flags
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('-v', '--verbose', action='store_true', 
                    help='Enable verbose mode')

args = parser.parse_args()

print(f"Input: {args.input}")
print(f"Output: {args.output}")
print(f"Verbose: {args.verbose}")
```

**Usage:**
```powershell
python script.py data.txt
# Input: data.txt
# Output: None
# Verbose: False

python script.py data.txt -o result.txt -v
# Input: data.txt
# Output: result.txt
# Verbose: True

python script.py data.txt --output=result.txt --verbose
# Input: data.txt
# Output: result.txt
# Verbose: True
```

### Type Conversion and Validation

```python
import argparse

parser = argparse.ArgumentParser(description='Temperature converter')

parser.add_argument('temperature', type=float, help='Temperature value')
parser.add_argument('-u', '--unit', choices=['C', 'F'], default='C',
                    help='Unit: C (Celsius) or F (Fahrenheit)')

args = parser.parse_args()

if args.unit == 'C':
    fahrenheit = args.temperature * 9/5 + 32
    print(f"{args.temperature}°C = {fahrenheit:.1f}°F")
else:
    celsius = (args.temperature - 32) * 5/9
    print(f"{args.temperature}°F = {celsius:.1f}°C")
```

**Usage:**
```powershell
python convert.py 25
# 25.0°C = 77.0°F

python convert.py 77 -u F
# 77.0°F = 25.0°C

python convert.py 100 --unit=X
# error: argument -u/--unit: invalid choice: 'X' (choose from 'C', 'F')
```

### Multiple Values

```python
import argparse

parser = argparse.ArgumentParser(description='Calculate average')
parser.add_argument('numbers', type=float, nargs='+',
                    help='Numbers to average')

args = parser.parse_args()

average = sum(args.numbers) / len(args.numbers)
print(f"Numbers: {args.numbers}")
print(f"Average: {average:.2f}")
```

**Usage:**
```powershell
python average.py 10 20 30 40
# Numbers: [10.0, 20.0, 30.0, 40.0]
# Average: 25.00

python average.py 5
# Numbers: [5.0]
# Average: 5.00
```

**`nargs` options:**
- `'+'` — One or more values
- `'*'` — Zero or more values
- `3` — Exactly 3 values
- `'?'` — Optional single value

### Real-World Example: File Backup Tool

```python
import argparse
import shutil
from datetime import datetime
from pathlib import Path

def backup_file(source, destination, compress):
    """Create backup of file."""
    source_path = Path(source)
    
    if not source_path.exists():
        print(f"Error: {source} not found")
        return False
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{source_path.stem}_{timestamp}{source_path.suffix}"
    
    if destination:
        dest_dir = Path(destination)
        dest_dir.mkdir(parents=True, exist_ok=True)
        backup_path = dest_dir / backup_name
    else:
        backup_path = source_path.parent / backup_name
    
    # Compress or copy
    if compress:
        shutil.make_archive(
            str(backup_path.with_suffix('')),
            'zip',
            source_path.parent,
            source_path.name
        )
        print(f"✓ Compressed backup: {backup_path}.zip")
    else:
        shutil.copy2(source, backup_path)
        print(f"✓ Backup created: {backup_path}")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Create timestamped file backups',
        epilog='Example: python backup.py document.txt -d ./backups -c'
    )
    
    parser.add_argument('file', help='File to backup')
    parser.add_argument('-d', '--destination', 
                        help='Backup directory (default: same as source)')
    parser.add_argument('-c', '--compress', action='store_true',
                        help='Compress backup as ZIP')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show detailed information')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Source: {args.file}")
        print(f"Destination: {args.destination or 'Same directory'}")
        print(f"Compress: {args.compress}")
        print("-" * 50)
    
    backup_file(args.file, args.destination, args.compress)


if __name__ == '__main__':
    main()
```

**Usage:**
```powershell
# Simple backup in same folder
python backup.py report.txt
# ✓ Backup created: report_20260212_143045.txt

# Backup to specific folder
python backup.py report.txt -d ./backups
# ✓ Backup created: backups/report_20260212_143100.txt

# Compressed backup
python backup.py report.txt --destination=./backups --compress --verbose
# Source: report.txt
# Destination: ./backups
# Compress: True
# --------------------------------------------------
# ✓ Compressed backup: backups/report_20260212_143130.zip
```

---

## Environment Variables

### Reading Environment Variables

```python
import os

# Get environment variable
python_path = os.environ.get('PYTHONPATH')
print(f"PYTHONPATH: {python_path}")

# Get with default value
debug_mode = os.environ.get('DEBUG', 'False')
print(f"Debug mode: {debug_mode}")

# Check if variable exists
if 'HOME' in os.environ:
    print(f"Home directory: {os.environ['HOME']}")

# Get all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")
```

### Setting Environment Variables (In Python)

```python
import os

# Set for current process and child processes
os.environ['MY_API_KEY'] = 'abc123'
os.environ['DEBUG'] = 'True'

# Access it
print(os.environ['MY_API_KEY'])  # abc123
```

**Note:** This only affects the current Python process, not the system.

### Setting Environment Variables (System-Wide)

**Windows PowerShell:**
```powershell
# Temporary (current session)
$env:API_KEY = "abc123"

# Permanent (user)
[System.Environment]::SetEnvironmentVariable('API_KEY', 'abc123', 'User')

# Permanent (system - requires admin)
[System.Environment]::SetEnvironmentVariable('API_KEY', 'abc123', 'Machine')
```

**Windows Command Prompt:**
```cmd
# Temporary
set API_KEY=abc123

# Permanent (user)
setx API_KEY "abc123"
```

### Using `.env` Files (Python-dotenv)

Create a `.env` file:
```
# .env
DATABASE_URL=postgresql://localhost:5432/mydb
API_KEY=secret_key_here
DEBUG=True
MAX_CONNECTIONS=100
```

Load it in Python:
```python
# Install first: uv add python-dotenv
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
db_url = os.environ.get('DATABASE_URL')
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG') == 'True'
max_conn = int(os.environ.get('MAX_CONNECTIONS', 50))

print(f"Database: {db_url}")
print(f"API Key: {api_key}")
print(f"Debug: {debug}")
print(f"Max connections: {max_conn}")
```

**Advantages:**
- Keep secrets out of code
- Easy to change configuration
- Different `.env` files for development/production
- Add `.env` to `.gitignore` to avoid committing secrets

### Real-World Example: API Client

```python
import os
import requests
from dotenv import load_dotenv

class WeatherClient:
    """Weather API client using environment variables."""
    
    def __init__(self):
        load_dotenv()
        
        self.api_key = os.environ.get('WEATHER_API_KEY')
        self.base_url = os.environ.get(
            'WEATHER_API_URL',
            'https://api.weather.com/v1'
        )
        
        if not self.api_key:
            raise ValueError("WEATHER_API_KEY not set in environment")
    
    def get_weather(self, city):
        """Get current weather for city."""
        url = f"{self.base_url}/current"
        params = {
            'city': city,
            'apikey': self.api_key
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        return response.json()


# Usage
try:
    client = WeatherClient()
    weather = client.get_weather('New York')
    print(f"Temperature: {weather['temp']}°C")
except ValueError as e:
    print(f"Configuration error: {e}")
except requests.RequestException as e:
    print(f"API error: {e}")
```

**.env file:**
```
WEATHER_API_KEY=your_api_key_here
WEATHER_API_URL=https://api.weather.com/v1
```

---

## Combining Arguments and Environment Variables

```python
import argparse
import os
from dotenv import load_dotenv

def get_config():
    """Get configuration from environment and arguments."""
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Database backup tool')
    
    # Arguments can override environment variables
    parser.add_argument('--db-host', 
                        default=os.environ.get('DB_HOST', 'localhost'),
                        help='Database host')
    parser.add_argument('--db-port', type=int,
                        default=int(os.environ.get('DB_PORT', '5432')),
                        help='Database port')
    parser.add_argument('--db-name',
                        default=os.environ.get('DB_NAME', 'mydb'),
                        help='Database name')
    parser.add_argument('-o', '--output',
                        default=os.environ.get('BACKUP_DIR', './backups'),
                        help='Backup output directory')
    
    return parser.parse_args()


def main():
    config = get_config()
    
    print("Database Configuration:")
    print(f"  Host: {config.db_host}")
    print(f"  Port: {config.db_port}")
    print(f"  Name: {config.db_name}")
    print(f"  Output: {config.output}")
    
    # Run backup...
    print(f"\nBacking up {config.db_name} to {config.output}")


if __name__ == '__main__':
    main()
```

**.env file:**
```
DB_HOST=production.db.server
DB_PORT=5432
DB_NAME=production_db
BACKUP_DIR=/mnt/backups
```

**Usage:**
```powershell
# Use all defaults from .env
python backup_db.py
# Database Configuration:
#   Host: production.db.server
#   Port: 5432
#   Name: production_db
#   Output: /mnt/backups

# Override specific values
python backup_db.py --db-host localhost --output ./local_backups
# Database Configuration:
#   Host: localhost
#   Port: 5432
#   Name: production_db
#   Output: ./local_backups
```

**Priority Order:**
1. Command-line arguments (highest)
2. Environment variables
3. Default values (lowest)

---

## Best Practices

### Command-Line Arguments

1. **Provide clear help text** with `--help`
2. **Use meaningful argument names:** `--output` not `-o` alone
3. **Set sensible defaults** when possible
4. **Validate inputs** early and provide clear error messages
5. **Use `type=` for automatic conversion** (int, float, Path)

### Environment Variables

1. **Use uppercase** with underscores: `API_KEY`, `DATABASE_URL`
2. **Prefix with app name** to avoid conflicts: `MYAPP_DEBUG`
3. **Never commit `.env` files** — add to `.gitignore`
4. **Provide `.env.example`** with dummy values:
   ```
   # .env.example
   API_KEY=your_key_here
   DATABASE_URL=postgresql://localhost/dbname
   ```
5. **Document required variables** in README

### Security

1. **Never hardcode secrets** in source code
2. **Use environment variables** for API keys, passwords, tokens
3. **Restrict file permissions** on `.env` files
4. **Rotate secrets regularly**
5. **Use secret management tools** in production (AWS Secrets Manager, Azure Key Vault)

---

## Practical Example: Configurable Script

```python
import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Data processing pipeline',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-f', '--format', 
                        choices=['json', 'csv', 'txt'],
                        default='json',
                        help='Output format')
    parser.add_argument('--max-rows', type=int,
                        help='Maximum rows to process')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without doing it')
    
    return parser.parse_args()


def load_config():
    """Load configuration from environment."""
    load_dotenv()
    
    return {
        'max_memory': int(os.environ.get('MAX_MEMORY_MB', '512')),
        'temp_dir': os.environ.get('TEMP_DIR', './temp'),
        'log_level': os.environ.get('LOG_LEVEL', 'INFO'),
        'parallel': os.environ.get('ENABLE_PARALLEL', 'False') == 'True'
    }


def main():
    args = parse_arguments()
    config = load_config()
    
    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)
    
    # Determine output file
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix(f'.{args.format}')
    
    # Show configuration
    if args.verbose:
        print("Configuration:")
        print(f"  Input: {input_path}")
        print(f"  Output: {output_path}")
        print(f"  Format: {args.format}")
        print(f"  Max rows: {args.max_rows or 'unlimited'}")
        print(f"  Max memory: {config['max_memory']} MB")
        print(f"  Temp dir: {config['temp_dir']}")
        print(f"  Parallel: {config['parallel']}")
        print(f"  Dry run: {args.dry_run}")
        print("-" * 50)
    
    if args.dry_run:
        print("DRY RUN: Would process file")
        return
    
    # Process file
    print(f"Processing {input_path}...")
    # ... actual processing logic ...
    print(f"✓ Saved to {output_path}")


if __name__ == '__main__':
    main()
```

**.env file:**
```
MAX_MEMORY_MB=1024
TEMP_DIR=C:/Temp
LOG_LEVEL=DEBUG
ENABLE_PARALLEL=True
```

**Usage:**
```powershell
# Basic usage
python process.py data.csv

# Full customization
python process.py data.csv -o result.json -f json --max-rows 1000 -v

# Dry run to test
python process.py data.csv --dry-run --verbose
```

---

## Quick Reference

### sys.argv
```python
import sys
filename = sys.argv[1]  # First argument
count = int(sys.argv[2])  # Convert to int
```

### argparse Basics
```python
import argparse
parser = argparse.ArgumentParser(description='Tool description')
parser.add_argument('required', help='Required argument')
parser.add_argument('-o', '--optional', help='Optional argument')
parser.add_argument('-f', '--flag', action='store_true', help='Boolean flag')
args = parser.parse_args()
```

### Environment Variables
```python
import os
api_key = os.environ.get('API_KEY')  # Safe (returns None if missing)
api_key = os.environ['API_KEY']  # Raises KeyError if missing
os.environ['NEW_VAR'] = 'value'  # Set variable
```

### python-dotenv
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file
value = os.environ.get('VAR_NAME')
```

---

## Next Steps

1. **Add arguments** to your existing scripts
2. **Create `.env` file** for configuration
3. **Combine both** for maximum flexibility
4. **Read:** argparse documentation for advanced features
5. **Practice:** Build a configurable tool from scratch

---

## Additional Resources

- **argparse documentation:** Official Python docs
- **python-dotenv:** Environment variable management
- **click library:** Alternative to argparse with decorator syntax
- **configparser:** INI-style configuration files
