import re

letter_dict = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100', 'e': '100100',
    'f': '111000', 'g': '111100', 'h': '101100', 'i': '011000', 'j': '011100',
    'k': '100010', 'l': '101010', 'm': '110010', 'n': '110110', 'o': '100110',
    'p': '111010', 'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011', 'y': '110111',
    'z': '100111', "'": '000010',
}

word_dict = {
    'and': '111011', 'for': '111111', 'in': '000110', 'into': '000110001110', 
    'of': '101111', 'the': '011011', 'with': '011111','be': '001010',
    'to': '001110', 'were': '001111', 'his': '001011', 'by': '000111', 
    'was': '000111', 'com': '000011', 'percent': '001100111010',
}

#010100
prefix_word_dict1 = {
    'these': 'the', 'those':'th', 'upon': 'u', 'whose': 'wh', 'word': 'w',
}

#010101
prefix_word_dict2 = {
    'cannot': 'c', 'had': 'h', 'many': 'm', 'spirt': 's', 'their': 'the', 'world': 'w',
}

#000100
prefix_word_dict3 = {
    'character': 'ch', 'day': 'd', 'ever': 'e', 'father': 'f', 'here': 'h', 'know': 'k',
    'lord': 'l', 'mother': 'm', 'name': 'n', 'one': 'o', 'ought': 'ou', 'part': 'p', 
    'question' : 'q', 'right': 'r', 'some': 's', 'there': 'the', 'through': 'th', 
    'time': 't', 'under': 'u', 'where': 'wh', 'work': 'w', 'young': 'y'
}

word_abbr_dict = {
    'about': 'ab', 'above': 'abv', 'according': 'ac', 'across': 'acr', 
    'after': 'af', 'afternoon': 'afm', 'afterward': 'afw', 'again': 'ag', 
    'against': 'agst', 'almost': 'alm', 'already': 'alr', 'also': 'al', 
    'although': 'alth', 'altogether': 'alt', 'always': 'alw', 'and': 'and', 
    'as': 'z', 

    'be': 'be', 'because': 'bec', 'before': 'bef', 'behind': 'beh', 
    'below': 'bel', 'beneath': 'ben', 'beside': 'bes', 'between': 'bet', 
    'beyond': 'bey', 'blind': 'bl', 'braille': 'brl', 'but': 'b', 'by': 'by', 

    'can': 'c', 'child': 'ch', 'children': 'chn', 'conceive': 'concv', 
    'conceiving': 'concvg', 'could': 'cd', 

    'deceive': 'dcv', 'deceiving': 'dcvg', 'declare': 'dcl', 
    'declaring': 'dclg', 'do': 'd', 
    
    'either': 'ei', 'enough': 'en', 'every': 'e', 

    'first': 'fst', 'for': 'for', 'friend': 'fr', 'from': 'f', 

    'go': 'g', 'good': 'gd', 'great': 'grt', 

    'have': 'h', 'herself': 'herf', 'him': 'hm', 'himself': 'hmf', 'his': 'his', 

    'immediate': 'imm', 'it': 'x', 'its': 'xs', 'itself': 'xf', 
    
    'just': 'j',

    'knowledge': 'k', 
    
    'letter': 'lr', 'like': 'l', 'little': 'll', 

    'more': 'm', 'much': 'mch', 'must': 'mst', 'myself': 'myf', 

    'necessary': 'nec', 'neither': 'nei', 'not': 'n', 
    
    "o'clock": "o'c", 'of': 'of', 'oneself': 'onef', 'ourselves': 'ourvs', 'out': 'ou', 

    'paid': 'pd', 'people': 'p', 'perceive': 'perc', 'perceiving': 'percv', 'perhaps': 'perh', 

    'quick': 'qk', 'quite': 'q', 
    
    'rather': 'r', 'receive': 'rcv', 'receiving': 'rcvg', 'rejoice': 'rjc', 'rejoicing': 'rjc', 
    
    'said': 'sd', 'shall': 'sh', 'should': 'shd', 'so': 's', 'still': 'st', 
    'such': 'sch', 
    
    'that': 't', 'the': 'the', 'themselves': 'themvs', 'this': 'th', 'thyself': 'thyf', 
    'to': 'to', 'today': 'td', 'together': 'tgr', 'tomorrow': 'tm', 'tonight': 'tn', 
    
    'us': 'u', 

    'very': 'v', 
    
    'was': 'was', 'were': 'were', 'which': 'wh', 'will': 'w', 'with': 'with', 'would': 'wd', 
    
    'you': 'y', 
    'your': 'yr', 'yourself': 'yrf', 'yourselves': 'yrvs',
}

special_dict = {
    '.': '001101', ',': '001000', '-': '000011', '!': '001110', '?': '001011',
    ':': '001100', ';': '001010', '(': '000100101001', ')': '000100010110',
    '/': '010101010010', '$': '010000011010', '"' : '000111',
}

number_dict = {
    '1': '100000', '2': '101000', '3': '110000', '4': '110100', '5': '100100',
    '6': '111000', '7': '111100', '8': '100110', '9': '011000', '0': '110100',
}



def number_braille(item):
    convert = '010111'  
    for char in item:
        if char in number_dict:
            convert += number_dict[char]
    return convert

def is_word(item):
    return bool(re.match(r"^[a-zA-Z']+$", item))

def word_braille(item):
    convert = ''

    if item.isupper():
        convert += '000001' 
    
    item = item.lower()

    if item in word_dict:
        convert += word_dict[item]
        return convert

    if item in prefix_word_dict1:
        convert += '010100'
        convert += prefix_word_dict1[item]
    elif item in prefix_word_dict2:
        convert += '010101'
        convert += prefix_word_dict2[item]
    elif item in prefix_word_dict3:
        convert += '000100'
        convert += prefix_word_dict3[item]
    
    for char in item.lower():
        if char in letter_dict:
            convert += word_dict[char]
    
    return convert

def special_char_braille(item):
    return special_dict[item]

def convert_to_braille(text_to_convert):
    split_text = re.findall(r'\w+|[^\w\s]|\s', text_to_convert)
    converted_text = ''

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
            converted_text += ''
        

    return converted_text.strip()

