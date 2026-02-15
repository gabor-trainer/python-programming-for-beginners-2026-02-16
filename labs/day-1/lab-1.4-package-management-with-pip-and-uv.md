# Lab 1.4: Package management with pip and uv

**Estimated time**: 45 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Command line, VS Code

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Install a Python package using pip and understand the traditional workflow
- Initialize a Python project using `uv init`
- Add dependencies to a project using `uv add`
- Run scripts inside a uv-managed project using `uv run`
- Read and understand the `pyproject.toml` file

---

## 3. Prerequisites

**Knowledge prerequisites**: Variables, strings, basic script writing (Chapters 1.1-1.3).

**Previous labs**: Lab 1.3 completed.

**Environment confirmation**:
- [ ] Python 3.12+ installed and on PATH
- [ ] pip available (`pip --version`)
- [ ] uv installed and on PATH (`uv --version`)
- [ ] Working directory `C:\labs` exists

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal and run `python --version` (expect 3.12+)
- [ ] Run `pip --version` (expect a version line)
- [ ] Run `uv --version` (expect a version line)
- [ ] Navigate to your working directory: `cd C:\labs`

If `uv --version` fails, ask your instructor to verify the uv installation.

---

## 5. Concept overview

Python's standard library covers many common tasks, but thousands of additional packages extend Python into specialized domains — web scraping, data analysis, HTTP requests, image processing, and more. To use these packages, you need a **package manager** that handles downloading, installing, and tracking dependencies.

In this lab, you will use two package managers. First, **pip** — the traditional tool that has been Python's default for over a decade. You will install a package with pip to understand the basic workflow. Then you will switch to **uv** — a modern tool that is significantly faster and integrates project management directly. uv creates projects with a `pyproject.toml` file that declares dependencies explicitly, making your projects reproducible and shareable.

After this lab, you will use uv exclusively for all future package management.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Install a package with pip and understand its limitations
- Create a project with uv and manage dependencies declaratively
- Run scripts inside a uv-managed environment
- Compare the two workflows and understand why uv is preferred

---

### Exercise 1.4.1: Install a package with pip

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Command line  
**Objective**: Understand the traditional pip workflow — install, use, and uninstall a package.

**Scenario**: You need to generate a random fake name for testing purposes. The `Faker` package does this, but it is not part of the standard library. You need to install it.

**Tasks**:

1. Open a command prompt and navigate to your labs folder:

```
C:\> cd C:\labs
```

2. List currently installed packages:

```
C:\labs> pip list
```

You will see a list of packages. Note that `Faker` is not present.

3. Install the `Faker` package with pip:

```
C:\labs> pip install Faker
```

pip downloads and installs Faker along with its dependencies. You will see progress messages and a "Successfully installed" line.

4. Verify the installation:

```
C:\labs> pip list
```

`Faker` should now appear in the list, along with any dependencies it pulled in.

5. Test it in the REPL:

```
C:\labs> python
```

```python
>>> from faker import Faker
>>> fake = Faker()
>>> print(fake.name())
>>> print(fake.address())
>>> print(fake.email())
>>> exit()
```

Each call generates a random fake value. The exact output differs each time.

6. Uninstall Faker:

```
C:\labs> pip uninstall Faker -y
```

The `-y` flag confirms the uninstall without prompting.

**Verification**: Faker installed successfully, generated fake data in the REPL, and was uninstalled cleanly.

**Expected output**: `pip install` shows download progress and a success message. The REPL produces three lines of fake data (a name, an address, and an email). `pip uninstall` confirms removal.

**What to notice**: pip works, but there is no record of what you installed. If you share this project with a colleague, they would not know that Faker was needed. This is the key limitation pip solves only partially (through manually created requirements.txt files).

---

### Exercise 1.4.2: Initialize a project with uv

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Command line  
**Objective**: Create a new Python project with uv and understand the generated structure.

**Scenario**: You are starting a new project that will process data. Instead of installing packages globally, you create a proper project structure with uv.

**Tasks**:

1. Navigate to your labs folder:

```
C:\labs> cd C:\labs
```

2. Initialize a new project:

```
C:\labs> uv init data-processor
```

uv creates a new directory with project files.

3. Navigate into the project:

```
C:\labs> cd data-processor
```

4. List the contents:

```
C:\labs\data-processor> dir
```

You should see files including `pyproject.toml`, `README.md`, and `hello.py` (or `main.py` depending on uv version).

5. Open `pyproject.toml` in Notepad to examine it:

```
C:\labs\data-processor> notepad pyproject.toml
```

You should see something like:

