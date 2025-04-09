def is_numeric(token: str) -> bool:
    return bool(re.fullmatch(r"[+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?", token, re.IGNORECASE))

def get_prev_token(split_text: List[str], index: int) -> str:
    i = index - 1
    while i >= 0:
        if split_text[i] != " ":
            return split_text[i]
        i -= 1
    return ""

def get_next_token(split_text: List[str], index: int) -> str:
    i = index + 1
    while i < len(split_text):
        if split_text[i] != " ":
            return split_text[i]
        i += 1
    return ""
