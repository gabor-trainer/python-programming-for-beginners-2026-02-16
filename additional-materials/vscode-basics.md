# Visual Studio Code basics

**Purpose:** Introduction to VS Code interface, navigation, and extension ecosystem for beginners  
**Time:** 20-30 minutes  
**Prerequisite:** VS Code installed on lab machine

---

## What is Visual Studio Code?

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft. It is lightweight, fast, and highly extensible through extensions. VS Code supports virtually every programming language through its extension marketplace and has become one of the most popular development tools worldwide.

**Key characteristics:**
- **Free and open source** — Available on Windows, macOS, and Linux
- **Lightweight but powerful** — Fast startup, low resource usage
- **Extensible** — Thousands of extensions for languages, themes, tools
- **Built-in Git integration** — Version control without leaving the editor
- **IntelliSense** — Smart code completion and suggestions
- **Integrated terminal** — Run commands without switching windows

---

## The VS Code interface

### Activity Bar (left edge)

The vertical bar on the left provides access to main views:

| Icon | View | Purpose |
|------|------|---------|
| Files | Explorer | Browse project files and folders |
| Search | Search | Find and replace across files |
| Source Control | Git | Commit, push, pull changes |
| Run and Debug | Debugger | Run and debug programs |
| Extensions | Marketplace | Install and manage extensions |

**Navigation:**
- Click icons to switch between views
- `Ctrl+B` toggles the entire sidebar visibility

### Side Bar

Shows the content of the selected Activity Bar view:
- **Explorer:** Tree view of folders and files
- **Search:** Search results with preview
- **Source Control:** Git changes and commit interface
- **Extensions:** Browse and install extensions

### Editor Area (center)

The main coding area where you edit files:
- **Tabs:** Each open file appears as a tab
- **Split editors:** Drag a tab to the side to view files side-by-side
- **Breadcrumbs:** Shows file path and current symbol location (top of editor)

**Keyboard shortcuts:**
- `Ctrl+W` — Close current tab
- `Ctrl+Tab` — Switch between open tabs
- `Ctrl+\` — Split editor vertically
- `Ctrl+1`, `Ctrl+2` — Focus on editor group 1, 2

### Status Bar (bottom)

Shows current file information:
- Line and column number
- File encoding
- Line ending type (CRLF / LF)
- Language mode (e.g., Python)
- Git branch name
- Problems/errors/warnings count

**Click status bar items to change settings** (e.g., click "CRLF" to switch to "LF")

### Panel (bottom, togglable)

Contains various tools:
- **Terminal:** Integrated command line
- **Problems:** Errors and warnings
- **Output:** Extension and tool output
- **Debug Console:** Debugging information

**Keyboard shortcuts:**
- `` Ctrl+` `` — Toggle terminal
- `Ctrl+Shift+M` — Toggle Problems panel
- `Ctrl+J` — Toggle entire panel

---

## Essential keyboard shortcuts

### File operations
| Shortcut | Action |
|----------|--------|
| `Ctrl+N` | New file |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+Shift+S` | Save as |
| `Ctrl+K, Ctrl+O` | Open folder |
| `Ctrl+W` | Close tab |
| `Ctrl+Shift+T` | Reopen closed tab |

### Editing
| Shortcut | Action |
|----------|--------|
| `Ctrl+X` | Cut line (if no selection) |
| `Ctrl+C` | Copy line (if no selection) |
| `Ctrl+V` | Paste |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Ctrl+/` | Toggle line comment |
| `Alt+Up/Down` | Move line up/down |
| `Shift+Alt+Up/Down` | Copy line up/down |
| `Ctrl+D` | Select next occurrence |
| `Ctrl+Shift+L` | Select all occurrences |

### Navigation
| Shortcut | Action |
|----------|--------|
| `Ctrl+P` | Quick Open (go to file) |
| `Ctrl+Shift+O` | Go to symbol in file |
| `Ctrl+G` | Go to line number |
| `Ctrl+Shift+F` | Search across files |
| `F12` | Go to definition |
| `Alt+Left/Right` | Navigate back/forward |

