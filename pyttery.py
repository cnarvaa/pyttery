import os
import sys
import time

import plyer
from psutil import sensors_battery

minute = 60  # seconds
percentage_trigger = 95


def notify():
    plyer.notification.notify(
        title='Hey!, Unplug your battery!',
        message='Your battery is already charged',
        app_name='Pyttery',
        app_icon=None,
        timeout=10,  # seconds
    )


if __name__ == "__main__":
    while True:
        battery = sensors_battery()
        percent = battery.percent
        power_plugged = battery.power_plugged

        if percent > percentage_trigger and power_plugged:
            notify()

        time.sleep(minute*5)
