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
    46: "k",
    66: "l",
    55: "m",
    62: "n",
    65: "o",
    61: "p",
    51: "s",
    53: "r",
    54: "t",
    63: "u",
    68: "w",
    69: "y",
    49: "z",
    }
# Missing: J, Q, V, X

def get_single_note(note_num):
    if note_num in single_note_dict:
        return single_note_dict[note_num]
    return None

