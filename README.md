# TouchMap

**TouchMap** is a Python library for converting textual data into Braille representations.  
Currently, it supports **Grade 1 Braille** only. Grade 2 support is under active development.

## Features

- Converts plain text (including numbers, punctuation, and scientific notation) into Grade 1 Braille.
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
text = "The value is -3.14e+10 and x is not multiplication."
braille = text_to_braille(text)
binary = text_to_braille(text, binary=True)
print(braille)
print(binary)
```

```bash
⠠⠞⠓⠑ ⠧⠁⠇⠥⠑ ⠊⠎ ⠼⠐⠤⠉⠲⠁⠙ ⠐⠦ ⠼⠁⠚⠄⠼⠐⠖⠁⠚ ⠁⠝⠙ ⠭ ⠊⠎ ⠝⠕⠞ ⠍⠥⠇⠞⠊⠏⠇⠊⠉⠁⠞⠊⠕⠝⠲
000001011110101100100100000000101011100000101010100011100100000000011000011010000000010111010000001001110000001110100000110100000000010000110110000000010111100000010110000100010111010000101110100000010110000000100000110110110100000000110011000000011000011010000000110110100110011110000000110010100011101010011110011000111010101010011000110000100000011110011000100110110110001110
```

## Roadmap

- Implementation of **Grade 2 Braille** conversion.
- Development of a **web API** for trying TouchMap online.

## Meta

License: **Apache License 2.0**  
Author: **Yajat Pathak**

**By Kayak for Braillent**
