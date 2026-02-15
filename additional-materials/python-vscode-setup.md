# Setting up VS Code for Python development

**Purpose:** Configure VS Code with Python extensions, settings, and best practices  
**Time:** 15-20 minutes  
**Prerequisites:** 
- VS Code installed
- Python 3.12+ installed (see [Python environment setup](python-environment-setup.md))
- Basic familiarity with VS Code (see [VS Code basics](vscode-basics.md))

---

## Essential Python extensions

### 1. Python (by Microsoft)

**Extension ID:** `ms-python.python`

The official Python extension provides:
- IntelliSense (code completion, parameter info)
- Linting (error detection)
- Debugging
- Code formatting
- Jupyter Notebook support
- Test discovery and execution
- Python environment management

**Installation:**
1. Open Extensions view (`Ctrl+Shift+X`)
2. Search for "Python"
3. Click **Install** on "Python" by Microsoft

**After installation:**
- VS Code will prompt to select a Python interpreter
- Click "Select Python Interpreter" in the bottom-left status bar
- Choose your installed Python version (e.g., Python 3.12.x)

---

### 2. Pylance

**Extension ID:** `ms-python.vscode-pylance`

Pylance is a fast, feature-rich language server for Python:
- **Type checking** — Identifies type errors before runtime
- **Auto-imports** — Suggests and auto-adds import statements
- **Smart completions** — Context-aware IntelliSense
- **Signature help** — Shows function parameters as you type

**Installation:**
- Usually installed automatically with the Python extension
- If not: Search "Pylance" in Extensions and install

**Configuration:**
```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic"
}
```

**Type checking modes:**
- `"off"` — No type checking
- `"basic"` — Good for beginners (default)
- `"strict"` — Enforce full type annotations

---

### 3. Ruff

**Extension ID:** `charliermarsh.ruff`

Ruff is an extremely fast Python linter and formatter written in Rust:
- **Linting** — Catches errors, style issues, complexity
- **Formatting** — Auto-formats code to follow PEP 8
- **Speed** — 10-100x faster than traditional tools

**Installation:**
1. Search "Ruff" in Extensions
2. Install "Ruff" by charliermarsh

**Ruff must be installed in your environment** (see [Python environment setup](python-environment-setup.md))

**Configuration:**
```json
{
  "ruff.enable": true,
  "ruff.organizeImports": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  }
}
```

---

### 4. Python Indent (optional but helpful)

**Extension ID:** `KevinRose.vsc-python-indent`

Automatically corrects Python indentation as you type:
- Detects when to indent/dedent after colons
- Useful for beginners learning Python's significant whitespace

**Installation:**
- Search "Python Indent" and install

---

### 5. autoDocstring (optional)

**Extension ID:** `njpwerner.autodocstring`

Generates Python docstring templates:
- Type `"""` and press Enter
- Automatically creates docstring skeleton based on function signature

**Installation:**
- Search "autoDocstring" and install

**Configuration:**
```json
{
  "autoDocstring.docstringFormat": "google"
}
```

Formats: `google`, `numpy`, `sphinx`, `pep257`

---

## Recommended VS Code settings for Python

Open settings (`Ctrl+,`) or settings JSON (`Ctrl+Shift+P` → "Preferences: Open Settings (JSON)") and add:

```json
{
  // Python interpreter
  "python.defaultInterpreterPath": "python",
  
  // Linting and formatting
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "none",
  
  // Editor behavior for Python
  "[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.formatOnType": false,
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    },
    "editor.rulers": [88, 120]
  },
  
  // IntelliSense
  "python.autoComplete.addBrackets": true,
  "python.analysis.autoImportCompletions": true,
  "python.analysis.typeCheckingMode": "basic",
  
  // Terminal
  "python.terminal.activateEnvironment": true,
  
  // Testing
  "python.testing.pytestEnabled": false,
  "python.testing.unittestEnabled": false,
  
  // File associations
  "files.associations": {
    "*.py": "python"
  },
  
  // Files to exclude from Explorer
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.ruff_cache": true,
    "**/.mypy_cache": true,
    "**/*.egg-info": true
  },
  
  // Auto-save
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  
  // Trim trailing whitespace
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true
}
```

