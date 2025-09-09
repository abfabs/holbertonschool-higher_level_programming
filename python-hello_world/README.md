# Python – Hello, World

Intro project to Python and the toolchain around it. You’ll practice running Python code from shell scripts, using basic printing/formatting, simple string operations, and (optionally) a small C algorithm task to detect cycles in a linked list.

## Learning objectives

By the end of this project, you should be able to:
- Run Python scripts and one-liners from the shell (`$PYFILE`, `$PYCODE`)
- Use `print()` with strings, integers, and floats (proper formatting, no casting hacks)
- Apply basic string operations: concatenation, repetition, slicing
- Follow PEP 8 style with `pycodestyle`
- (Advanced) Write a short C function and compile with strict flags
- (Advanced) Write to `stderr` and exit with a specific status code

## Requirements

- Ubuntu 20.04 LTS, Python 3.8+ (Holberton default)
- All Python files: executable, end with a newline, and start with `#!/usr/bin/python3`
- Follow PEP 8 (`pycodestyle`) and include simple module/function docstrings when applicable
- Shell scripts: executable and POSIX-compatible (`/bin/bash`)
- C files (if present): compile with `gcc -Wall -Werror -Wextra -pedantic -std=gnu89`
- No external libraries unless the task specifies otherwise

## Project structure

> Update filenames if your repo differs. Some curricula use **“Best School”** instead of **“Holberton School”** in output—adjust strings to match your checker.

| File | Purpose |
|---|---|
| `0-run` | Shell script that runs a Python script whose path is in `$PYFILE`. |
| `1-run_inline` | Shell script that runs Python code provided in `$PYCODE`. |
| `2-print.py` | Print a fixed message using `print()`. |
| `3-print_number.py` | Print an integer with surrounding text (no casting—use formatting). |
| `4-print_float.py` | Print a float with 2 decimal places. |
| `5-print_string.py` | Print a string 3 times and then print its first 9 characters. |
| `6-concat.py` | Concatenate strings to output a welcome message. |
| `7-edges.py` | Slice a string to get first, last, and middle parts. |
| `8-concat_edges.py` | Build a specific sentence by slicing and concatenating substrings. |
| `9-easter_egg.py` | Print “The Zen of Python” by importing `this`. |
| `10-check_cycle.c` | C function to detect a cycle in a singly linked list. |
| `lists.h` | Header for the linked list structure and prototypes (C task). |
| `linked_lists.c` / `10-main.c` | Test helpers/mains for the C task (names may vary). |
| `100-write.py` | Write a message to `stderr` using `sys.stderr.write()` and exit with status `1`. |
| `101-compile` | Shell script that “compiles” a Python file in `$PYFILE` to bytecode. |
| `102-magic_calculation.py` | Recreate a function based on given Python bytecode (logic-only). |

## Usage

### Run from shell scripts

```bash
# 0-run: execute the Python file in $PYFILE
export PYFILE=main.py
./0-run

# 1-run_inline: run inline Python from $PYCODE
export PYCODE='print("Hello from inline code")'
./1-run_inline
````

### Run individual Python tasks

```bash
python3 2-print.py
python3 3-print_number.py
python3 4-print_float.py
python3 5-print_string.py
python3 9-easter_egg.py
```

### Format examples

```python
# 3-print_number.py (example idea)
number = 98
print(f"{number} Battery street")
# or: print("{} Battery street".format(number))

# 4-print_float.py (example idea)
number = 3.14159
print(f"Float: {number:.2f}")
```

### C cycle detection (if included)

```bash
# Example compile line (adjust file names if yours differ)
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 \
    10-check_cycle.c 10-main.c linked_lists.c -o cycle

./cycle
```

## Style checks

```bash
# Python
pycodestyle .

# Shell scripts
shellcheck 0-run 1-run_inline

# C (compile with strict flags; fix all warnings/errors)
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 your_files.c -o a.out
```

## Tips

* Use f-strings or `str.format()`; avoid converting numbers to strings just to print.
* When slicing strings, double-check indices off-by-one errors.
* Keep outputs **exactly** as specified by the checker (spacing, punctuation, newline).
* For `100-write.py`, write to `stderr` and return exit status `1`.
* For `101-compile`, respect the `$PYFILE` environment variable.

## Author

* **BB (abfabs)** — [github.com/abfabs](https://github.com/abfabs)