### View
| Shortcut | Action |
|----------|--------|
| `Ctrl+B` | Toggle sidebar |
| `Ctrl+J` | Toggle panel |
| `` Ctrl+` `` | Toggle terminal |
| `Ctrl+\` | Split editor |
| `Ctrl+=` / `Ctrl+-` | Zoom in/out |

---

## The Extension ecosystem

Extensions add functionality to VS Code. They provide language support, themes, debuggers, linters, formatters, and productivity tools.

### Accessing extensions

1. Click the **Extensions** icon in the Activity Bar (or `Ctrl+Shift+X`)
2. Search for extensions by name or functionality
3. Click **Install** to add an extension
4. Some extensions require a reload to activate

### Extension categories

**Language Support:**
- Syntax highlighting
- IntelliSense (code completion)
- Debugging support
- Linting and formatting

**Productivity Tools:**
- GitLens — Enhanced Git features
- Live Share — Real-time collaboration
- Todo Tree — Highlight TODO comments
- Bracket Pair Colorizer — Match brackets with colors

**Themes:**
- Color themes (editor appearance)
- Icon themes (file/folder icons)

**Formatters and Linters:**
- Prettier — Multi-language formatter
- ESLint — JavaScript linter
- Black, Ruff — Python formatters/linters

**Remote Development:**
- Remote - SSH — Edit files on remote machines
- Dev Containers — Develop inside Docker containers

### Managing extensions

**View installed extensions:**
- Extensions view → "Installed" filter

**Enable/disable extensions:**
- Click gear icon next to extension → Enable/Disable

**Uninstall extensions:**
- Click gear icon → Uninstall

**Extension settings:**
- Click gear icon → Extension Settings
- Or go to Settings (`Ctrl+,`) and search for extension name

---

## Settings and customization

### Opening settings

- **GUI:** `Ctrl+,` or File → Preferences → Settings
- **JSON:** `Ctrl+Shift+P` → "Preferences: Open Settings (JSON)"

### Settings levels

1. **User Settings** — Apply globally to all projects
2. **Workspace Settings** — Apply only to the current project folder
3. **Folder Settings** — Apply to a specific folder in a multi-root workspace

**Workspace settings override user settings.**

### Common settings to customize

**Editor appearance:**
```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "Consolas, 'Courier New', monospace",
  "editor.lineHeight": 22,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.wordWrap": "on"
}
```

**Files:**
```json
{
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "files.exclude": {
    "**/.git": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

**Terminal:**
```json
{
  "terminal.integrated.fontSize": 12,
  "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe"
}
```

---

## Command Palette

The Command Palette provides access to all VS Code commands.

**Open:** `Ctrl+Shift+P` (or `F1`)

**Usage:**
- Type to search for commands
- Execute commands without navigating menus
- Access extension-specific commands

**Common commands:**
- "Format Document" — Format the entire file
- "Change Language Mode" — Set syntax highlighting
- "Transform to Uppercase/Lowercase" — Change text case
- "Sort Lines Ascending" — Sort selected lines
- "Developer: Reload Window" — Restart VS Code

---

## Integrated Terminal

VS Code includes a built-in terminal so you can run commands without leaving the editor.

**Open terminal:** `` Ctrl+` ``

**Features:**
- Multiple terminals (click `+` to add)
- Split terminals (click split icon)
- Switch between terminals (dropdown menu)
- Choose shell type (PowerShell, cmd, Git Bash, etc.)

**Right-click in terminal:**
- Copy/Paste
- Clear terminal
- Kill terminal

---

## Working with files and folders

### Opening a project

**Option 1: Open Folder**
- File → Open Folder → Select project directory
- Best practice for any project work

**Option 2: Quick Open**
- `Ctrl+P` → Type filename → Open

**Option 3: From Terminal**
```cmd
cd C:\path\to\project
code .
```

### File Explorer tips

**Create files/folders:**
- Right-click in Explorer → New File / New Folder
- Or click the icons at top of Explorer

**Search in Explorer:**
- Click search icon or `Ctrl+Shift+F`
- Search across all files in the project

**Copy file path:**
- Right-click file → Copy Path (full path)
- Right-click file → Copy Relative Path (from workspace root)

---

## Multi-cursor editing

Edit multiple locations simultaneously.

**Add cursors:**
- `Alt+Click` — Add cursor at click position
- `Ctrl+Alt+Up/Down` — Add cursor above/below
- `Ctrl+D` — Select next occurrence of current word
- `Ctrl+Shift+L` — Select all occurrences

**Example use case:**
1. Select a variable name
2. Press `Ctrl+D` repeatedly to select more occurrences
3. Type to replace all at once

---

## Search and replace

### Quick search
- `Ctrl+F` — Find in current file
- `Ctrl+H` — Find and replace in current file

### Search across files
- `Ctrl+Shift+F` — Search in all files
- `Ctrl+Shift+H` — Find and replace in all files

**Search options:**
- Match case (`Alt+C`)
- Match whole word (`Alt+W`)
- Use regular expression (`Alt+R`)

**Filters:**
- **files to include:** `*.py` (only Python files)
- **files to exclude:** `**/node_modules/**` (ignore folders)

---

## Themes and appearance

### Change color theme
1. `Ctrl+K, Ctrl+T` (or `Ctrl+Shift+P` → "Color Theme")
2. Use arrow keys to preview themes
3. Press Enter to select

**Popular themes:**
- Dark+ (VS Code default dark)
- Light+ (VS Code default light)
- Monokai
- Dracula Official
- One Dark Pro

### Change icon theme
1. `Ctrl+Shift+P` → "File Icon Theme"
2. Select theme

**Popular icon themes:**
- Material Icon Theme
- VS Code Icons

---

## IntelliSense (code completion)

IntelliSense provides smart completions based on:
- Variable types
- Function definitions
- Imported modules

**Usage:**
- Type to trigger suggestions automatically
- `Ctrl+Space` to manually trigger
- Arrow keys to navigate
- `Enter` or `Tab` to accept

**Features:**
- Method signatures and parameter hints
- Quick info on hover
- Auto-import suggestions

---

## Tips for beginners

1. **Learn shortcuts gradually** — Start with `Ctrl+P`, `Ctrl+Shift+P`, and `` Ctrl+` ``
2. **Use Quick Open (`Ctrl+P`)** — Fastest way to open files
3. **Install extensions as needed** — Don't over-install; add when you need functionality
4. **Enable auto-save** — File → Auto Save (or settings: `"files.autoSave": "afterDelay"`)
5. **Use the integrated terminal** — Stay in one window instead of switching
6. **Explore Command Palette** — `Ctrl+Shift+P` is your friend
7. **Split editor for reference** — View two files side-by-side while coding
8. **Read extension READMEs** — Extensions often add commands and shortcuts

---

## Next steps

- **Python setup:** See [Python VS Code setup](python-vscode-setup.md) for Python-specific configuration
- **Environment setup:** See [Python environment setup](python-environment-setup.md) for installing Python, uv, and ruff
- **VS Code documentation:** https://code.visualstudio.com/docs
- **Keyboard shortcut reference:** `Ctrl+K, Ctrl+R` opens the online reference
