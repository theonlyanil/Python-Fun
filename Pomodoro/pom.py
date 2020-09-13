# TODO incomplete

import time
starttime = time.time()
time_elapsed = float(input('Time in Minutes: '))


def something():
    while True:
        current_time = time.strftime('%I:%M:%S', time.localtime())
        print(current_time)
        time.sleep((time_elapsed * 60) - ((time.time() - starttime) % (time_elapsed * 60)))
