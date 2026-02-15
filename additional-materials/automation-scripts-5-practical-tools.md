# Automation Scripts: 5 Practical Tools You Can Build Today

**Target Audience:** Day 4+ students ready to apply Python immediately  
**Prerequisites:** Core syntax, functions, file I/O, basic modules  
**Time to Build:** 15-30 minutes per script  

---

## Introduction

Python excels at automating repetitive tasks. This guide presents five production-ready scripts that solve real problems. Each includes working code, usage examples, and enhancement ideas.

**What You'll Build:**
1. File organizer that sorts downloads by type
2. Bulk file renamer with pattern matching
3. Email extractor from text files
4. Image resizer for batch processing
5. Automated backup script with rotation

---

## Script 1: Download Folder Organizer

**Problem:** Downloads folder becomes cluttered with mixed file types.

**Solution:** Automatically sort files into category folders.

### Full Code

```python
# organize_downloads.py
import os
import shutil
from pathlib import Path

# Define file categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.json', '.xml'],
    'Executables': ['.exe', '.msi', '.dmg', '.pkg'],
}


def get_category(file_path):
    """Return category name for file based on extension."""
    extension = file_path.suffix.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    
    return 'Others'


def organize_folder(source_folder):
    """Organize files in source_folder into category subfolders."""
    source = Path(source_folder)
    
    if not source.exists():
        print(f"Error: {source_folder} does not exist")
        return
    
    files_moved = 0
    
    # Process each file
    for item in source.iterdir():
        # Skip if it's a directory or hidden file
        if item.is_dir() or item.name.startswith('.'):
            continue
        
        # Determine category
        category = get_category(item)
        
        # Create category folder if needed
        category_path = source / category
        category_path.mkdir(exist_ok=True)
        
        # Move file
        destination = category_path / item.name
        
        # Handle name conflicts
        if destination.exists():
            base = item.stem
            extension = item.suffix
            counter = 1
            
            while destination.exists():
                new_name = f"{base}_{counter}{extension}"
                destination = category_path / new_name
                counter += 1
        
        shutil.move(str(item), str(destination))
        print(f"Moved: {item.name} → {category}/")
        files_moved += 1
    
    print(f"\n✓ Organized {files_moved} files")


def main():
    """Run the organizer on Downloads folder."""
    downloads = Path.home() / 'Downloads'
    
    print(f"Organizing: {downloads}")
    print("-" * 50)
    
    organize_folder(downloads)


if __name__ == '__main__':
    main()
```

### Usage

```powershell
# Run on your Downloads folder
python organize_downloads.py

# Moved: report.pdf → Documents/
# Moved: vacation.jpg → Images/
# Moved: setup.exe → Executables/
# ✓ Organized 47 files
```

### Enhancements

- Add command-line argument for custom folder path
- Create undo function that reverses organization
- Add dry-run mode to preview changes
- Log all operations to file with timestamps
- Schedule with Windows Task Scheduler to run daily

---

## Script 2: Bulk File Renamer

**Problem:** Need to rename dozens of files with consistent pattern.

**Solution:** Pattern-based renaming with preview and safety checks.

### Full Code

