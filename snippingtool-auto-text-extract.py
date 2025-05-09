# pip install pyautogui keyboard
import pyautogui
import keyboard
import time

# Store buttons in a list instead of a set for indexed access
buttons = [
    "assets/copyalltext.png",
    "assets/copyastable.png",
    "assets/textcopybutton.png"
]

def automate_button_click(button_path):
    try:
        button_location = pyautogui.locateOnScreen(button_path)
        if button_location:
            pyautogui.click(pyautogui.center(button_location))
            print(f"Clicked button: {button_path}")
        else:
            print(f"Button {button_path} not found!")
    except Exception as e:
        print(f"Error: {e}")

def stroke():
    while True:
        # Different key combinations for different buttons
        if keyboard.is_pressed('alt+ctrl+shift+1'):
            automate_button_click(buttons[0])  # copyalltext
            time.sleep(1)
            
        elif keyboard.is_pressed('alt+ctrl+shift+2'):
            automate_button_click(buttons[1])  # copyastable
            time.sleep(1)
            
        elif keyboard.is_pressed('alt+ctrl+shift+3'):
            automate_button_click(buttons[2])  # textcopybutton
            time.sleep(1)

if __name__ == "__main__":
    print("Running... Use the following shortcuts:")
    print("Alt+Ctrl+Shift+1: Copy all text")
    print("Alt+Ctrl+Shift+2: Copy as table")
    print("Alt+Ctrl+Shift+3: Copy text")
    stroke() #test