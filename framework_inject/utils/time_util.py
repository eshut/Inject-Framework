"""Framework: https://github.com/eshut/Inject-Framework"""

import time
import random
from framework_inject.constants import DEFAULT_WAIT_TIME_SEC


def wait_time(sec=DEFAULT_WAIT_TIME_SEC):
    time.sleep(sec)


def wait_random_time(min_time, max_time):
    if min_time < 0 or max_time < 0:
        raise ValueError("Time values must be non-negative.")
    if min_time > max_time:
        raise ValueError("min_time must not be greater than max_time.")

    wait_time = random.uniform(min_time, max_time)
    time.sleep(wait_time)