```python
# bulk_rename.py
import os
import sys
from pathlib import Path


def preview_rename(folder, old_pattern, new_pattern, extension=None):
    """Show what files will be renamed without making changes."""
    folder_path = Path(folder)
    
    if not folder_path.exists():
        print(f"Error: {folder} does not exist")
        return []
    
    changes = []
    
    for file_path in folder_path.iterdir():
        if file_path.is_dir():
            continue
        
        # Filter by extension if specified
        if extension and file_path.suffix.lower() != extension.lower():
            continue
        
        old_name = file_path.name
        
        # Check if pattern exists in filename
        if old_pattern in old_name:
            new_name = old_name.replace(old_pattern, new_pattern)
            changes.append((file_path, old_name, new_name))
    
    return changes


def apply_rename(changes):
    """Apply the rename operations."""
    success_count = 0
    
    for file_path, old_name, new_name in changes:
        try:
            new_path = file_path.parent / new_name
            
            # Check if target already exists
            if new_path.exists():
                print(f"✗ Skip {old_name}: {new_name} already exists")
                continue
            
            file_path.rename(new_path)
            print(f"✓ {old_name} → {new_name}")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error renaming {old_name}: {e}")
    
    return success_count


def main():
    """Interactive bulk rename tool."""
    print("Bulk File Renamer")
    print("=" * 50)
    
    # Get inputs
    folder = input("Folder path: ").strip()
    
    if not folder:
        folder = '.'
    
    old_pattern = input("Text to replace: ").strip()
    
    if not old_pattern:
        print("Error: Pattern cannot be empty")
        sys.exit(1)
    
    new_pattern = input("Replace with: ").strip()
    extension = input("File extension (optional, e.g., .jpg): ").strip()
    
    if extension and not extension.startswith('.'):
        extension = '.' + extension
    
    # Preview changes
    print("\nPreview:")
    print("-" * 50)
    
    changes = preview_rename(folder, old_pattern, new_pattern, extension)
    
    if not changes:
        print("No matching files found")
        return
    
    for _, old_name, new_name in changes:
        print(f"  {old_name}")
        print(f"→ {new_name}")
        print()
    
    print(f"Total: {len(changes)} files")
    
    # Confirm
    confirm = input("\nProceed with rename? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        print("\nRenaming:")
        print("-" * 50)
        success = apply_rename(changes)
        print(f"\n✓ Renamed {success} of {len(changes)} files")
    else:
        print("Cancelled")


if __name__ == '__main__':
    main()
```

### Usage Examples

```powershell
# Interactive mode
python bulk_rename.py

# Example session:
# Folder path: ./photos
# Text to replace: IMG_
# Replace with: Vacation_2025_
# File extension (optional): .jpg
# 
# Preview:
# IMG_0001.jpg → Vacation_2025_0001.jpg
# IMG_0002.jpg → Vacation_2025_0002.jpg
# Total: 24 files
# 
# Proceed? (yes/no): yes
# ✓ Renamed 24 of 24 files
```

### Enhancements

- Add regular expressions for complex patterns
- Support sequential numbering with padding
- Handle date-based renaming (creation/modified date)
- Add case conversion (lowercase, uppercase, title case)
- Create undo file to reverse operations

---

## Script 3: Email Extractor

**Problem:** Extract email addresses from text files, web scrapes, or logs.

**Solution:** Pattern matching with validation and deduplication.

### Full Code

```python
# extract_emails.py
import re
import sys
from pathlib import Path


def is_valid_email(email):
    """Basic email format validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def extract_emails_from_text(text):
    """Extract all email addresses from text."""
    # More permissive pattern for extraction
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    potential_emails = re.findall(pattern, text)
    
    # Validate each match
    valid_emails = [email.lower() for email in potential_emails 
                    if is_valid_email(email)]
    
    return valid_emails


def extract_from_file(file_path):
    """Extract emails from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        return extract_emails_from_text(text)
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []


def extract_from_folder(folder_path, extensions=None):
    """Extract emails from all files in folder."""
    if extensions is None:
        extensions = ['.txt', '.html', '.log', '.csv']
    
    all_emails = []
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: {folder_path} does not exist")
        return []
    
    for file_path in folder.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            print(f"Scanning: {file_path.name}")
            emails = extract_from_file(file_path)
            all_emails.extend(emails)
    
    return all_emails


def save_emails(emails, output_file):
    """Save emails to file, one per line."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for email in emails:
            f.write(email + '\n')


def main():
    """Extract emails from files and save to output."""
    if len(sys.argv) < 2:
        print("Usage: python extract_emails.py <file_or_folder> [output.txt]")
        print("\nExamples:")
        print("  python extract_emails.py document.txt")
        print("  python extract_emails.py ./data/ emails.txt")
        sys.exit(1)
    
    source = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else 'extracted_emails.txt'
    
    source_path = Path(source)
    
    print("Email Extractor")
    print("=" * 50)
    
    # Extract from file or folder
    if source_path.is_file():
        print(f"Source: {source} (file)")
        emails = extract_from_file(source)
    elif source_path.is_dir():
        print(f"Source: {source} (folder)")
        emails = extract_from_folder(source)
    else:
        print(f"Error: {source} not found")
        sys.exit(1)
    
    # Remove duplicates and sort
    unique_emails = sorted(set(emails))
    
    print(f"\nFound: {len(emails)} total, {len(unique_emails)} unique")
    
    if unique_emails:
        # Save to file
        save_emails(unique_emails, output)
        print(f"Saved to: {output}")
        
        # Show first few
        print("\nSample:")
        for email in unique_emails[:5]:
            print(f"  {email}")
        
        if len(unique_emails) > 5:
            print(f"  ... and {len(unique_emails) - 5} more")
    else:
        print("No valid email addresses found")


if __name__ == '__main__':
    main()
```

