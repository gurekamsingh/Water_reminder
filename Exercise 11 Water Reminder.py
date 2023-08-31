import time
from plyer import notification


def reminder():
    x = float(input("What time interval(in hours) do you need the reminder to display : "))
    while True:
        notification.notify("Reminder!", "Time to drink water", timeout=1)
        time.sleep(3600 * x)

reminder()