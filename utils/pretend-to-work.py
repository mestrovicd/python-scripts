import pyautogui
import time

def move_mouse(duration_hours):
    end_time = time.time() + duration_hours * 3600
    while time.time() < end_time:
        try:
            for _ in range(3):
                pyautogui.moveRel(10, 0, duration=1)
                pyautogui.moveRel(-10, 0, duration=1)
            time.sleep(57)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    time_in_hours = float(input("Enter the duration in hours: "))
    move_mouse(time_in_hours)
