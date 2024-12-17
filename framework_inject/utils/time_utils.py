from datetime import datetime
from framework_inject.constants import DEFAULT_WAIT_TIME_SEC
from constants import DEFAULT_TIME_LOG_STRUCTURE, DEFAULT_TIME_FORMAT
import time


class TimeUtils:
    @staticmethod
    def get_time_log(structure=DEFAULT_TIME_LOG_STRUCTURE):
        return time.strftime(structure, time.localtime(time.time()))

    @staticmethod
    def get_time_now(format=DEFAULT_TIME_FORMAT):
        return datetime.now().strftime(format)

    @staticmethod
    def wait_time(sec=DEFAULT_WAIT_TIME_SEC):
        time.sleep(sec)

    @staticmethod
    def wait_random_time(min_time, max_time):
        if min_time < 0 or max_time < 0:
            raise ValueError("Time values must be non-negative.")
        if min_time > max_time:
            raise ValueError("min_time must not be greater than max_time.")

        wait_time = random.uniform(min_time, max_time)
        time.sleep(wait_time)
