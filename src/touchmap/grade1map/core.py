import re
from typing import List, Any
from . import brailledict, binarydict
from .utils import is_numeric, get_next_token, get_prev_token

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

def overlap_converter(token: str, previous: str, next: str, quote_state: List[bool], d: Any) -> str:

    if token == '"':
        if quote_state[0]:
            quote_state[0] = False
            return d.overlap_char_dict[token][1]  
        
        quote_state[0] = True
        return d.overlap_char_dict[token][0]

    if is_numeric(previous) and is_numeric(next):
        return d.overlap_char_dict[token][1]  
    return d.overlap_char_dict[token][0] 


def grade1_to_braille(split_text: List[str], characterError: bool, binary: bool) -> str :
    d = binarydict if binary else brailledict
    converted_text = ""
    quote_state = [False]

    for i, token in enumerate(split_text):

        if token == " ": 
            converted_text += d.alpha_dict[" "]

        elif token in d.overlap_char_dict:
            previous = get_prev_token(split_text, i)
            next = get_next_token(split_text, i)
            converted_text += overlap_converter(token, previous, next, quote_state, d)

        elif token.isalpha():
            converted_text += alpha_converter(token, d)

        elif is_numeric(token):
            converted_text += numeric_converter(token, d)

        elif token in d.char_dict:
            converted_text += d.char_dict[token]

        elif characterError:
            raise ValueError(f"Unsupported character '{token}'")
        else:
            converted_text += d.alpha_dict[" "]


    return converted_text




