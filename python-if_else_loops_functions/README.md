# Python – If/Else, Loops, Functions

Intro exercises covering Python control flow and simple functions. You’ll practice conditional statements, `for`/`while` loops, function definitions, return values, and a small C task for inserting into a sorted linked list.

## Learning objectives

By the end of this project, you should be able to:
- Use `if`, `elif`, `else` to branch logic
- Iterate with `for` and `while` (including `break`/`continue`)
- Write and call functions with parameters and return values
- Work with characters and ASCII, basic arithmetic, and string formatting
- Follow PEP 8 style (`pycodestyle`) and shebang/permissions conventions
- (C task) Insert a node into a sorted singly linked list

## Requirements

- Ubuntu 20.04 LTS, Python 3.8+
- All Python scripts start with `#!/usr/bin/python3`, are executable, and end with a newline
- No external libraries unless stated
- Code style: PEP 8 (`pycodestyle`)
- C files (if present) compile with:
```

gcc -Wall -Werror -Wextra -pedantic -std=gnu89

````

## Project structure

> Filenames follow common Holberton conventions for this project. If any differ in your repo, update the table accordingly.

| File | Purpose |
|---|---|
| `0-positive_or_negative.py` | Print whether a random number is positive, zero, or negative. |
| `1-last_digit.py` | Print the last digit of a random number with a specific message. |
| `2-print_alphabet.py` | Print the lowercase alphabet without newline separators. |
| `3-print_alphabt.py` | Print the alphabet except `q` and `e`. |
| `4-print_hexa.py` | Print numbers 0–98 with their hexadecimal representation. |
| `5-print_comb2.py` | Print numbers `00`–`99` as two-digit combinations separated by `, `. |
| `6-print_comb3.py` | Print all unique two-digit combinations `01`–`89` (no repeats). |
| `7-islower.py` | Function `islower(c)` returning `True` if `c` is lowercase. |
| `8-uppercase.py` | Print a string in uppercase without using built-ins like `str.upper()`. |
| `9-print_last_digit.py` | Function that prints and returns the last digit of a number. |
| `10-add.py` | Function `add(a, b)` that returns the sum. |
| `11-pow.py` | Function `pow(a, b)` that returns `a` to the power `b`. |
| `12-fizzbuzz.py` | Print numbers 1–100 with FizzBuzz rules on a single line. |
| `13-insert_number.c` | Insert a node into a **sorted** singly linked list (C). |
| `lists.h` | C header for the singly linked list structure and prototypes. |
| `linked_lists.c` / `13-main.c` | Test helpers/mains for the C task (names may vary). |
| `100-print_tebahpla.py` | Advanced: print the alphabet in reverse, alternating case. |
| `101-remove_char_at.py` | Advanced: return a copy of a string with one char removed at index. |
| `102-magic_calculation.py` | Recreate a function based on given bytecode (logic-only). |

## Usage

Make scripts executable and run:

```bash
chmod +x 2-print_alphabet.py
./2-print_alphabet.py
````

Run specific functions quickly from the shell:

```bash
# islower
python3 - << 'PY'
from islower import islower
for ch in ['a','Z','m','!']:
    print(ch, '->', islower(ch))
PY

# add / pow
python3 - << 'PY'
from add import add
from pow import pow
print(add(10, 5))   # 15
print(pow(2, 5))    # 32
PY

# fizzbuzz (prints on one line)
python3 12-fizzbuzz.py
```

C task (sorted insert):

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 \
    13-insert_number.c linked_lists.c 13-main.c -o insert
./insert
```

## Notes and tips

* Keep outputs **exactly** as the checker expects (spacing, commas, trailing spaces, newline).
* For `6-print_comb3.py`, avoid duplicates and reversed pairs (e.g., `01`, not `10`).
* `8-uppercase.py`: operate on ASCII codes (e.g., `ord()`/`chr()`).
* `9-print_last_digit.py`: both prints and returns the digit—match that signature.
* Prefer f-strings or `format()` for clean formatting; don’t cast ints to strings just to concatenate.
* Handle edge cases (negative numbers in `print_last_digit`, empty strings, etc.).

## Style checks

```bash
pycodestyle .
# or target an individual file
pycodestyle 7-islower.py
```

## Author

* **BB (abfabs)** — [github.com/abfabs](https://github.com/abfabs)