### Usage Examples

```powershell
# Extract from single file
python extract_emails.py document.txt

# Extract from folder, save to custom file
python extract_emails.py ./website_scrape/ contacts.txt

# Example output:
# Email Extractor
# ==================================================
# Source: ./data/ (folder)
# Scanning: page1.html
# Scanning: page2.html
# Scanning: contacts.txt
# 
# Found: 47 total, 32 unique
# Saved to: extracted_emails.txt
# 
# Sample:
#   admin@example.com
#   contact@company.com
#   info@business.org
#   ... and 29 more
```

### Enhancements

- Add phone number extraction
- Support multiple output formats (CSV, JSON)
- Group emails by domain
- Validate emails against DNS records
- Extract from PDF files using PyPDF2

---

## Script 4: Batch Image Resizer

**Problem:** Resize multiple images for web upload or email attachments.

**Solution:** Batch processing with aspect ratio preservation.

### Full Code

```python
# resize_images.py
import sys
from pathlib import Path
from PIL import Image


def resize_image(input_path, output_path, max_width=800, max_height=600, quality=85):
    """
    Resize image while maintaining aspect ratio.
    
    Args:
        input_path: Source image file
        output_path: Destination image file
        max_width: Maximum width in pixels
        max_height: Maximum height in pixels
        quality: JPEG quality (1-100)
    """
    try:
        # Open image
        with Image.open(input_path) as img:
            # Get current dimensions
            width, height = img.size
            
            # Calculate new dimensions maintaining aspect ratio
            ratio = min(max_width / width, max_height / height)
            
            # Only resize if image is larger than max dimensions
            if ratio < 1:
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                
                # Resize using high-quality resampling
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save with specified quality
                img.save(output_path, quality=quality, optimize=True)
                
                return True, f"{width}x{height} → {new_width}x{new_height}"
            else:
                # Image already small enough, just copy
                img.save(output_path, quality=quality, optimize=True)
                return True, f"{width}x{height} (unchanged)"
    
    except Exception as e:
        return False, str(e)


def resize_folder(input_folder, output_folder=None, max_width=800, max_height=600):
    """Resize all images in folder."""
    input_path = Path(input_folder)
    
    if not input_path.exists():
        print(f"Error: {input_folder} does not exist")
        return
    
    # Create output folder if not specified
    if output_folder is None:
        output_path = input_path.parent / f"{input_path.name}_resized"
    else:
        output_path = Path(output_folder)
    
    output_path.mkdir(exist_ok=True)
    
    # Supported formats
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'}
    
    success_count = 0
    error_count = 0
    
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Max size: {max_width}x{max_height}")
    print("-" * 50)
    
    # Process each image
    for file_path in input_path.iterdir():
        if file_path.suffix.lower() not in image_extensions:
            continue
        
        output_file = output_path / file_path.name
        
        success, message = resize_image(
            file_path,
            output_file,
            max_width,
            max_height
        )
        
        if success:
            print(f"✓ {file_path.name}: {message}")
            success_count += 1
        else:
            print(f"✗ {file_path.name}: {message}")
            error_count += 1
    
    print("-" * 50)
    print(f"Complete: {success_count} resized, {error_count} errors")


def main():
    """Batch image resizer."""
    print("Batch Image Resizer")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("\nUsage: python resize_images.py <folder> [width] [height] [output_folder]")
        print("\nExamples:")
        print("  python resize_images.py ./photos")
        print("  python resize_images.py ./photos 1920 1080")
        print("  python resize_images.py ./photos 800 600 ./web_images")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    max_width = int(sys.argv[2]) if len(sys.argv) > 2 else 800
    max_height = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    output_folder = sys.argv[4] if len(sys.argv) > 4 else None
    
    resize_folder(input_folder, output_folder, max_width, max_height)


if __name__ == '__main__':
    main()
```

