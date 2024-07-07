import pyautogui
import pydirectinput as key
import time
import random
import pytesseract
import keyboard
import sys

# (234,820),(382,850) = (234,820,382,850)// (260 832) .. x=256~364


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    time.sleep(1)
    pyautogui.hotkey("Alt", "Tab")
    pyautogui.hotkey("Esc")
    time.sleep(3)

    wheat()

    key.moveRel(100, 0)


def wheat():
    def move_right():
        t1 = time.time()
        key.keyDown('s')
        key.keyDown('d')
        while ((time.time() - t1) < 125):
            if checkStop() or checkPaused():
                sys.exit("stopping")
            continue
        key.keyUp('s')
        key.keyUp('d')

        time.sleep(random.randint(0, 4))
        return

    def move_left():
        t1 = time.time()
        key.keyDown('s')
        key.keyDown('a')
        while ((time.time() - t1) < 125):
            if checkStop() or checkPaused():
                sys.exit("stopping")
            continue
        key.keyUp('s')
        key.keyUp('a')

        time.sleep(random.randint(0, 4))
        return

    for i in range(2):
        move_left()
        move_right()
    move_left()
    time.sleep(5)


def checkPaused():
    screenshot = pyautogui.screenshot()

    # set to only the portion that display pause
    screenshot = pyautogui.screenshot()
    roi = (234, 820, 364, 850)
    crop_screenshot = screenshot.crop(roi)

    # config 8 is image as a single word
    custom_config = r'--psm 8'
    detected_text = pytesseract.image_to_string(
        crop_screenshot, lang='eng', config=custom_config)

    # Specify the text you are looking for
    target_text = "PAUSED"

    # Check if the target text is present in the detected text
    if target_text in detected_text:
        print(f"Detected '{target_text}' on screen.")
        return True
    else:
        print(f"'{target_text}' not found on screen.")
        return False


def BackToSB():
    for char in "/skyblock":
        key.keyDown(char)
        time.sleep(time.delay[random.randint(0, 4)])
        key.keyUp(char)

    key.keyDown('enter')
    time.sleep(0.1)
    key.keyUp('enter')


def checkStop():
    if keyboard.is_pressed('t'):
        return True
    return False


if __name__ == "__main__":
    main()
