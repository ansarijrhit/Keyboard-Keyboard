import mido
import time
import note_library

def main():
    inport = mido.open_input()

    print("Listening")
    while True:
        message = inport.receive()
        if message:
            print(process_input(message))

shifted = False
letter_mode = True
def process_input(message):
    global shifted, letter_mode
    if message.type == "control_change" and message.control == 72:
        shifted = not shifted
    elif message.type == "note_on":
        if message.note == 45:
            letter_mode = not letter_mode
        else:
            return note_library.get_single_note(letter_mode, shifted, message.note)
    return ""

main()