### Installation

```powershell
# Install Pillow library
uv add pillow
```

### Usage Examples

```powershell
# Resize all images to 800x600 (default)
python resize_images.py ./vacation_photos

# Custom dimensions
python resize_images.py ./vacation_photos 1920 1080

# Custom output folder
python resize_images.py ./originals 800 600 ./web_ready

# Example output:
# Input:  vacation_photos
# Output: vacation_photos_resized
# Max size: 800x600
# --------------------------------------------------
# ✓ IMG_001.jpg: 4032x3024 → 800x600
# ✓ IMG_002.jpg: 1920x1080 → 800x450
# ✓ thumbnail.jpg: 200x200 (unchanged)
# --------------------------------------------------
# Complete: 47 resized, 0 errors
```

### Enhancements

- Add watermark overlay option
- Support format conversion (PNG to JPG)
- Add image rotation based on EXIF data
- Create thumbnail versions
- Add progress bar for large batches

---

## Script 5: Automated Backup with Rotation

**Problem:** Need regular backups of important folders with automatic old backup deletion.

**Solution:** Date-stamped backups with configurable retention.

### Full Code

```python
# auto_backup.py
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path


def create_backup(source_folder, backup_root):
    """Create timestamped backup of source folder."""
    source = Path(source_folder)
    
    if not source.exists():
        print(f"Error: {source_folder} does not exist")
        return None
    
    # Create backup root if needed
    backup_root_path = Path(backup_root)
    backup_root_path.mkdir(parents=True, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = source.name
    backup_name = f"{folder_name}_backup_{timestamp}"
    backup_path = backup_root_path / backup_name
    
    print(f"Creating backup: {backup_name}")
    
    try:
        # Copy entire directory tree
        shutil.copytree(source, backup_path)
        
        # Get size
        total_size = sum(f.stat().st_size for f in backup_path.rglob('*') if f.is_file())
        size_mb = total_size / (1024 * 1024)
        
        print(f"✓ Backup created: {size_mb:.1f} MB")
        
        return backup_path
    
    except Exception as e:
        print(f"✗ Backup failed: {e}")
        return None


def get_old_backups(backup_root, folder_name, days_to_keep=7):
    """Find backups older than specified days."""
    backup_root_path = Path(backup_root)
    
    if not backup_root_path.exists():
        return []
    
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    old_backups = []
    
    # Pattern to match: foldername_backup_YYYY-MM-DD_HH-MM-SS
    pattern = f"{folder_name}_backup_*"
    
    for backup_folder in backup_root_path.glob(pattern):
        if not backup_folder.is_dir():
            continue
        
        # Get creation time
        created = datetime.fromtimestamp(backup_folder.stat().st_ctime)
        
        if created < cutoff_date:
            old_backups.append((backup_folder, created))
    
    return old_backups


def delete_old_backups(backup_root, folder_name, days_to_keep=7, dry_run=False):
    """Delete backups older than specified days."""
    old_backups = get_old_backups(backup_root, folder_name, days_to_keep)
    
    if not old_backups:
        print(f"No backups older than {days_to_keep} days")
        return 0
    
    print(f"\nFound {len(old_backups)} old backups:")
    
    deleted = 0
    
    for backup_path, created in old_backups:
        age_days = (datetime.now() - created).days
        
        if dry_run:
            print(f"  [DRY RUN] Would delete: {backup_path.name} ({age_days} days old)")
        else:
            try:
                shutil.rmtree(backup_path)
                print(f"  ✓ Deleted: {backup_path.name} ({age_days} days old)")
                deleted += 1
            except Exception as e:
                print(f"  ✗ Error deleting {backup_path.name}: {e}")
    
    return deleted


def main():
    """Run backup with rotation."""
    print("Automated Backup Tool")
    print("=" * 50)
    
    if len(sys.argv) < 3:
        print("\nUsage: python auto_backup.py <source_folder> <backup_location> [days_to_keep]")
        print("\nExamples:")
        print("  python auto_backup.py C:/Projects D:/Backups")
        print("  python auto_backup.py C:/Documents D:/Backups 14")
        print("\nDefaults: 7 days retention")
        sys.exit(1)
    
    source_folder = sys.argv[1]
    backup_root = sys.argv[2]
    days_to_keep = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    
    print(f"Source: {source_folder}")
    print(f"Backup location: {backup_root}")
    print(f"Retention: {days_to_keep} days")
    print("-" * 50)
    
    # Create new backup
    backup_path = create_backup(source_folder, backup_root)
    
    if backup_path is None:
        sys.exit(1)
    
    # Clean up old backups
    folder_name = Path(source_folder).name
    deleted = delete_old_backups(backup_root, folder_name, days_to_keep)
    
    if deleted > 0:
        print(f"\n✓ Removed {deleted} old backups")
    
    print(f"\n✓ Backup complete: {backup_path}")


if __name__ == '__main__':
    main()
```

