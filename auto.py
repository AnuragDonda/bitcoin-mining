import pyautogui
import time

# Define the list of keyboard shortcuts to switch between applications
shortcuts = ['alt', 'tab']

while True:
    try:
        # Send the keyboard shortcuts to switch applications
        pyautogui.hotkey(*shortcuts)

        # Wait for 2-3 minutes (adjust the sleep duration as needed)
        time.sleep(60)  # Sleep for 3 minutes
    except KeyboardInterrupt:
        # Exit the script if you manually interrupt it (e.g., with Ctrl+C)
        break
