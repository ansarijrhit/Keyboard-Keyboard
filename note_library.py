single_note_dict = {
    50: "a",
    52: "e",
    62: "i",
    67: "l", 
    53: "r",
    55: "t",

    }

def get_single_note(note_num):
    if note_num in single_note_dict:
        return single_note_dict[note_num]
    return None