---

## Selecting a Python interpreter

VS Code needs to know which Python installation to use.

### View current interpreter

Look at the **bottom-left corner** of the status bar — it shows the active interpreter (e.g., "Python 3.12.1").

### Change interpreter

**Method 1: Status bar**
1. Click the Python version in the bottom-left status bar
2. Select from the list of detected interpreters

**Method 2: Command Palette**
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Choose interpreter

### Interpreter options

- **Global Python:** `C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe`
- **Virtual environment:** `.venv\Scripts\python.exe`
- **uv-managed environment:** Auto-detected when using uv

**Best practice:** Use a virtual environment or uv project per project (keeps dependencies isolated).

---

## Using the integrated terminal with Python

### Activate terminal
`` Ctrl+` `` to toggle terminal

### Run Python scripts
```cmd
python script.py
```

### Run with uv (in a uv project)
```cmd
uv run script.py
```

### Interactive REPL
```cmd
python
>>> print("Hello, Python!")
>>> exit()
```

### Change terminal shell (optional)

To use PowerShell instead of cmd:
1. `Ctrl+Shift+P` → "Terminal: Select Default Profile"
2. Choose "PowerShell" or "Command Prompt"

---

## Code formatting and linting

### Format document
- **Shortcut:** `Shift+Alt+F`
- **Command Palette:** `Ctrl+Shift+P` → "Format Document"
- **Auto-format on save:** Enabled in recommended settings above

### Format selection
- Select code
- Right-click → "Format Selection"
- Or `Ctrl+K, Ctrl+F`

### Linting (error detection)

With Ruff installed and enabled:
- Errors and warnings appear as **squiggly underlines**
- Hover to see the issue
- Click the lightbulb icon or press `Ctrl+.` for quick fixes

**View all problems:**
- `Ctrl+Shift+M` opens the Problems panel
- Shows all errors and warnings in the project

---

## IntelliSense and code completion

### Trigger IntelliSense
- **Automatic:** Start typing, suggestions appear
- **Manual:** `Ctrl+Space`

### Accept suggestions
- `Enter` or `Tab` to accept
- `Esc` to dismiss

### Navigate suggestions
- Arrow keys to move up/down
- `Ctrl+Space` again to see more options

### Parameter hints
- Type `(` after a function name to see parameters
- `Ctrl+Shift+Space` to manually trigger parameter hints

### Quick info
- **Hover** over any symbol to see documentation
- `Ctrl+K, Ctrl+I` to trigger hover info

---

## Debugging Python in VS Code

### Simple debugging
1. Open a Python file
2. Press `F5` (or Run → Start Debugging)
3. Select "Python File" when prompted
4. Code executes with debugger attached

### Set breakpoints
- Click in the left margin (gutter) next to line numbers
- Red dot appears
- Code pauses at breakpoint when debugging

### Debug controls (when paused)
- **F5** — Continue
- **F10** — Step over (execute current line)
- **F11** — Step into (enter function)
- **Shift+F11** — Step out (exit function)
- **Ctrl+Shift+F5** — Restart
- **Shift+F5** — Stop

### View variables
- **Variables pane** shows local and global variables
- **Watch pane** lets you monitor specific expressions
- **Hover** over variables in code to see values

### Debug Console
- Evaluate expressions while paused
- Type Python code to inspect state

---

## Working with Python projects

### Project structure example
```
my_project/
├── .venv/               # Virtual environment (if using venv)
├── .vscode/
│   └── settings.json    # Workspace-specific settings
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml       # Project config (uv)
├── requirements.txt     # Dependencies (pip)
└── README.md
```

### Open a project folder
1. File → Open Folder
2. Select project root directory
3. VS Code opens the entire folder

**Benefits:**
- IntelliSense knows about all project files
- Search/replace works across the project
- Git integration works at project level

---

## Running Python code

### Option 1: Run in terminal
1. Open file in editor
2. `` Ctrl+` `` to open terminal
3. Type `python filename.py` and press Enter

### Option 2: Run button (top-right)
- Click the **▶ Run Python File** button in the top-right corner
- Runs file in integrated terminal

### Option 3: Run selected code
1. Select lines of code
2. Right-click → "Run Selection/Line in Python Terminal"
3. Or `Shift+Enter`

**This sends code to the interactive REPL** — great for experimenting!

---

## Code navigation

### Go to definition
- `F12` — Jump to where a function/class is defined
- `Ctrl+Click` — Same as F12

### Peek definition
- `Alt+F12` — View definition in a popup without leaving current file

### Go to symbol
- `Ctrl+Shift+O` — List all functions/classes in current file
- Type to filter, Enter to jump

### Find all references
- `Shift+F12` — Show all places where a symbol is used

### Go back/forward
- `Alt+Left` — Go back to previous location
- `Alt+Right` — Go forward

---

## Code snippets

VS Code includes Python snippets that expand into code templates.

### Common snippets

| Type | Press Tab | Expands to |
|------|-----------|------------|
| `for` | Tab | `for item in iterable:` |
| `def` | Tab | Function definition template |
| `class` | Tab | Class definition template |
| `if` | Tab | `if condition:` |
| `try` | Tab | Try/except block |

**Usage:**
1. Type snippet prefix (e.g., `for`)
2. Press `Tab`
3. Template expands, cursor positioned at first input
4. Tab to move between placeholders

---

## Workspace settings vs. user settings

### User settings
- Apply to **all** VS Code projects
- Stored in: `%APPDATA%\Code\User\settings.json`

### Workspace settings
- Apply **only to the current project**
- Stored in: `.vscode/settings.json` in project folder

**Example workspace settings:**
```json
{
  "python.defaultInterpreterPath": ".venv/Scripts/python.exe",
  "python.analysis.extraPaths": ["./src"]
}
```

**When to use workspace settings:**
- Project-specific interpreter paths
- Custom linting rules for this project
- Team-shared settings (commit `.vscode/settings.json` to Git)

---

## Recommended workflow for beginners

1. **Open project folder** — Always work in a folder, not individual files
2. **Select interpreter** — Ensure correct Python version is active
3. **Enable auto-save** — Settings → `"files.autoSave": "afterDelay"`
4. **Enable format on save** — Settings → `"editor.formatOnSave": true`
5. **Use the terminal** — `` Ctrl+` `` to run code without leaving VS Code
6. **Leverage IntelliSense** — Let VS Code suggest completions
7. **Check the Problems panel** — `Ctrl+Shift+M` to see linting errors
8. **Debug instead of print** — Set breakpoints and use F5 to understand code flow

---

## Troubleshooting

### "Python is not recognized" in terminal

**Cause:** Python not in PATH

**Solution:**
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to PATH (see [Python environment setup](python-environment-setup.md))
3. Restart VS Code

### IntelliSense not working

**Cause:** Interpreter not selected or Pylance not installed

**Solution:**
1. Click Python version in status bar and select interpreter
2. Ensure Pylance extension is installed
3. Reload window: `Ctrl+Shift+P` → "Developer: Reload Window"

### Linting not working

**Cause:** Ruff not installed or not enabled

**Solution:**
1. Install ruff: `pip install ruff` or `uv add --dev ruff`
2. Enable in settings: `"ruff.enable": true`
3. Check extension is installed: Ruff by charliermarsh

### Format on save not working

**Solution:**
1. Check settings: `"editor.formatOnSave": true`
2. Check `"[python]"` section has `"editor.defaultFormatter": "charliermarsh.ruff"`
3. Ensure Ruff is installed in the active Python environment

---

## Next steps

- **Python environment setup:** See [Python environment setup](python-environment-setup.md) for installing Python, uv, and ruff
- **VS Code Python tutorial:** https://code.visualstudio.com/docs/python/python-tutorial
- **Pylance documentation:** https://github.com/microsoft/pylance-release
- **Ruff documentation:** https://docs.astral.sh/ruff/
