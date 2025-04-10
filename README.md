# TouchMap

**TouchMap** is a Python library for converting textual data into Braille representations.  
It supports both **Grade 1 and 2 Braille**. Grade 2 support is under active development.

## Features

- Converts plain text (including numbers, punctuation, and scientific notation) into Grade 1 and 2 Braille.
- Supports both **Unicode Braille** and **binary (dot) representation**.
- Handles context-sensitive characters like `"`, `x`, `*`, `/`, and `-`.
- Graceful handling of unsupported characters.

## Installation

```bash
pip install touchmap
```

## Usage

### Import the Function

```python
from touchmap import text_to_braille
```

### Function Signature

```python
def text_to_braille(text: Any, grade: int = 1, characterError: bool = True, binary: bool = False) -> str:
    ...
```

### Parameters

| Argument         | Data Type | Default Value | Required | Description                                                                         |
| ---------------- | --------- | ------------- | -------- | ----------------------------------------------------------------------------------- |
| `text`           | `Any`     | —             | Yes      | Input to be converted. Accepts strings, numbers, and booleans.                      |
| `grade`          | `1 or 2`  | `1`           | No       | Braille grade to use. Currently only `1` is supported.                              |
| `characterError` | `bool`    | `True`        | No       | If `True`, raises error on unsupported characters; if `False`, replaces with space. |
| `binary`         | `bool`    | `False`       | No       | If `True`, returns binary (6-dot) format; if `False`, returns Unicode Braille.      |

### Example

```python
from touchmap import text_to_braille

text = "The value is -3.14e+10 and x is not multiplication."

braille1 = text_to_braille(text)
braille2 = text_to_braille(text, grade=2)

binary1 = text_to_braille(text, binary=True)
binary2 = text_to_braille(text, grade=2, binary=True)

print("Grade 1 Braille:", braille1)
print("\nGrade 2 Braille:", braille2)

print("\n\nGrade 1 Binary:", binary1)
print("\nGrade 2 Binary:", binary2)
```

```bash
Grade 1 Braille: ⠠⠞⠓⠑ ⠧⠁⠇⠥⠑ ⠊⠎ ⠼⠐⠤⠉⠲⠁⠙ ⠐⠦ ⠼⠁⠚⠈⠢⠼⠐⠖⠁⠚ ⠁⠝⠙ ⠭ ⠊⠎ ⠝⠕⠞ ⠍⠥⠇⠞⠊⠏⠇⠊⠉⠁⠞⠊⠕⠝⠲

Grade 2 Braille: ⠠⠮ ⠧⠁⠇⠥⠑ ⠊⠎ ⠼⠐⠤⠉⠲⠁⠙ ⠐⠦ ⠼⠁⠚⠈⠢⠼⠐⠖⠁⠚ ⠯ ⠭ ⠊⠎ ⠝ ⠍⠥⠇⠞⠊⠏⠇⠊⠉⠁⠞⠊⠕⠝⠲


Grade 1 Binary: 000001011110101100100100000000101011100000101010100011100100000000011000011010000000010111000100000011110000001101100000110100000000000100001011000000010111100000011100010000001001010111000100001110100000011100000000100000110110110100000000110011000000011000011010000000110110100110011110000000110010100011101010011110011000111010101010011000110000100000011110011000100110110110001101

Grade 2 Binary: 000001011011000000101011100000101010100011100100000000011000011010000000010111000100000011110000001101100000110100000000000100001011000000010111100000011100010000001001010111000100001110100000011100000000111011000000110011000000011000011010000000110110000000110010100011101010011110011000111010101010011000110000100000011110011000100110110110001101
```

## Roadmap

- Implementation of partial word conversion in grade 2.
- Development of a **web API** for trying TouchMap online.
- Bugfixes

## Meta

License: **Apache License 2.0**  
Author: **Yajat Pathak**

**By Kayak for Braillent**
