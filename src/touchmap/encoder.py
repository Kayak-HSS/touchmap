import re
from typing import Literal
from .boolmap import bool_to_braille

def text_to_braille(text, grade: Literal[1, 2] =1, characterError: bool =True, binary: bool =False) -> str:

    if not isinstance(text, str): 

        if isinstance(text, bool):
            return bool_to_braille(text, binary)

        elif isinstance(text, (int, float)):
            return ""

        elif hasattr(text, "__str__"):
            text = str(text)
        else:
            raise TypeError("Unsupported type for text. Must be str, int, float, bool, or implement __str__().")

    return ""

