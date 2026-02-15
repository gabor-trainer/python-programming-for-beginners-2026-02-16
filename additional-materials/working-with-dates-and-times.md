# Working with Dates and Times

**Target Audience:** Day 3+ students handling temporal data  
**Prerequisites:** Basic syntax, strings, functions  
**Time to Learn:** 40-50 minutes  

---

## Introduction

Python's `datetime` module provides classes for working with dates and times. Use it for timestamps, scheduling, date arithmetic, and formatting.

**Key Classes:**
- `datetime` — Date and time combined
- `date` — Date only (year, month, day)
- `time` — Time only (hour, minute, second, microsecond)
- `timedelta` — Duration between dates/times

---

## Getting Current Date and Time

### Current Date and Time

```python
from datetime import datetime

# Current date and time
now = datetime.now()
print(now)  # 2026-02-12 14:30:45.123456

print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
```

### Today's Date

```python
from datetime import date

today = date.today()
print(today)  # 2026-02-12

print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")
print(f"Weekday: {today.weekday()}")  # Monday=0, Sunday=6
```

### Current Time

```python
from datetime import datetime

now = datetime.now()
current_time = now.time()

print(current_time)  # 14:30:45.123456
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")
```

---

## Creating Dates and Times

### Creating Specific Dates

```python
from datetime import date, datetime

# Create a specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15

# Create a specific datetime
meeting = datetime(2026, 3, 15, 14, 30, 0)
print(meeting)  # 2026-03-15 14:30:00

# Create from today
today = date.today()
new_year = date(today.year + 1, 1, 1)
print(f"Next New Year: {new_year}")
```

### Creating from Timestamp

```python
from datetime import datetime

# Unix timestamp (seconds since 1970-01-01)
timestamp = 1707739845
dt = datetime.fromtimestamp(timestamp)
print(dt)  # Converts to local datetime

# Get timestamp from datetime
now = datetime.now()
ts = now.timestamp()
print(f"Timestamp: {ts}")
```

---

## Formatting Dates and Times

### Using strftime (String From Time)

```python
from datetime import datetime

now = datetime.now()

# Common formats
print(now.strftime('%Y-%m-%d'))  # 2026-02-12
print(now.strftime('%d/%m/%Y'))  # 12/02/2026
print(now.strftime('%B %d, %Y'))  # February 12, 2026
print(now.strftime('%I:%M %p'))  # 02:30 PM
print(now.strftime('%H:%M:%S'))  # 14:30:45

# Custom format
print(now.strftime('%A, %B %d, %Y at %I:%M %p'))
# Wednesday, February 12, 2026 at 02:30 PM
```

**Common Format Codes:**
- `%Y` — Year with century (2026)
- `%y` — Year without century (26)
- `%m` — Month as number (02)
- `%B` — Month full name (February)
- `%b` — Month short name (Feb)
- `%d` — Day of month (12)
- `%A` — Weekday full name (Wednesday)
- `%a` — Weekday short name (Wed)
- `%H` — Hour 24-hour (14)
- `%I` — Hour 12-hour (02)
- `%M` — Minute (30)
- `%S` — Second (45)
- `%p` — AM/PM

### Using isoformat

```python
from datetime import datetime

now = datetime.now()

# ISO 8601 format (standard for APIs, databases)
print(now.isoformat())  # 2026-02-12T14:30:45.123456
```

---

## Parsing Dates from Strings

### Using strptime (String Parse Time)

```python
from datetime import datetime

# Parse date string
date_string = '2026-02-12'
dt = datetime.strptime(date_string, '%Y-%m-%d')
print(dt)  # 2026-02-12 00:00:00

# Parse datetime string
datetime_string = '12/02/2026 14:30'
dt = datetime.strptime(datetime_string, '%d/%m/%Y %H:%M')
print(dt)  # 2026-02-12 14:30:00

# Parse with text
text = 'Meeting on February 12, 2026'
dt = datetime.strptime('February 12, 2026', '%B %d, %Y')
print(dt)  # 2026-02-12 00:00:00
```

