# Python environment setup guide

**Purpose:** Install Python 3.12+, uv, and ruff on Windows lab machines  
**Time:** 15-20 minutes  
**Target:** ALEF training lab environment (Windows)

---

## Overview

This guide covers installing:
1. **Python 3.12+** — The Python interpreter
2. **uv** — Fast Python package and project manager
3. **ruff** — Fast Python linter and formatter

**Why these tools?**

| Tool | Purpose | Why use it |
|------|---------|------------|
| Python | Run Python code | Required for all Python development |
| uv | Manage projects and packages | 10-100x faster than pip, modern dependency management |
| ruff | Lint and format code | Extremely fast, catches errors, enforces PEP 8 |

---

## Part 1: Installing Python 3.12+

### Step 1: Download Python

1. Go to https://www.python.org/downloads/
2. Click **"Download Python 3.12.x"** (latest 3.12 version)
3. Save the installer (e.g., `python-3.12.1-amd64.exe`)

**Note:** Python 3.12+ is required for this course. Do not install Python 3.11 or earlier.

### Step 2: Run the installer

1. **Double-click** the downloaded installer
2. **IMPORTANT: Check "Add python.exe to PATH"** (at the bottom)
3. Click **"Install Now"** (recommended for beginners)
   - Installs Python to `%APPDATA%\Local\Programs\Python\Python312`
   - Includes pip, IDLE, and documentation

**Alternative (Custom Installation):**
- Click "Customize installation" if you want to:
  - Install to a specific directory
  - Choose optional features
  - Install for all users

4. Wait for installation to complete
5. Click **"Close"** when done

### Step 3: Verify installation

1. Open a **new** Command Prompt window (not an old one)
   - Press `Win+R`, type `cmd`, press Enter
   
2. Check Python version:
   ```cmd
   python --version
   ```
   **Expected output:** `Python 3.12.x`

3. Check pip version:
   ```cmd
   pip --version
   ```
   **Expected output:** `pip 23.x.x from ...`

**Troubleshooting:**

| Issue | Solution |
|-------|----------|
| `'python' is not recognized` | PATH not set. Reinstall with "Add to PATH" checked, or add manually (see below) |
| Shows Python 3.11 or older | Multiple Python versions installed. Uninstall old versions or use `py -3.12` |
| Command Prompt was already open | Close and reopen Command Prompt to reload PATH |

### Step 4: Add Python to PATH manually (if needed)

If you forgot to check "Add to PATH" during installation:

1. Find Python installation path:
   ```cmd
   where python
   ```
   Or typically: `C:\Users\YourName\AppData\Local\Programs\Python\Python312`

2. Open Environment Variables:
   - Press `Win+R`, type `sysdm.cpl`, press Enter
   - Click **"Advanced"** tab
   - Click **"Environment Variables"**

3. Edit PATH:
   - Under "User variables", select **Path** and click **Edit**
   - Click **New** and add:
     - `C:\Users\YourName\AppData\Local\Programs\Python\Python312`
     - `C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts`
   - Click **OK** on all dialogs

4. **Restart Command Prompt** and verify again

---

## Part 2: Installing uv

### What is uv?

uv is a fast Python package and project manager developed by Astral (creators of Ruff). It replaces pip, venv, and virtualenv with a single, extremely fast tool.

**Key features:**
- **10-100x faster** than pip for package installation
- **Project management** with `pyproject.toml`
- **Dependency resolution** that actually works
- **Lockfiles** for reproducible environments
- **Cross-platform** and written in Rust for speed

### Step 1: Install uv (recommended method)

**Using the official installer (Windows):**

```cmd
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

This downloads and installs uv to `%USERPROFILE%\.cargo\bin\uv.exe`

**Alternative: Install with pip (if installer fails):**

```cmd
pip install uv
```

### Step 2: Verify installation

```cmd
uv --version
```

**Expected output:** `uv 0.x.x`

**Troubleshooting:**

| Issue | Solution |
|-------|----------|
| `'uv' is not recognized` | PATH not set. Close/reopen terminal, or add `%USERPROFILE%\.cargo\bin` to PATH |
| pip install fails | Try the official installer method above |

### Step 3: Test uv

Create a test project:

```cmd
cd C:\temp
uv init hello-uv
cd hello-uv
uv run python hello.py
```

**Expected output:** `Hello from hello-uv!`

**What happened:**
- `uv init hello-uv` — Created a project directory with `pyproject.toml` and `hello.py`
- `uv run python hello.py` — Ran the script with uv's managed Python environment

---

## Part 3: Installing ruff

### What is ruff?

Ruff is an extremely fast Python linter and code formatter, written in Rust. It replaces multiple tools (flake8, black, isort, pylint) with one fast tool.

**Key features:**
- **10-100x faster** than existing Python linters
- **All-in-one:** linting + formatting + import sorting
- **Compatible** with PEP 8, flake8 rules
- **IDE integration** for VS Code, PyCharm, Sublime

### Step 1: Install ruff with uv (recommended)

If you're working in a uv project:

```cmd
cd your-project-folder
uv add --dev ruff
```

This adds ruff as a development dependency in `pyproject.toml`.

### Step 2: Install ruff globally with pip (alternative)

If you want ruff available everywhere:

```cmd
pip install ruff
```

### Step 3: Verify installation

```cmd
ruff --version
```

**Expected output:** `ruff 0.x.x`

### Step 4: Test ruff

Create a test Python file with issues:

```cmd
cd C:\temp
echo. > test.py
```

Edit `test.py` to contain:

```python
import os
import sys
def hello(  x):
 print( 'hello' )
