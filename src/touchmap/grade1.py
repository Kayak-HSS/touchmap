import re

def text_to_braille1(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    split_text = re.findall(r"\d+\.\d+|[a-zA-Z]+|\d+|[^\w\s]|\s", text)
    converted_text = ""

    for item in split_text:

        if item.isdigit():
            converted_text += number_braille(item)
        elif is_word(item):
            converted_text += word_braille(item)
        elif item in special_dict:
            converted_text += special_char_braille(item)
        elif item == ' ':
            converted_text += ' '
        else:
            raise ValueError(f"Unsupported character: '{item}'")

