import re
from typing import Literal, List
from .grade1map import alpha1_converter, numeric_converter, overlap_converter, binarydict, brailledict
from .grade2map import alpha2_converter
from .utils import is_numeric, get_next_token, get_prev_token


def braille_converter(split_text: List[str], grade: Literal[1, 2], characterError: bool, d: any) -> str :
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
            if grade == 1:
                converted_text += alpha1_converter(token, d)
            else:
                converted_text += alpha2_converter(token, d)

        elif is_numeric(token):
            converted_text += numeric_converter(token, d)

        elif token in d.char_dict:
            converted_text += d.char_dict[token]

        elif characterError:
            raise ValueError(f"Unsupported character '{token}'")
        else:
            converted_text += d.alpha_dict[" "]


    return converted_text


def text_to_braille(text, grade: Literal[1, 2] =1, characterError: bool =True, binary: bool =False) -> str:

    if not(grade == 1 or grade == 2):
        raise ValueError("Invalid grade. Only Grade 1 and Grade 2 are supported.")


    if not isinstance(text, str): 

        if isinstance(text, (int, float, bool)):
            return braille_converter([str(text)], 1, False, binary)

        elif hasattr(text, "__str__"):
            text = str(text)
        else:
            raise TypeError("Unsupported type for text. Must be str, int, float, bool, or implement __str__().")
    
    split_text = re.findall(r"[+-]?(?:\d+\.\d+|\.\d+|\d+)(?:[eE][+-]?\d+)?|[a-zA-Z]+|[^\w\s]|\s", text)

    d = binarydict if binary else brailledict

    return braille_converter(split_text, grade, characterError, d)
        

