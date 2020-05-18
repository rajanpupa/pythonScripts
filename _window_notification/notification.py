import time
from plyer import notification

# This program Give a message every 10 seconds. and lasts for 10 seconds on the screen
# app_icon
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "* Please Drint water Now!!! ",
            message = "Some useful information about why drinking water is important",
            timeout = 10
        )
        time.sleep(10);