import mido
import time
import note_library

def main():
    inport = mido.open_input()
    
    print("Listening")
    while True:
        message = inport.receive()
        if message:
            print(process_input(message), end = '', flush=True)

shifted = False
letter_mode = True
t1 = 0
t2 = 1
note1 = 0
note2 = 100
on_t1 = True

def process_input(message):
    global shifted, letter_mode, t1, t2, on_t1, note1, note2
    if message.type == "control_change" and (message.control == 72 or message.control == 64):
        shifted = not shifted
    elif message.type == "note_on":
        if message.note == 45:
            letter_mode = not letter_mode
        else:
            if on_t1:
                t1 = time.time()
                note1 = message.note
                on_t1 = False
            else:
                t2 = time.time()
                note2 = message.note
                on_t1 = True
            if abs(t2 - t1) <= .05 and (note1 == 60 or note2 == 60 or note1 == 48 or note2 == 48):
                return note_library.get_note_diff(note1, note2)
            return note_library.get_single_note(letter_mode, shifted, note1 if on_t1 else note2)
    return ""

main()