```

**Run ruff linter:**
```cmd
ruff check test.py
```

**Output:** Shows linting errors (unused imports, formatting issues)

**Run ruff formatter:**
```cmd
ruff format test.py
```

**Output:** `1 file reformatted`

**View the formatted file:**
```cmd
type test.py
```

**Output (cleaned up):**
```python
def hello(x):
    print("hello")
```

**Notice:**
- Unused imports removed
- Spacing fixed
- Single quotes → double quotes (Ruff default)
- Proper indentation (4 spaces)

---

## Part 4: Setting up your first project with uv

### Create a new project

```cmd
cd C:\labs
uv init my-first-project
cd my-first-project
```

**Files created:**
- `pyproject.toml` — Project configuration
- `hello.py` — Sample script
- `.python-version` — Python version pinning

### Add dependencies

```cmd
uv add requests
```

This:
- Installs `requests` library
- Adds it to `pyproject.toml`
- Creates/updates `uv.lock` (lockfile)

### Add development dependencies

```cmd
uv add --dev ruff pytest
```

This adds tools you use during development (not needed in production).

### View pyproject.toml

```cmd
type pyproject.toml
```

**Content:**
```toml
[project]
name = "my-first-project"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
]
```

### Run scripts

```cmd
uv run python hello.py
```

Or create a script alias in `pyproject.toml`:

```toml
[project.scripts]
hello = "hello:main"
```

Then run:
```cmd
uv run hello
```

---

## Part 5: Configuring ruff in your project

### Create ruff config in pyproject.toml

Edit `pyproject.toml` and add:

```toml
[tool.ruff]
# Set line length to 88 (Black default)
line-length = 88

# Target Python 3.12+
target-version = "py312"

[tool.ruff.lint]
# Enable rules
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (import sorting)
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
]

# Ignore specific rules
ignore = [
    "E501",  # Line too long (let formatter handle it)
]

[tool.ruff.format]
# Use double quotes for strings
quote-style = "double"

# Indent with spaces
indent-style = "space"
```

### Run ruff on your project

**Check for issues:**
```cmd
uv run ruff check .
```

**Auto-fix issues:**
```cmd
uv run ruff check --fix .
```

**Format all files:**
```cmd
uv run ruff format .
```

---

## Part 6: Python environment types (background)

### Global Python
- Installed system-wide
- Packages installed here affect all projects
- **Not recommended** for project work (causes conflicts)

### Virtual environments (venv)
- Isolated Python environment per project
- Created with `python -m venv .venv`
- Activate: `.venv\Scripts\activate`
- **Traditional approach** (still common)

### uv-managed environments
- Automatically created by uv per project
- No manual activation needed
- Faster than venv
- **Modern approach** (recommended for this course)

**Comparison:**

| Task | venv | uv |
|------|------|-----|
| Create environment | `python -m venv .venv` | Automatic with `uv init` |
| Activate | `.venv\Scripts\activate` | Not needed |
| Install package | `pip install requests` | `uv add requests` |
| Run script | `python script.py` | `uv run python script.py` |
| Speed | Normal | 10-100x faster |

---

## Verification checklist

Before starting the training, verify:

- [ ] `python --version` shows Python 3.12.x or higher
- [ ] `pip --version` shows pip is installed
- [ ] `uv --version` shows uv is installed
- [ ] `ruff --version` shows ruff is installed
- [ ] Can create a uv project: `uv init test-project`
- [ ] Can add a package: `cd test-project && uv add requests`
- [ ] Can run ruff: `uv run ruff check .`
- [ ] Can run a script: `uv run python hello.py`

**If all checks pass, your environment is ready for the training!**

---

## Common issues and solutions

### Issue: Multiple Python versions installed

**Problem:** `python --version` shows an old version

**Solution:**
1. Use `py -3.12` instead of `python` to target Python 3.12
2. Or uninstall old Python versions:
   - Settings → Apps → Python → Uninstall
3. Reinstall Python 3.12 and ensure PATH is set

### Issue: pip installs to wrong Python version

**Problem:** `pip install` installs to Python 3.11 instead of 3.12

**Solution:**
Use explicit version:
```cmd
py -3.12 -m pip install package-name
```

Or use uv exclusively (recommended).

### Issue: uv not found after installation

**Problem:** `'uv' is not recognized`

**Solution:**
1. Close and reopen Command Prompt
2. If still not found, add to PATH manually:
   - Add `%USERPROFILE%\.cargo\bin` to PATH
   - Restart terminal

### Issue: Permission denied during installation

**Problem:** "Access is denied" error

**Solution:**
- Run installer as Administrator (right-click → Run as administrator)
- Or install to user directory (default)

---

## Next steps

- **VS Code setup:** See [Python VS Code setup](python-vscode-setup.md) to configure VS Code for Python development
- **VS Code basics:** See [VS Code basics](vscode-basics.md) to learn the editor
- **Official documentation:**
  - Python: https://docs.python.org/3.12/
  - uv: https://docs.astral.sh/uv/
  - ruff: https://docs.astral.sh/ruff/
