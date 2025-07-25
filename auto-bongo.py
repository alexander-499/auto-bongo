import pyautogui
import threading
import time
import keyboard
import tkinter as tk

pyautogui.PAUSE = 0
keys = [ "a","b","c","d","e","f","g","h","i","j","k","l","m", "n","o","q","r","s","t","u","v","w","x","y","z", "0","1","2","3","4","5","6","7","8","9" ]

Interval = 0.01
key_to_press = "space"
toggle_key = "p"

running = False
lock = threading.Lock()

def auto_press():
  while True:
    with lock:
      if running:
        for key in keys:
          try:
            pyautogui.keyDown(key)
          except Exception as e:
            print(f"Error at {key} (keyDown): {e}")

        for key in keys:
          try:
            pyautogui.keyUp(key)
          except Exception as e:
            print(f"Error at {key} (keyUp): {e}")
        pyautogui.keyDown(key_to_press)
        pyautogui.keyUp(key_to_press)
    time.sleep(Interval)

def toggle_running():
  global running
  while True:
    keyboard.wait(toggle_key)
    with lock:
      running = not running
      print("Started" if running else "Stopped")

def exit_on_esc():
  keyboard.wait("esc")
  print("\nClosing Program...")
  root.destroy()
  root.quit()

root = tk.Tk()
root.withdraw()

threading.Thread(target=auto_press, daemon=True).start()
threading.Thread(target=toggle_running, daemon=True).start()
threading.Thread(target=exit_on_esc, daemon=True).start()

print(f"Press [{toggle_key}] to Start/Stop. Press [Esc] to close.")
root.mainloop()