import webbrowser
import ctypes
import time
import random
import string

def automate_process(num_repeats):
    # URL to open
    url = 'https://roblox.com/redeem'

    for _ in range(num_repeats):
        # Open the URL in a new browser window
        webbrowser.open_new(url)

        # Set the coordinates (x, y)
        x, y = 400, 345

        # Move the mouse
        time.sleep(1)
        ctypes.windll.user32.SetCursorPos(x, y)

        # Perform a left click
        time.sleep(0.1)
        mouse_event = ctypes.windll.user32.mouse_event
        mouse_event(2, 0, 0, 0,0) # left button down
        mouse_event(4, 0, 0, 0,0) # left button up

        # Generate a random 18-character alphanumeric string
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=18))

        # Type the string
        for c in code:
            # Press the key
            ctypes.windll.user32.keybd_event(ord(c.upper()), 0, 0, 0)
            # Release the key
            ctypes.windll.user32.keybd_event(ord(c.upper()), 0, 2, 0)
            # Wait a bit between keystrokes to prevent them from being missed
            time.sleep(0.01)

        # Set the new coordinates (x, y)
        x, y = 175, 400

        # Move the mouse to the new coordinates
        time.sleep(0.5)
        ctypes.windll.user32.SetCursorPos(x, y)

        # Perform a left click at the new coordinates
        time.sleep(0.1)
        mouse_event = ctypes.windll.user32.mouse_event
        mouse_event(2, 0, 0, 0,0) # left button down
        mouse_event(4, 0, 0, 0,0) # left button up

        # Set the new coordinates (x, y)
        x, y = 500, 640

        # Move the mouse to the new coordinates
        time.sleep(0.1)
        ctypes.windll.user32.SetCursorPos(x, y)

        # Perform a left click at the new coordinates
        time.sleep(0.1)
        mouse_event = ctypes.windll.user32.mouse_event
        mouse_event(2, 0, 0, 0,0) # left button down
        mouse_event(4, 0, 0, 0,0) # left button up

        time.sleep(1)

        # Close the tab
        ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # Ctrl key down
        ctypes.windll.user32.keybd_event(0x57, 0, 0, 0)  # W key down
        ctypes.windll.user32.keybd_event(0x57, 0, 2, 0)  # W key up
        ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)  # Ctrl key up

if __name__ == "__main__":
    print(r"""
 _             _                                                           _
| |__    ___  | |__   _   _ __  __   __ _   ___  _ __    ___  _ __   __ _ | |_   ___   _ __
| '_ \  / _ \ | '_ \ | | | |\ \/ /  / _` | / _ \| '_ \  / _ \| '__| / _` || __| / _ \ | '__|
| |_) || (_) || |_) || |_| | >  <  | (_| ||  __/| | | ||  __/| |   | (_| || |_ | (_) || |
|_.__/  \___/ |_.__/  \__,_|/_/\_\  \__, | \___||_| |_| \___||_|    \__,_| \__| \___/ |_|
                                    |___/ 
    """)
    num_repeats = int(input("Enter the number of repeats: "))
    start = input("Do you want to start the process? (y/n): ")
    if start.lower() == 'y':
        automate_process(num_repeats)