### Handling Parse Errors

```python
from datetime import datetime

def parse_date(date_string, format_string):
    """Parse date with error handling."""
    try:
        return datetime.strptime(date_string, format_string)
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None


# Valid
dt = parse_date('2026-02-12', '%Y-%m-%d')
print(dt)  # 2026-02-12 00:00:00

# Invalid
dt = parse_date('2026-13-40', '%Y-%m-%d')
print(dt)  # Error parsing date: day is out of range for month
```

---

## Date Arithmetic with timedelta

### Creating timedelta

```python
from datetime import timedelta

# Create durations
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
two_hours = timedelta(hours=2)
thirty_minutes = timedelta(minutes=30)

# Combined
duration = timedelta(days=7, hours=3, minutes=15, seconds=30)
print(duration)  # 7 days, 3:15:30
```

### Adding and Subtracting

```python
from datetime import date, datetime, timedelta

# Add to date
today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)  # Approximate

print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Subtract from datetime
now = datetime.now()
two_hours_ago = now - timedelta(hours=2)
print(f"Two hours ago: {two_hours_ago}")

# Combine multiple deltas
future = now + timedelta(days=7, hours=3, minutes=30)
print(f"Future time: {future}")
```

### Difference Between Dates

```python
from datetime import date, datetime

# Date difference
today = date.today()
birthday = date(1990, 5, 15)
age_delta = today - birthday

print(f"Days since birth: {age_delta.days}")
print(f"Years old: {age_delta.days // 365}")  # Approximate

# Datetime difference
now = datetime.now()
past = datetime(2026, 1, 1, 0, 0, 0)
delta = now - past

print(f"Days: {delta.days}")
print(f"Seconds: {delta.seconds}")
print(f"Total seconds: {delta.total_seconds()}")
```

### Practical Example: Days Until Event

```python
from datetime import date, timedelta

def days_until(target_date):
    """Calculate days until a future date."""
    today = date.today()
    delta = target_date - today
    
    if delta.days < 0:
        return f"Event was {abs(delta.days)} days ago"
    elif delta.days == 0:
        return "Event is today!"
    else:
        return f"{delta.days} days until event"


# Usage
christmas = date(2026, 12, 25)
print(days_until(christmas))

new_year = date(2027, 1, 1)
print(days_until(new_year))
```

---

## Comparing Dates and Times

### Comparison Operators

```python
from datetime import datetime

dt1 = datetime(2026, 1, 1)
dt2 = datetime(2026, 12, 31)

print(dt1 < dt2)   # True
print(dt1 > dt2)   # False
print(dt1 == dt2)  # False
print(dt1 != dt2)  # True
```

### Finding Min and Max

```python
from datetime import date

dates = [
    date(2026, 1, 15),
    date(2026, 3, 20),
    date(2025, 12, 1),
    date(2026, 2, 10)
]

earliest = min(dates)
latest = max(dates)

print(f"Earliest: {earliest}")  # 2025-12-01
print(f"Latest: {latest}")      # 2026-03-20
```

### Sorting Dates

```python
from datetime import datetime

events = [
    {'name': 'Meeting', 'date': datetime(2026, 2, 15, 14, 0)},
    {'name': 'Deadline', 'date': datetime(2026, 2, 10, 17, 0)},
    {'name': 'Launch', 'date': datetime(2026, 2, 20, 9, 0)}
]

# Sort by date
events.sort(key=lambda x: x['date'])

for event in events:
    print(f"{event['name']}: {event['date'].strftime('%B %d at %I:%M %p')}")

# Output:
# Deadline: February 10 at 05:00 PM
# Meeting: February 15 at 02:00 PM
# Launch: February 20 at 09:00 AM
```

---

## Working with Weekdays

### Getting Weekday

