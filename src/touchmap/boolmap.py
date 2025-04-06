def bool_to_braille(value: bool, binary: bool) -> str:
    braille_true = "⠠⠞⠗⠥⠑"  
    braille_false = "⠠⠋⠁⠇⠎⠑"

    binary_true = "000001011100111101010100"
    binary_false = "00000110011010001110100101"

    if value:
        if binary:
            return binary_true
        return braille_true
    
    if binary:
        return binary_false
    
    return braille_false