```toml
[project]
name = "data-processor"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

Notice `dependencies = []` — the list is empty because you have not added any packages yet. Close Notepad.

6. Run the default script to verify the project works:

```
C:\labs\data-processor> uv run hello.py
```

You should see `Hello from data-processor!` (or similar default output).

**Verification**: The project directory exists and contains `pyproject.toml`. The default script runs successfully with `uv run`.

**Expected output**: `dir` shows at least `pyproject.toml`, a README file, and a Python script. The `uv run` command produces the default greeting output.

---

### Exercise 1.4.3: Add dependencies and build a script

**Time**: 15 minutes  
**Difficulty**: Intermediate  
**Tool**: Command line, VS Code  
**Objective**: Add packages with `uv add`, write a script that uses them, and run it with `uv run`.

**Scenario**: You want to build a script that generates fake employee data and formats it nicely. You need the `Faker` package.

**Tasks**:

1. Make sure you are in the project directory:

```
C:\labs\data-processor>
```

2. Add the Faker package with uv:

```
C:\labs\data-processor> uv add Faker
```

uv downloads and installs Faker, and updates `pyproject.toml` automatically.

3. Verify the dependency was added. Open `pyproject.toml`:

```
C:\labs\data-processor> notepad pyproject.toml
```

The `dependencies` field should now include `"faker"`:

```toml
dependencies = [
    "faker",
]
```

Close Notepad.

4. Create a new script. In VS Code, create a new file and save it as `generate_employees.py` in the `data-processor` folder. Write the following code:

```python
# generate_employees.py - Generate fake employee data

from faker import Faker

fake = Faker()

print("=== Generated employee data ===")
print(f"{'Name':<25} {'Email':<30} {'Phone':<15}")
print("-" * 72)

for _ in range(5):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    print(f"{name:<25} {email:<30} {phone:<15}")

print("-" * 72)
print("5 employee records generated")
```

5. Save the file as `generate_employees.py` in the `C:\labs\data-processor` directory.

6. Run the script with uv:

```
C:\labs\data-processor> uv run generate_employees.py
```

You should see a formatted table with five rows of fake employee data.

7. Run it again — notice that the data is different each time, because Faker generates random values.

**Verification**: The script runs without import errors. The output is a formatted table with five rows of fake data.

**Expected output**: A header line, a separator, five rows of generated data (name, email, phone), and a footer. Each row has left-aligned columns. The exact data values differ each run.

**Hints**:
- If you see `ModuleNotFoundError: No module named 'faker'`, make sure you are using `uv run` (not `python`), and that you ran `uv add Faker` in the current project directory
- The underscore `_` in `for _ in range(5)` is a convention meaning "I do not need this variable"

**Try it yourself**:
- Change `range(5)` to `range(10)` to generate more records
- Add a `fake.job()` column to the table
- Add a `fake.city()` column

---

### Exercise 1.4.4: Compare pip and uv workflows

**Time**: 10 minutes  
**Difficulty**: Intermediate  
**Tool**: Command line  
**Objective**: Understand the practical differences between pip and uv.

**Scenario**: You want to summarize what you learned and verify that uv's dependency tracking works as expected.

**Tasks**:

1. First, verify that `pyproject.toml` records all dependencies:

```
C:\labs\data-processor> type pyproject.toml
```

You should see `faker` listed in the `dependencies` array.

2. Notice the `uv.lock` file. List it:

```
C:\labs\data-processor> dir uv.lock
```

This lock file records the exact versions of every package installed. It ensures that anyone who runs `uv sync` on this project gets identical versions.

3. Create a summary script. In VS Code, create a new file and save it as `summary.py` in the `data-processor` folder. Write:

```python
# summary.py - Demonstrate uv project structure

import sys
from pathlib import Path

print("=== Project environment summary ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {Path.cwd()}")
print()

# Read pyproject.toml to show dependencies
toml_path = Path("pyproject.toml")
if toml_path.exists():
    content = toml_path.read_text()
    print("=== pyproject.toml contents ===")
    print(content)
else:
    print("pyproject.toml not found")
