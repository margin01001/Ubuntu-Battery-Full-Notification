import subprocess as s
import psutil
import sys
import schedule
import time

def job():

    battery = psutil.sensors_battery()

    # print("Battery-Percentage: ", str(battery.percent))
    # s.call(['notify-send','battery full','may be 100%'])

    if battery is None:
        sys.exit("no battery is installed")

    battery_percentage = battery.percent

    print(battery_percentage)

    if battery_percentage > 94:
        s.call(['notify-send','Battery Full','Remove from power supply'])
    elif battery_percentage < 15:
        s.call(['notify-send', 'Battery', 'Battery is about to die plug in to power supply'])

schedule.every(10).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
