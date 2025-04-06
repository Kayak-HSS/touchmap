from .numdict import braille_num_dict, binary_num_dict

def convert_fractional_part(frac_part, num_dict, max_digits=17):
    result = ""
    count = 0
    epsilon = 1e-12  # precision threshold

    while frac_part > epsilon and count < max_digits:
        frac_part *= 10
        digit = int(frac_part)
        result += num_dict[digit]
        frac_part -= digit
        count += 1

    return result


def num_to_braille(value: int | float, binary: bool) -> str:
    num_dict = binary_num_dict if binary else braille_num_dict
    converted_value = "010111" if binary else "⠼" #number prefix

    if value < 0:
        converted_value += num_dict["-"]
        value = abs(value)

    int_part = int(value)
    frac_part = value - int_part

    if int_part == 0:
        converted_value += num_dict[0]
    else:
        int_converted = ""
        while int_part > 0:
            int_converted = num_dict[int_part % 10] + int_converted
            int_part //= 10

        converted_value += int_converted

    if frac_part > 0:
        converted_value += num_dict["."]
        converted_value += convert_fractional_part(frac_part, num_dict)

    return converted_value
