import mido
import time
import note_library

inport = mido.open_input()

print("Listening")
while True:
    message = inport.receive()
    if message:
        if message.type == "note_on":
            print(note_library.get_single_note(message.note), message.note)