### Usage Examples

```powershell
# Backup with default 7-day retention
python auto_backup.py C:/Projects D:/Backups

# Custom retention period
python auto_backup.py C:/Documents D:/Backups 30

# Example output:
# Automated Backup Tool
# ==================================================
# Source: C:/Projects
# Backup location: D:/Backups
# Retention: 7 days
# --------------------------------------------------
# Creating backup: Projects_backup_2026-02-12_14-30-45
# ✓ Backup created: 245.3 MB
# 
# Found 3 old backups:
#   ✓ Deleted: Projects_backup_2026-01-31_10-15-22 (12 days old)
#   ✓ Deleted: Projects_backup_2026-01-28_09-30-10 (15 days old)
#   ✓ Deleted: Projects_backup_2026-01-23_16-45-33 (20 days old)
# 
# ✓ Removed 3 old backups
# ✓ Backup complete: D:/Backups/Projects_backup_2026-02-12_14-30-45
```

### Scheduling Backups (Windows)

Create a batch file `run_backup.bat`:

```batch
@echo off
python C:\scripts\auto_backup.py C:\Projects D:\Backups 14
```

Schedule with Task Scheduler:
1. Open Task Scheduler
2. Create Basic Task → Name it "Daily Project Backup"
3. Trigger: Daily at 6:00 PM
4. Action: Start a program → Browse to `run_backup.bat`
5. Finish

### Enhancements

- Compress backups to ZIP files
- Add email notifications on completion/failure
- Implement incremental backups (only changed files)
- Add exclusion patterns (.git, node_modules, etc.)
- Create restore script to recover from backup

---

## Deployment Tips

### Make Scripts Portable

Add shebangs for cross-platform compatibility:

```python
#!/usr/bin/env python3
# your_script.py
```

### Create Requirements File

```powershell
# Save all dependencies
uv pip freeze > requirements.txt

# On another system, install with:
uv pip install -r requirements.txt
```

### Build Executables (Optional)

Convert to standalone .exe using PyInstaller:

```powershell
uv add pyinstaller
pyinstaller --onefile script.py
```

---

## Next Steps

1. **Customize:** Modify scripts for your specific needs
2. **Combine:** Chain scripts together in larger workflows
3. **Schedule:** Set up automated execution with Task Scheduler
4. **Share:** Package scripts for colleagues using similar systems
5. **Extend:** Add logging, error handling, configuration files

---

## Additional Resources

- **pathlib documentation:** Modern file path handling
- **shutil documentation:** High-level file operations
- **argparse module:** Professional command-line interfaces
- **logging module:** Production-ready logging
- **configparser module:** Configuration file management
