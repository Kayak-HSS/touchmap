from typing import List, Any
from . import binarydict, brailledict
from ..utils import is_numeric

def alpha1_converter(token: str, d: any) -> str:

    converted = ""

    for char in token:
        if char.isupper():
            converted += d.alpha_dict["cap"]
            char = char.lower()
        
        converted += d.alpha_dict[char]

    return converted

def numeric_converter(token: str, d: any) -> str:
    indicator = d.num_dict["num"]
    converted = indicator 

    for char in token:
        if char == "e" or char == "E":
            space = d.alpha_dict[" "]
            converted += space + d.overlap_char_dict["x"][1] + space + indicator + d.num_dict["1"] + d.num_dict["0"] +d.char_dict["^"] + indicator
        else :
            converted += d.num_dict[char]

    return converted

def overlap_converter(token: str, previous: str, next: str, quote_state: List[bool], d: any) -> str:

    if token == '"':
        if quote_state[0]:
            quote_state[0] = False
            return d.overlap_char_dict[token][1]  
        
        quote_state[0] = True
        return d.overlap_char_dict[token][0]

    if is_numeric(previous) and is_numeric(next):
        return d.overlap_char_dict[token][1]  
    return d.overlap_char_dict[token][0] 





