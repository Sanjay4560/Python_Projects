from plyer import notification
import time
if __name__ == "__main__":
    while True:
        notification.notify(
        title = "*** Please! Drink Water***",
        message = "Keeping hydrated is crucial for health and well-being",
        # app_icon = "c:\Users\Sanjay\Desktop\Implementation\icon.icon",
        timeout = 5
    )
    time.sleep(10)

    
    