```python
from datetime import date

today = date.today()

# weekday(): Monday=0, Sunday=6
weekday_num = today.weekday()
print(f"Weekday number: {weekday_num}")

# isoweekday(): Monday=1, Sunday=7
iso_weekday = today.isoweekday()
print(f"ISO weekday: {iso_weekday}")

# Weekday names
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
            'Friday', 'Saturday', 'Sunday']
weekday_name = weekdays[today.weekday()]
print(f"Today is {weekday_name}")
```

### Finding Next Weekday

```python
from datetime import date, timedelta

def next_weekday(target_weekday):
    """
    Find next occurrence of a weekday.
    
    Args:
        target_weekday: 0=Monday, 6=Sunday
    
    Returns:
        date object of next occurrence
    """
    today = date.today()
    days_ahead = target_weekday - today.weekday()
    
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    
    return today + timedelta(days=days_ahead)


# Find next Monday (0)
next_monday = next_weekday(0)
print(f"Next Monday: {next_monday.strftime('%B %d, %Y')}")

# Find next Friday (4)
next_friday = next_weekday(4)
print(f"Next Friday: {next_friday.strftime('%B %d, %Y')}")
```

### Checking for Weekend

```python
from datetime import date

def is_weekend(check_date):
    """Check if date is Saturday or Sunday."""
    return check_date.weekday() >= 5


today = date.today()
if is_weekend(today):
    print("It's the weekend!")
else:
    print("It's a weekday")
```

---

## Working with Time Ranges

### Generating Date Range

```python
from datetime import date, timedelta

def date_range(start_date, end_date):
    """Generate all dates between start and end."""
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


# Generate all dates in February 2026
start = date(2026, 2, 1)
end = date(2026, 2, 28)

for day in date_range(start, end):
    print(day)
```

### Working Days Calculator

```python
from datetime import date, timedelta

def count_working_days(start_date, end_date):
    """Count weekdays (Monday-Friday) between two dates."""
    working_days = 0
    current = start_date
    
    while current <= end_date:
        if current.weekday() < 5:  # Monday=0, Friday=4
            working_days += 1
        current += timedelta(days=1)
    
    return working_days


start = date(2026, 2, 1)
end = date(2026, 2, 28)

total_days = (end - start).days + 1
working = count_working_days(start, end)
weekend = total_days - working

print(f"Total days: {total_days}")
print(f"Working days: {working}")
print(f"Weekend days: {weekend}")
```

---

## Real-World Examples

### Task Scheduler

```python
from datetime import datetime, timedelta

class Task:
    """A scheduled task."""
    
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
    
    def is_overdue(self):
        """Check if task is past due date."""
        return datetime.now() > self.due_date
    
    def time_remaining(self):
        """Get time remaining until due date."""
        delta = self.due_date - datetime.now()
        
        if delta.total_seconds() < 0:
            return "Overdue"
        
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        
        if days > 0:
            return f"{days} days, {hours} hours"
        elif hours > 0:
            return f"{hours} hours, {minutes} minutes"
        else:
            return f"{minutes} minutes"
    
    def __str__(self):
        status = "⚠️ OVERDUE" if self.is_overdue() else self.time_remaining()
        due_str = self.due_date.strftime('%B %d at %I:%M %p')
        return f"{self.name} - Due: {due_str} ({status})"


# Create tasks
tasks = [
    Task("Write report", datetime(2026, 2, 15, 17, 0)),
    Task("Team meeting", datetime(2026, 2, 12, 14, 30)),
    Task("Code review", datetime(2026, 2, 13, 10, 0))
]

# Display tasks sorted by due date
tasks.sort(key=lambda t: t.due_date)

print("Task List:")
print("-" * 50)
for task in tasks:
    print(task)
```

### Age Calculator