```

4. Save as `summary.py` in `C:\labs\data-processor`.

5. Run it:

```
C:\labs\data-processor> uv run summary.py
```

6. Observe the output. Notice that the Python executable path points to a virtual environment inside the project (`.venv` folder), not the system Python. uv created an isolated environment automatically.

7. Now try running the same script with plain `python`:

```
C:\labs\data-processor> python summary.py
```

Compare the Python executable paths. The `uv run` version uses the project's virtual environment; the `python` version uses the system Python.

**Verification**: `pyproject.toml` lists the Faker dependency. The `uv.lock` file exists. The `uv run` command uses an isolated Python environment.

**Expected output**: The summary shows the Python version, the path to the executable (inside `.venv` when using `uv run`), and the contents of `pyproject.toml` including the dependency on Faker.

**Try it yourself**:
- Add a second package: `uv add cowsay` and check that `pyproject.toml` now lists two dependencies
- Write a quick script that uses `cowsay` and run it with `uv run`
- Remove a package: `uv remove cowsay` and verify it disappears from `pyproject.toml`

---

## 7. Validation checklist

- [ ] You installed and uninstalled a package with pip
- [ ] `uv init data-processor` created a project directory with `pyproject.toml`
- [ ] `uv add Faker` added the dependency and updated `pyproject.toml`
- [ ] `uv run generate_employees.py` executed the script using the project's environment
- [ ] `pyproject.toml` shows Faker in the dependencies list
- [ ] `uv.lock` exists in the project directory
- [ ] You understand the difference between `python script.py` and `uv run script.py`

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `'uv' is not recognized` | uv not installed or not on PATH | Ask your instructor. Try closing and reopening the terminal. |
| `'pip' is not recognized` | pip not on PATH | Try `python -m pip` instead of `pip` |
| `ModuleNotFoundError: No module named 'faker'` | Using `python` instead of `uv run` | Use `uv run script.py` to run within the project environment |
| `error: No pyproject.toml found` | Not inside a uv project directory | Navigate to the project folder first with `cd` |
| `uv add` fails with network error | No internet connection or firewall blocking | Check network connectivity. Ask instructor if on restricted network. |

**Common beginner pitfalls:**
- Using `uv pip install` instead of `uv add`. Always use `uv add` — it updates `pyproject.toml` automatically. `uv pip install` does not.
- Running `python script.py` instead of `uv run script.py` inside a uv project. The system Python does not know about project-specific packages.
- Forgetting to `cd` into the project directory before running `uv add` or `uv run`.

---

## 9. Questions

1. Explain why installing packages globally (using `pip install` without a project) can cause problems when you work on multiple projects. What specific issues might arise?

2. Your colleague sends you a Python project that uses three external packages but has no `pyproject.toml` or `requirements.txt`. You run the script and get `ModuleNotFoundError`. How would you figure out which packages to install, and how could this situation have been prevented?

3. Compare the role of `pyproject.toml` in a uv project with the role of a recipe in cooking. What specific problems does declarative dependency management solve?

4. When you ran `uv run summary.py`, the Python executable pointed to a `.venv` directory inside the project, not the system Python. Explain what a virtual environment is and why isolating project dependencies matters.

5. You run `uv add requests` and it succeeds, but later `uv add requests==2.25.0` (an older version). What do you think happens to `pyproject.toml`? Why might you want to specify a particular version of a package?

---

## 10. Clean-up

Keep the project for future reference:
- `C:\labs\data-processor\` — your first uv project

Files created in this lab:
- `C:\labs\data-processor\generate_employees.py`
- `C:\labs\data-processor\summary.py`

The Faker package installed via pip in Exercise 1.4.1 was already uninstalled during the exercise.

**Note**: Do NOT uninstall Python, pip, or uv. Do NOT delete the `.venv` directory manually.

---

## 11. Key takeaways

- pip is the traditional package manager: `pip install <package>` / `pip uninstall <package>`
- pip does not automatically track dependencies in a project file
- uv is a modern, fast package manager with integrated project management
- `uv init <project>` creates a project with `pyproject.toml`
- `uv add <package>` installs a package and records it in `pyproject.toml`
- `uv run <script.py>` executes a script in the project's isolated environment
- `pyproject.toml` declares dependencies explicitly — anyone can reproduce your setup
- `uv.lock` pins exact versions for reproducibility
- From this point forward, use `uv add` (not `pip install`) for all package management
- Use `uv run` (not `python`) to run scripts in uv-managed projects

---

## 12. Additional resources

- uv documentation: https://docs.astral.sh/uv/
- pip documentation: https://pip.pypa.io/en/stable/
- Python Packaging User Guide: https://packaging.python.org/
- PyPI — Python Package Index: https://pypi.org/
- pyproject.toml specification: https://packaging.python.org/en/latest/specifications/pyproject-toml/

---

## 13. Appendices

### Appendix A: Quick reference — Package management commands

**pip commands (traditional):**

| Command | Action |
|---------|--------|
| `pip install <package>` | Install a package |
| `pip uninstall <package>` | Remove a package |
| `pip list` | List installed packages |
| `pip show <package>` | Show package details |

**uv commands (modern, preferred):**

| Command | Action |
|---------|--------|
| `uv init <project>` | Create a new project with `pyproject.toml` |
| `uv add <package>` | Add a dependency (updates `pyproject.toml`) |
| `uv remove <package>` | Remove a dependency |
| `uv run <script.py>` | Run a script in the project environment |
| `uv sync` | Install all dependencies from `pyproject.toml` |
| `uv lock` | Update the lock file |

### Appendix B: pyproject.toml structure

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Project description"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "faker",
    "requests",
]
```

