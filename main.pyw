from plyer import notification
from psutil import sensors_battery


def notify():
    notification.notify(
        title='Hey!, Unplug your battery!',
        message='Your battery is charged',
        app_name='Pyttery',
        app_icon=None,
        timeout=10,  # seconds
    )


if __name__ == "__main__":

    battery = sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged

    if percent > 50 and power_plugged:
        notify()