```python
from datetime import date

def calculate_age(birth_date):
    """Calculate age in years from birth date."""
    today = date.today()
    
    age = today.year - birth_date.year
    
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age


def detailed_age(birth_date):
    """Calculate detailed age (years, months, days)."""
    today = date.today()
    
    years = calculate_age(birth_date)
    
    # Calculate months
    if today.month >= birth_date.month:
        months = today.month - birth_date.month
    else:
        months = 12 + today.month - birth_date.month
        years -= 1
    
    # Calculate days
    if today.day >= birth_date.day:
        days = today.day - birth_date.day
    else:
        # Approximate (doesn't handle all edge cases)
        days = 30 + today.day - birth_date.day
        months -= 1
    
    return years, months, days


# Usage
birth_date = date(1990, 5, 15)

age = calculate_age(birth_date)
print(f"Age: {age} years")

years, months, days = detailed_age(birth_date)
print(f"Detailed age: {years} years, {months} months, {days} days")
```

### Meeting Duration Logger

```python
from datetime import datetime

class MeetingLogger:
    """Track meeting start and end times."""
    
    def __init__(self, title):
        self.title = title
        self.start_time = None
        self.end_time = None
    
    def start(self):
        """Start the meeting timer."""
        self.start_time = datetime.now()
        print(f"Meeting started: {self.start_time.strftime('%I:%M:%S %p')}")
    
    def end(self):
        """End the meeting timer."""
        if not self.start_time:
            print("Error: Meeting not started")
            return
        
        self.end_time = datetime.now()
        print(f"Meeting ended: {self.end_time.strftime('%I:%M:%S %p')}")
        
        duration = self.duration()
        print(f"Duration: {duration}")
    
    def duration(self):
        """Calculate meeting duration."""
        if not self.start_time or not self.end_time:
            return "Not available"
        
        delta = self.end_time - self.start_time
        
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60
        
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"


# Usage
meeting = MeetingLogger("Sprint Planning")
meeting.start()

# ... meeting happens ...

meeting.end()
```

---

## Common Patterns and Best Practices

### Always Use aware datetimes for production

```python
from datetime import datetime, timezone

# Naive datetime (no timezone info)
naive = datetime.now()
print(naive)  # 2026-02-12 14:30:45.123456

# Aware datetime (with UTC timezone)
aware = datetime.now(timezone.utc)
print(aware)  # 2026-02-12 14:30:45.123456+00:00
```

**Note:** For production applications, use `pytz` or `zoneinfo` (Python 3.9+) for proper timezone handling.

### Store UTC, Display Local

```python
from datetime import datetime, timezone

# Store in UTC
created_at = datetime.now(timezone.utc)

# Display in local time (for user)
local_time = created_at.astimezone()
print(local_time.strftime('%B %d, %Y at %I:%M %p'))
```

### Validate Date Ranges

```python
from datetime import date

def validate_date_range(start, end):
    """Ensure start date is before end date."""
    if start > end:
        raise ValueError(f"Start date ({start}) must be before end date ({end})")


try:
    start = date(2026, 3, 1)
    end = date(2026, 2, 1)
    validate_date_range(start, end)
except ValueError as e:
    print(f"Validation error: {e}")
```

---

## Quick Reference

### Import
```python
from datetime import datetime, date, time, timedelta
```

### Current Date/Time
```python
now = datetime.now()
today = date.today()
```

### Create Date/Time
```python
dt = datetime(2026, 2, 12, 14, 30, 0)
d = date(2026, 2, 12)
```

### Format to String
```python
now.strftime('%Y-%m-%d %H:%M:%S')
```

### Parse from String
```python
dt = datetime.strptime('2026-02-12', '%Y-%m-%d')
```

### Date Arithmetic
```python
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
difference = date2 - date1  # returns timedelta
```

### Compare Dates
```python
if date1 < date2:
    print("date1 is earlier")
```

---

## Next Steps

1. **Practice:** Calculate your age in days
2. **Build:** Create a countdown timer to an event
3. **Explore:** Learn about `zoneinfo` for timezone support (Python 3.9+)
4. **Read:** datetime module documentation
5. **Try:** Parse dates from real log files or CSV data

---

## Additional Resources

- **datetime documentation:** Official Python docs
- **dateutil library:** More powerful date parsing and arithmetic
- **pytz library:** Comprehensive timezone support
- **arrow library:** Modern alternative to datetime with cleaner API
