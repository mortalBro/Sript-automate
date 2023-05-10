####Atomatically shutdown system in a given time

import datetime
import os

now = datetime.datetime.now()

set_time_bro_hr=16
set_time_min_bro=24
shutdown_time = datetime.datetime(now.year, now.month, now.day, set_time_bro_hr, set_time_min_bro)

time_diff = (shutdown_time - now).total_seconds()

if time_diff > 0:
    print("Shutting down in", int(time_diff / 60), "minutes.")
    os.system(f'sudo shutdown -h {int(time_diff / 60)}')
else:
    print("Specified time has already passed.")
