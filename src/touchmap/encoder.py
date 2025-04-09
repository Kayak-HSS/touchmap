import re
from typing import Literal
from .grade1map import grade1_to_braille

def text_to_braille(text, grade: Literal[1, 2] =1, characterError: bool =True, binary: bool =False) -> str:

    if not isinstance(text, str): 

        if isinstance(text, (int, float, bool)):
            return grade1_to_braille([str(text)], False, binary)

        elif hasattr(text, "__str__"):
            text = str(text)
        else:
            raise TypeError("Unsupported type for text. Must be str, int, float, bool, or implement __str__().")
    
    split_text = re.findall(r"[+-]?(?:\d+\.\d+|\.\d+|\d+)(?:[eE][+-]?\d+)?|[a-zA-Z]+|[^\w\s]|\s", text)

    if grade == 1:
        return grade1_to_braille(split_text, characterError, binary)
    elif grade == 2:
        return ""
    else:
        raise ValueError("Invalid grade. Only Grade 1 and Grade 2 are supported.")


