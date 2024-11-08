from pynput.keyboard import Listener, Key
import pyautogui
import re
import time

recent_keys = []
pattern_detected = False
extracted_number = None


def on_press(key):
    global recent_keys

    try:

        if hasattr(key, 'char') and key.char is not None:
            recent_keys.append(key.char)
        elif key == Key.space:
            recent_keys.append(' ')
        elif key == Key.backspace:
            if recent_keys:
                recent_keys.pop()
    except AttributeError:
        pass

    if len(recent_keys) > 30:
        recent_keys.pop(0)


def on_release(key):
    global recent_keys, pattern_detected, extracted_number

    if key == Key.esc:

        return False

    if key == Key.shift_r:

        typed_string = ''.join(recent_keys)


        match = re.search(r"@allwp(\d+)", typed_string)
        if match:
            extracted_number = match.group(1)
            print(f"Pattern detected: @allwp{extracted_number}")
            tag_all(extracted_number)


        recent_keys.clear()
        
def tag_all(number):
    if number:
        pyautogui.typewrite(' ')
        for i in range(int(number) - 1):
            pyautogui.typewrite('@')
            time.sleep(0.1)
            pyautogui.press('Down')
            pyautogui.press('Enter')
    else:
        print("No valid number detected.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
