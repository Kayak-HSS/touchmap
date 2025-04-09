import re
from typing import List, Any
from . import brailledict, binarydict


def is_numeric(token: str) -> bool:
    return bool(re.fullmatch(r"[+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?", token, re.IGNORECASE))

def alpha_converter(token: str, d: Any) -> str:
    converted = ""

    for char in token:
        if char.isupper():
            converted += d.alpha_dict["cap"]
            char = char.lower()
        
        converted += d.alpha_dict[char]

    return converted

def numeric_converter(token: str, d: Any) -> str:
    indicator = d.num_dict["num"]
    converted = indicator 

    for char in token:
        if char == "e" or char == "E":
            space = d.alpha_dict[" "]
            converted += space + d.overlap_char_dict["x"][1] + space + indicator + d.num_dict["1"] + d.num_dict["0"] +d.char_dict["'"]
        else :
            converted += d.num_dict[char]

    return converted

def grade1_to_braille(split_text: List[str], characterError: bool, binary: bool) -> str :
    d = binarydict if binary else brailledict
    converted_text = ""

    for token in split_text:

        if token == " ": 
            converted_text += d.alpha_dict[" "]
        elif token in d.overlap_char_dict:
            pass
        elif token.isalpha():
            converted_text += alpha_converter(token, d)
        elif token.is_numeric():
            converted_text += numeric_converter(token, d)
        elif token in d.char_dict:
            pass
        elif characterError:
            raise ValueError(f"Unsupported character '{token}'")
        else:
            converted_text += d.alpha_dict[" "]


    return converted_text




