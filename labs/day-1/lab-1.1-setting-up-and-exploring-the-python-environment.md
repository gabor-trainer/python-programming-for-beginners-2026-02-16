# Lab 1.1: Setting up and exploring the Python environment

**Estimated time**: 45 minutes  
**Difficulty level**: Beginner  
**Python version**: 3.12+  
**Tools**: Python REPL, VS Code, command line

---

## 2. Learning objectives

By the end of this lab, you will be able to:

- Verify that Python is installed and accessible from the command line
- Launch the Python REPL and execute arithmetic expressions and function calls
- Open VS Code, write a Python script, and run it from the integrated terminal
- Run a Python script from an external command prompt
- Recognize the difference between interactive (REPL) and script-based execution

---

## 3. Prerequisites

**Knowledge prerequisites**: None — this is the first lab.

**Environment confirmation**:
- [ ] You have access to your ALEF lab computer (via Remote Desktop)
- [ ] Python 3.12+ is installed and on PATH
- [ ] VS Code is installed with the Python extension

---

## 4. Lab-specific setup

**Before you start checklist:**

- [ ] Open a terminal: press `Win + R`, type `cmd`, press Enter
- [ ] Run `python --version` — you should see `Python 3.12.x` (or newer)

If the version check succeeds, you are ready to begin.

**Working directory:**

Create a folder for today's labs and navigate into it:

```
C:\> mkdir C:\labs
C:\> cd C:\labs
```

---

## 5. Concept overview

Programming is the act of writing instructions that a computer executes. Python lets you write these instructions in readable, concise text. The computer reads your instructions from top to bottom and carries them out.

There are two ways to give Python instructions: **interactively** (type one line, see the result immediately) and **via scripts** (write multiple lines in a file, run the entire file at once). Both are essential skills. The REPL is ideal for quick experiments. Scripts are how you build real programs.

In this lab, you will try both approaches. You will start in the REPL to get comfortable, then move to VS Code to write your first saved program, and finally run that program from the command line.

---

## 6. Exercises

**Problems you will solve in this lab:**
- Verify your Python environment is working correctly
- Execute Python expressions and function calls interactively
- Create, save, and run a Python script file

---

### Exercise 1.1.1: Verify your Python installation

**Time**: 5 minutes  
**Difficulty**: Basic  
**Tool**: Command line  
**Objective**: Confirm Python is installed, accessible, and the correct version.

**Scenario**: Before writing any code, you need to confirm the tools are ready. A developer always verifies the environment first.

**Tasks**:

1. Open a command prompt (if not already open).

2. Check the Python version:

```
C:\labs> python --version
```

You should see output like:

```
Python 3.12.1
```

The exact patch version may differ. Any `3.12.x` or newer is fine.

3. Check that pip is available:

```
C:\labs> pip --version
```

You should see output showing the pip version and the Python it is associated with.

4. Check that VS Code is accessible by running:

```
C:\labs> code --version
```

You should see the VS Code version number. If VS Code opens instead, that also confirms it is installed.

**Verification**: All three commands produce output without errors.

**Expected output**: `python --version` prints a version starting with `3.12` or higher. `pip --version` prints a version line. `code --version` prints the VS Code version.

---

### Exercise 1.1.2: Explore the Python REPL

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: Python REPL  
**Objective**: Learn to use the interactive REPL for quick experiments.

**Scenario**: You want to use Python as a calculator and test simple commands before writing a full script.

**Tasks**:

1. Start the Python REPL:

```
C:\labs> python
```

You should see the Python version header and the `>>>` prompt.

2. Try arithmetic expressions. Type each line at the `>>>` prompt and press Enter:

```python
>>> 2 + 3
5
>>> 10 - 4
6
>>> 7 * 8
56
>>> 100 / 3
33.333333333333336
>>> 100 // 3
33
>>> 100 % 3
1
>>> 2 ** 10
1024
```

3. Try using parentheses to control order of operations:

```python
>>> (2 + 3) * 4
20
>>> 2 + 3 * 4
14
```

