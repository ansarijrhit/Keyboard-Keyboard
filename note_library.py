
single_note_dict = {
    50: "a",
    59: "b",
    48: "c",
    67: "d",
    52: "e",
    47: "f",
    57: "g",
    60: "h",
    64: "i",
    58: "j",
    46: "k",
    66: "l",
    55: "m",
    62: "n",
    65: "o",
    61: "p",
    56: "q",
    53: "r",
    51: "s",
    54: "t",
    63: "u",
    71: "v",
    68: "w",
    70: "x",
    69: "y",
    49: "z",
    }

number_dict = {
    48: "1",
    50: "2",
    52: "3",
    53: "4",
    55: "5",
    60: "6",
    62: "7",
    64: "8",
    65: "9",
    67: "0"
}

symbol_dict = {
    48: "!",
    50: "@",
    52: "#",
    53: "$",
    55: "%",
    60: "^",
    62: "&",
    64: "*",
    65: "(",
    67: ")"
}

def get_single_note(letter_mode, shifted, note_num):
    if letter_mode and note_num in single_note_dict:
        return single_note_dict[note_num].capitalize() if shifted else single_note_dict[note_num]
    elif note_num in number_dict:
        return symbol_dict[note_num] if shifted else number_dict[note_num]
    return None

