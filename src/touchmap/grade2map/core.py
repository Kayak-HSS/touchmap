from .word_contract_dict import prefix_word_dict1, prefix_word_dict2, prefix_word_dict3, word_abbr_dict

def alpha2_converter(token: str, d1: any, d2: any) -> str:
    converted = ""

    if token.isupper():
        converted += (d1.alpha_dict["cap"] *2)
    elif token[0].isupper():
        converted += d1.alpha_dict["cap"]
    
    token = token.lower()

    if token in d2.word_dict:
        return converted + d2.word_dict[token]
    
    if token in prefix_word_dict1:
        converted += d2.prefix_whole[0]
        token = prefix_word_dict1[token]
        
    elif token in prefix_word_dict2:
        converted += d2.prefix_whole[1]
        token = prefix_word_dict2[token]

    elif token in prefix_word_dict3:
        converted += d2.prefix_whole[2]
        token = prefix_word_dict3[token]
    
    if token == "the":
        return converted + d2.word_dict["the"]
    
    if token in word_abbr_dict:
        token = word_abbr_dict[token]
    
    for char in token:        
        converted += d1.alpha_dict[char]

    return converted