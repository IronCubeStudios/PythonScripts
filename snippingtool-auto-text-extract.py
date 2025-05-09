# pip install pyautogui keyboard pyperclip
import pyautogui
import keyboard
import time
import pyperclip

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort
pyautogui.PAUSE = 0.1  # Small pause between actions

# Store buttons in a list with their paths and confidence levels
buttons = [
    {"path": "assets/copyalltext.png", "confidence": 0.8, "name": "Copy All Text"},
    {"path": "assets/copyastable.png", "confidence": 0.8, "name": "Copy as Table"},
    {"path": "assets/textcopybutton.png", "confidence": 0.8, "name": "Text Copy"}
]

def activate_snipping_tool():
    """Activate or open Snipping Tool."""
    try:
        # Try to activate Snipping Tool window
        pyautogui.hotkey('win', 'shift', 's')  # Default Windows shortcut for Snipping Tool
        time.sleep(0.5)
        print("Snipping Tool activated")
        return True
    except Exception as e:
        print(f"Error activating Snipping Tool: {e}")
        return False

def automate_button_click(button):
    """Click a button on the screen if found."""
    try:
        button_location = pyautogui.locateOnScreen(
            button["path"], confidence=button["confidence"]
        )
        if button_location:
            pyautogui.click(pyautogui.center(button_location))
            print(f"Clicked button: {button['name']}")
            # Wait for clipboard content to update
            time.sleep(0.5)
            # Retrieve and print clipboard content
            clipboard_content = pyperclip.paste()
            if clipboard_content:
                print(f"Clipboard content: {clipboard_content[:100]}...")  # Print first 100 chars
            else:
                print("No content in clipboard")
        else:
            print(f"Button {button['name']} not found!")
    except Exception as e:
        print(f"Error clicking {button['name']}: {e}")

def stroke():
    """Monitor keyboard shortcuts and perform actions."""
    print("Running... Use the following shortcuts:")
    print("Alt+Ctrl+Shift+1: Copy all text")
    print("Alt+Ctrl+Shift+2: Copy as table")
    print("Alt+Ctrl+Shift+3: Copy text")
    print("Alt+Ctrl+Shift+Q: Quit program")

    while True:
        try:
            # Check for quit command
            if keyboard.is_pressed('alt+ctrl+shift+q'):
                print("Exiting program...")
                break

            # Ensure Snipping Tool is active before attempting button clicks
            if not pyautogui.getActiveWindow().title.lower().find("snipping tool") != -1:
                activate_snipping_tool()

            # Different key combinations for different buttons
            if keyboard.is_pressed('alt+ctrl+shift+1'):
                automate_button_click(buttons[0])  # Copy all text
                time.sleep(1)

            elif keyboard.is_pressed('alt+ctrl+shift+2'):
                automate_button_click(buttons[1])  # Copy as table
                time.sleep(1)

            elif keyboard.is_pressed('alt+ctrl+shift+3'):
                automate_button_click(buttons[2])  # Text copy
                time.sleep(1)

            time.sleep(0.1)  # Prevent CPU overuse

        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        # Give user time to prepare
        print("Starting in 3 seconds...")
        time.sleep(3)
        stroke()
    except KeyboardInterrupt:
        print("Program terminated by user")
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        print("Program ended")
        
        #test