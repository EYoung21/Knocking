import keyboard
import time
import pyautogui
from threading import Thread

# Global variables to manage typing state and threading
knocking_active = False
knocking_thread = None
stop_knocking = False
knocking_delay = 0.1  # Delay between knocks

# Position for knocking (left side of the screen)
screen_width, screen_height = pyautogui.size()
knock_x = screen_width // 4
knock_y = screen_height // 4

def knock_on_door():
    global knocking_active, stop_knocking
    while knocking_active and not stop_knocking:
        # Hold down 'e' key
        keyboard.press('e')
        
        time.sleep(0.25)  # Simulate holding down 'e' key for 0.25 seconds
        
        # Move mouse to the knock position and click
        pyautogui.moveTo(knock_x, knock_y)
        pyautogui.click()
        
        # Release 'e' key
        keyboard.release('e')

        # Print knock message
        print("Knocked on the door.")

        # Delay before the next knock
        time.sleep(knocking_delay)

def toggle_knocking():
    global knocking_active, knocking_thread
    if knocking_active:
        # Pausing the knocking
        knocking_active = False
        print("Knocking paused.")
    else:
        # Start knocking
        knocking_active = True
        print("Starting knocking...")
        knocking_thread = Thread(target=knock_on_door)
        knocking_thread.start()

def stop_knocking_function():
    global stop_knocking
    stop_knocking = True  # Immediately stop knocking
    print("Knocking stopped.")

# Bind the start/stop knocking function to 'F2'
keyboard.add_hotkey('f2', toggle_knocking)

# Bind the "End" key to stop knocking
keyboard.add_hotkey('end', stop_knocking_function)

# Keep the script running
print("Press 'F2' to start/stop knocking on the door.")
print("Press 'End' to stop knocking.")
print("Press 'Esc' to exit the program.")
keyboard.wait('esc')
print("Program terminated.")