### Appendix C: Environment information

- Python: `python --version`
- pip: `pip --version`
- uv: `uv --version`
- Package management: `uv add <package>`
- Run scripts: `uv run script.py`

---

## 14. Answers

**Answer 1:**

Global installation means every project on your system shares the same set of packages. This causes problems when two projects need different versions of the same package. For example, Project A requires `requests==2.28.0` and Project B requires `requests==2.31.0`. You can only have one version installed globally, so one project breaks.

Additionally, global installations create "dependency clutter" over time. After working on many projects, your system accumulates dozens of packages. You cannot easily tell which project needs which package. If you need to set up a clean environment or share your project, you cannot generate an accurate dependency list.

Virtual environments (created automatically by uv) solve this: each project has its own isolated set of packages. Project A and Project B can each have the exact version they need without conflict.

**Answer 2:**

Without a dependency file, you have to discover the dependencies by reading the code. Look for all `import` statements and `from ... import` statements, then determine which of those modules are not part of the standard library. Install each missing one. This is tedious and error-prone — you might miss a transitive dependency or install the wrong version.

This situation is prevented by using declarative dependency management from the start. With uv, every `uv add` call updates `pyproject.toml`. When your colleague receives the project, they run `uv sync` and all dependencies install automatically. The lock file ensures they get the exact same versions you used.

**Answer 3:**

A `pyproject.toml` is like a recipe that lists every ingredient (package) and the quantities (versions) needed. Without a recipe, someone trying to recreate your dish would have to guess the ingredients by tasting the final product — unreliable and time-consuming.

Declarative dependency management solves several specific problems: reproducibility (anyone can recreate your environment), portability (the project works on any machine), clarity (you know exactly what your project depends on), and automation (tools like `uv sync` install everything automatically). It also prevents "works on my machine" problems where code runs on your computer but fails on a colleague's because they are missing a package.

**Answer 4:**

A virtual environment is an isolated Python installation specific to one project. It contains its own copy of the Python interpreter and its own set of installed packages, separate from the system Python and other projects.

Isolation matters because different projects often need different packages (or different versions of the same package). Without virtual environments, installing a package for one project affects all projects. This leads to version conflicts, broken dependencies, and difficulty reproducing setups. With a virtual environment, each project is self-contained. You can install, upgrade, or remove packages freely without affecting anything else on the system.

uv creates virtual environments automatically when you run `uv init` or `uv add`. You do not need to manage them manually — uv handles activation and package installation within the environment when you use `uv run`.

**Answer 5:**

When you run `uv add requests==2.25.0`, uv updates `pyproject.toml` to specify that exact version. The dependency entry changes from `"requests"` (any compatible version) to `"requests==2.25.0"` (exactly this version). uv also updates the lock file.

You might want a specific version for several reasons: compatibility with other libraries, reproducing a known-working configuration, matching a production server's setup, or avoiding a bug introduced in a newer version. However, pinning to an exact version also means you do not get security updates or bug fixes automatically. In practice, projects often use version ranges (like `"requests>=2.28,<3.0"`) to allow updates within a compatible range.

---

## 15. Code solutions

### Exercise 1.4.3: generate_employees.py

```python
# generate_employees.py - Generate fake employee data

from faker import Faker

fake = Faker()

print("=== Generated employee data ===")
print(f"{'Name':<25} {'Email':<30} {'Phone':<15}")
print("-" * 72)

for _ in range(5):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    print(f"{name:<25} {email:<30} {phone:<15}")

print("-" * 72)
print("5 employee records generated")
```

### Exercise 1.4.4: summary.py

```python
# summary.py - Demonstrate uv project structure

import sys
from pathlib import Path

print("=== Project environment summary ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {Path.cwd()}")
print()

# Read pyproject.toml to show dependencies
toml_path = Path("pyproject.toml")
if toml_path.exists():
    content = toml_path.read_text()
    print("=== pyproject.toml contents ===")
    print(content)
else:
    print("pyproject.toml not found")
```
