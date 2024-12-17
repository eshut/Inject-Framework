"""Framework: https://github.com/eshut/Inject-Framework"""

import logging
from logging import LogRecord
import os
import time
import sys
from dotenv import load_dotenv

from framework_inject.constants import LOG_TIME_STRUCTURE

load_dotenv()
log_level = os.getenv("LOG_LEVEL")

class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.log_level = log_level
        self.logger = logging.getLogger("UnifiedLogger")
        self.logger.setLevel(logging.DEBUG)

        if not os.path.exists("logs"):
            os.mkdir("logs")

        log_time = time.strftime(LOG_TIME_STRUCTURE, time.localtime(time.time()))
        log_file = os.path.join("logs", f"log-{log_time}.log")

        if not self.logger.handlers:
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setLevel(self.log_level)

            ch = logging.StreamHandler()
            ch.setLevel(self.log_level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

        sys.excepthook = self.handle_exception

    def get_logger(self, name):
        """Return the logger instance with the given name."""
        return logging.getLogger(name)

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Handles uncaught exceptions."""
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        self.logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


class Logger:
    def __init__(self, logger_name):
        singleton_logger = SingletonLogger()
        self.logger = singleton_logger.logger

    def get_log(self):
        return self.logger

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