4. Use the `print()` function:

```python
>>> print("Hello, World!")
Hello, World!
>>> print(2 + 2)
4
```

5. Create a variable and use it:

```python
>>> name = "Alice"
>>> print(name)
Alice
>>> greeting = "Hello, " + name + "!"
>>> print(greeting)
Hello, Alice!
```

6. Use the `type()` function to inspect values:

```python
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("hello")
<class 'str'>
>>> type(True)
<class 'bool'>
```

7. Exit the REPL:

```python
>>> exit()
```

**Verification**: You return to the `C:\labs>` command prompt after `exit()`.

**Expected output**: Each expression produces an immediate result. `type()` shows the class of each value.

**Try it yourself**:
- Calculate how many seconds there are in a day (60 * 60 * 24)
- Compute 3 to the power of 20 using `**`
- Create a variable with your name and print a greeting

---

### Exercise 1.1.3: Write and run a script in VS Code

**Time**: 15 minutes  
**Difficulty**: Basic  
**Tool**: VS Code  
**Objective**: Create a Python script file, save it, and run it from VS Code's integrated terminal.

**Scenario**: You need to write a short program that performs multiple steps. Typing each line in the REPL would be tedious and not reusable. A script file solves this.

**Tasks**:

1. Open VS Code. You can do this from the Start menu (search for "Visual Studio Code") or from the command line:

```
C:\labs> code .
```

This opens VS Code with the `C:\labs` folder as your workspace.

2. Create a new file: click the new-file icon in the Explorer sidebar (left panel), or press `Ctrl+N`.

3. If you pressed `Ctrl+N`, save the file immediately: press `Ctrl+S`, navigate to `C:\labs`, and name it `hello.py`.

   If you used the Explorer icon, type `hello.py` as the filename and press Enter.

4. Type the following code in the editor:

```python
# hello.py - My first Python script
print("=== My First Python Program ===")
print()

name = "Alice"
age = 28
city = "Budapest"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print()
print(f"{name} is {age} years old and lives in {city}.")
```

5. Save the file: press `Ctrl+S`.

6. Open the integrated terminal: press `` Ctrl+` `` (backtick key, typically above Tab). A terminal panel appears at the bottom of VS Code.

7. In the terminal, run the script:

```
C:\labs> python hello.py
```

The output appears in the terminal.

**Verification**: The terminal displays the formatted output with no errors.

**Expected output**: Five lines of text. The first line is a header with `===`. Then the name, age, and city appear each on their own line. The last line combines all three into a sentence.

**Tip**: If the terminal opens in a different directory, type `cd C:\labs` to navigate to your working folder.

**Try it yourself**:
- Change the values of `name`, `age`, and `city` to your own details, save, and run again
- Add another variable (for example, `profession`) and include it in the output

---

### Exercise 1.1.4: Run a script from the command line

**Time**: 10 minutes  
**Difficulty**: Basic  
**Tool**: Command line  
**Objective**: Execute a Python script directly from an external command prompt.

**Scenario**: In production and automation, scripts run from the command line — not from an editor. You need to know both approaches.

**Tasks**:

1. Open an external command prompt (leave VS Code open).

2. Navigate to your labs folder:

```
C:\> cd C:\labs
```

3. Confirm your script file exists:

```
C:\labs> dir hello.py
```

You should see `hello.py` listed.

4. Run the script:

```
C:\labs> python hello.py
```

The same output you saw in VS Code appears in the command prompt.

5. Create a second script. You can create it in VS Code (recommended) or with Notepad. In VS Code, click the new-file icon and name it `greeting.py`. Type the following code:

```python
# greeting.py - Interactive greeting
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python programming.")
```

Save the file (`Ctrl+S`).

6. Run the interactive script from the command prompt:

```
C:\labs> python greeting.py
What is your name? Alice
Hello, Alice! Welcome to Python programming.
```

Type your name when prompted and press Enter.

**Verification**: Both scripts execute without errors. The second script waits for your input and responds with a personalized greeting.

**Expected output**: `hello.py` produces the same formatted output as in VS Code. `greeting.py` asks for your name and prints a greeting that includes it.

**Try it yourself**:
- Modify `greeting.py` to ask for both a name and a favorite color, then print a sentence using both

---

## 7. Validation checklist

- [ ] `python --version` shows Python 3.12 or newer
- [ ] You can start and exit the REPL (`python` then `exit()`)
- [ ] VS Code opens and you can create `.py` files
- [ ] `hello.py` exists in `C:\labs` and runs in both VS Code's terminal and an external command prompt
- [ ] `greeting.py` exists in `C:\labs`, accepts input, and prints a greeting
- [ ] You understand the difference between REPL (interactive) and script (file-based) execution

---

## 8. Troubleshooting guide

| Error | Cause | Solution |
|-------|-------|----------|
| `'python' is not recognized` | Python is not on the system PATH | Try `py` instead of `python`. If that fails, ask your instructor. |
| `SyntaxError: invalid syntax` | Typo in code, missing quotes or parentheses | Re-check the code carefully, character by character |
| `SyntaxError: unterminated string literal` | Missing closing quote | Ensure every `"` or `'` has a matching closing quote |
| VS Code does not open | VS Code not installed or not found | Ask your instructor. On ALEF lab machines it should be pre-installed. |
| `FileNotFoundError` when running script | Wrong directory or filename | Run `dir` to list files. Use `cd C:\labs` to navigate. |
| No syntax highlighting in VS Code | Python extension not installed | Open Extensions (`Ctrl+Shift+X`), search "Python", click Install |

