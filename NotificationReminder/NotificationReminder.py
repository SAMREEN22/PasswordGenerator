import time
from plyer import notification
if __name__=='__main__':
    while True:
        notification.notify(
            title="Today's Reminder",
            message="Assignment due",
            timeout=10
        )
        time.sleep(10)