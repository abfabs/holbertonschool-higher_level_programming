# Python – Data Structures: Lists & Tuples

A collection of small Python exercises focused on core data structures—primarily lists and tuples—plus a few utility tasks. The goal is to practice indexing, slicing, immutability vs. mutability, in-place vs. copy semantics, and writing simple, well-documented functions.

## Learning objectives

By the end of this project, you should be able to:
- Work with lists and tuples (create, access, modify, iterate)
- Distinguish mutable vs. immutable types and when to use each
- Write functions that avoid side effects (returning new objects vs. mutating inputs)
- Format and print lists and matrices cleanly
- Use tuple packing/unpacking to write concise code
- Implement small, testable utilities in Pythonic style

## Requirements

- Python 3.x (Holberton projects typically use Python 3.8+ on Ubuntu 20.04)
- Files end with a newline and start with the shebang `#!/usr/bin/python3` for scripts
- Code should be PEP 8 compliant (e.g., check with `pycodestyle`)
- No external modules unless stated
- Include docstrings for modules and functions
- Guard executable code with `if __name__ == "__main__":`

## Project structure

Typical tasks/files for this project (update to match your exact files):

| File | Purpose |
|---|---|
| `0-print_list_integer.py` | Print all integers in a list (one per line). |
| `1-element_at.py` | Retrieve an element from a list at a given index. |
| `2-replace_in_list.py` | Replace an element in a list at a given index (in-place). |
| `3-print_reversed_list_integer.py` | Print a list of integers in reverse order. |
| `4-new_in_list.py` | Return a **new** list with one element replaced (original unchanged). |
| `5-no_c.py` | Return a string with all `c`/`C` characters removed. |
| `6-print_matrix_integer.py` | Nicely print a matrix of integers. |
| `7-add_tuple.py` | Add two tuples element-wise; missing items treated as `0`. |
| `8-multiple_returns.py` | Return a tuple summary of a string (e.g., length and first char). |
| `9-max_integer.py` | Return the max integer in a list (or `None` for empty lists). |
| `10-divisible_by_2.py` | Return a list of booleans indicating even numbers. |
| `11-delete_at.py` | Delete the item at a specific index in a list (in-place). |
| `12-switch.py` | Swap the values of two variables without using a temp. |
| `13-is_palindrome.c` | (C) Check if a singly linked list is a palindrome. |
| `lists.h` | Header for the C palindrome task (structs and prototypes). |
| `linked_lists.c` | Helpers for the C task (create/print/free list). |
| `100-print_python_list_info.c` | (Advanced) Print info about Python lists via the CPython API. |

> If your repository’s filenames differ, update the table accordingly. The descriptions still apply.

## Usage

Most files provide a function you can import and test quickly from the shell:

```bash
# Example: test add_tuple
python3 -c "from add_tuple import add_tuple; print(add_tuple((1, 2), (3, 4)))"
# -> (4, 6)

# Example: test new_in_list (original list unchanged)
python3 - << 'PY'
from new_in_list import new_in_list
src = [10, 20, 30]
dst = new_in_list(src, 1, 99)
print('src:', src)   # [10, 20, 30]
print('dst:', dst)   # [10, 99, 30]
PY
````

For scripts that should be executable on their own (e.g., `12-switch.py`), make sure permissions are set:

```bash
chmod +x 12-switch.py
./12-switch.py
```

For the C palindrome task:

```bash
gcc -Wall -Werror -Wextra -pedantic linked_lists.c 13-is_palindrome.c -o pal
./pal
```

## Notes and tips

* Prefer returning new lists (pure functions) when the task asks not to modify inputs.
* When printing matrices, avoid trailing spaces on lines.
* Handle edge cases: empty lists, negative indices, `None`, non-existent indices.
* Docstrings help clarify behavior, inputs, and return values.
* Keep functions small and test them in isolation.

## Running style checks

```bash
pycodestyle .
# or target a single file
pycodestyle 7-add_tuple.py
```

## Author

* **BB (abfabs)** — [github.com/abfabs](https://github.com/abfabs)

```
::contentReference[oaicite:0]{index=0}
```