**Common beginner pitfalls:**
- Typing `>>>` in a script file. The `>>>` prompt is only for the REPL. Do not include it in `.py` files.
- Forgetting to save before running. Always `Ctrl+S` first. Look for the dot on the file tab indicating unsaved changes.
- Running `python` when already inside the REPL (you will see a `NameError`). Use `exit()` first.

---

## 9. Questions

1. Explain the practical difference between using the Python REPL and writing a script file. In what situations would each approach be more suitable?

2. When you type an expression like `2 + 3` in the REPL, Python shows `5` immediately. When you put the same line in a script and run it, nothing appears on screen. Why? What would you need to add to see the result?

3. You saved a script in `C:\labs\hello.py` but when you run `python hello.py` from `C:\Users\student`, you get a `FileNotFoundError`. Explain what went wrong and describe two different ways to fix it.

4. Suppose you wrote a 50-line script in VS Code but forgot to save it, and your computer restarted. What happens to your code? What habit should you develop to avoid this?

5. A colleague asks: "Why would I use VS Code when I can type everything in the REPL?" How would you explain the limitations of the REPL for building real programs?

---

## 10. Clean-up

For this lab, keep your files — you will use the `C:\labs` directory throughout the training.

Files created in this lab:
- `C:\labs\hello.py`
- `C:\labs\greeting.py`

These files are small and do not need to be removed.

**Note**: Do NOT uninstall Python, remove it from PATH, or delete any system files.

---

## 11. Key takeaways

- `python --version` confirms your Python installation
- The REPL (`>>>`) is ideal for quick tests and exploring Python interactively
- VS Code provides a professional editor with syntax highlighting, code completion, and an integrated terminal
- Python scripts are plain text files with a `.py` extension
- Run scripts from VS Code's terminal or an external command prompt with `python script.py`
- `print()` displays output; `input()` reads user input
- f-strings (`f"..."`) embed variables directly into strings
- Always save your file before running it

---

## 12. Additional resources

- Python official tutorial — An informal introduction: https://docs.python.org/3/tutorial/introduction.html
- VS Code Python tutorial: https://code.visualstudio.com/docs/python/python-tutorial
- Python `print()` function reference: https://docs.python.org/3/library/functions.html#print
- Python `input()` function reference: https://docs.python.org/3/library/functions.html#input

---

## 13. Appendices

