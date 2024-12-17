import csv
import os
from utils.time_utils import TimeUtils
from logger.logger import Logger


class CSVUtil(Logger):
    def __init__(self, base_dir="logs/csv_files", logger=__file__):
        super().__init__(logger)
        self.time_util = TimeUtils()
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.logger.debug(f"CSV directory initialized: {self.base_dir}")
        self.file_path = None

    def generate_filename(self, prefix="data"):
        timestamp = self.time_util.get_time_now()
        filename = f"{prefix}_{timestamp}.csv"
        self.file_path = os.path.join(self.base_dir, filename)
        self.logger.debug(f"Generated filename: {self.file_path}")
        return self.file_path

    def write_csv(self, data, headers=None):
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if headers:
                    writer.writerow(headers)
                elif data and isinstance(data[0], dict):
                    headers = list(data[0].keys())
                    writer.writerow(headers)
            self.logger.debug(f"CSV file written successfully: {self.file_path}")
        except Exception as e:
            self.logger.error(f"Error writing CSV file: {e}")

    def append_to_csv(self, data):
        try:
            with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row.values() if isinstance(row, dict) else row)
            self.logger.debug(f"Data appended to CSV file successfully: {self.file_path}")
        except Exception as e:
            self.logger.error(f"Error appending to CSV file: {e}")

    def update_log_structure(self, log_structure, **kwargs):
        for key, value in kwargs.items():
            if key in log_structure[0]:  # Only update existing keys
                log_structure[0][key] = value
        return log_structure