### Appendix A: Quick reference — Python basics

| Action | Command / code |
|--------|----------------|
| Check Python version | `python --version` |
| Start the REPL | `python` |
| Exit the REPL | `exit()` or `Ctrl+Z` then Enter |
| Print output | `print("text")` |
| Read user input | `input("prompt")` |
| f-string | `f"Hello, {name}"` |
| Comment | `# This is a comment` |

### Appendix B: VS Code keyboard shortcuts

| Action | Shortcut |
|--------|----------|
| New file | Ctrl+N |
| Open file | Ctrl+O |
| Save file | Ctrl+S |
| Open terminal | Ctrl+` |
| Toggle sidebar | Ctrl+B |
| Open command palette | Ctrl+Shift+P |
| Open extensions | Ctrl+Shift+X |
| Find in file | Ctrl+F |

### Appendix C: Environment information

- Python: `python --version`
- VS Code: `code --version`
- Run scripts: `python script.py`

---

## 14. Answers

**Answer 1:**

The REPL is an interactive session where you type one expression or statement at a time and see the result immediately. This is valuable for quick experiments — testing how a function behaves, checking the result of a calculation, or exploring a new feature. However, your work is not saved. When you close the REPL, everything is gone.

A script file is a saved program that you can run repeatedly. You write the code once, save it as a `.py` file, and execute it whenever needed. Scripts can contain dozens or thousands of lines, accept input, process data, and produce output. For any task you want to repeat or share with others, a script is the right choice.

In practice, developers often prototype in the REPL first — testing a small piece of logic — then move the working code into a script for permanent use.

**Answer 2:**

In the REPL, Python automatically displays the result of any expression you type. This is a convenience feature of the interactive mode — it evaluates the expression and shows the return value.

In a script, Python executes each line but does not display results unless you explicitly use `print()`. The line `2 + 3` in a script computes the value 5 but discards it because nothing tells Python to show it. To see the result, you would write `print(2 + 3)`.

This design makes sense: a script might compute thousands of intermediate values, and automatically printing all of them would flood the screen. The programmer decides what to display.

**Answer 3:**

The command `python hello.py` tells Python to look for `hello.py` in the current working directory, which is `C:\Users\student`. Since the file is in `C:\labs`, Python cannot find it and raises a `FileNotFoundError`.

Two fixes: First, navigate to the correct directory before running the script: `cd C:\labs` followed by `python hello.py`. Second, provide the full path to the script: `python C:\labs\hello.py`. Both approaches work. The first is more practical when you will run multiple scripts from the same directory.

**Answer 4:**

Unsaved code in VS Code exists only in memory. When the computer restarts, that memory is cleared. The code is lost permanently. VS Code may attempt to restore unsaved tabs, but this is not guaranteed, especially after a sudden restart.

The habit to develop is saving frequently — every few minutes and certainly after every significant change. Press `Ctrl+S` regularly. Some developers save almost reflexively after every few lines. With saved files, even a crash only costs the changes since your last save.

**Answer 5:**

The REPL has several limitations for building real programs. First, code in the REPL is not saved — close the session and it is gone. Second, you cannot easily edit earlier lines in a long sequence; in VS Code, you edit any line and re-run. Third, the REPL executes one statement at a time, making it difficult to write multi-line structures (functions, loops, classes) comfortably. Fourth, you cannot share REPL sessions with colleagues or run them automatically.

VS Code's editor solves all of these problems: your code is saved in a file, you can edit any part freely, you see the entire program at once, and you can run the whole thing from the integrated terminal. The REPL is a powerful complement — not a replacement — for script development.

---

## 15. Code solutions

### Exercise 1.1.3: hello.py

```python
# hello.py - My first Python script
print("=== My First Python Program ===")
print()

name = "Alice"
age = 28
city = "Budapest"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print()
print(f"{name} is {age} years old and lives in {city}.")
```

### Exercise 1.1.4: greeting.py

```python
# greeting.py - Interactive greeting
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python programming.")
```
