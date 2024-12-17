import hashlib
import os


class SystemUtils:
    @staticmethod
    def sha1(input_string: str) -> str:
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        sha1_hash = hashlib.sha1(input_string.encode('utf-8')).hexdigest()
        return sha1_hash

    @staticmethod
    def cut_string(input_string, target_length):
        """
        Cuts a string to the specified length.

        Parameters:
            input_string (str): The string to cut.
            target_length (int): The desired length of the string.

        Returns:
            str: The cut string, no longer than the specified length.
        """
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string.")
        if not isinstance(target_length, int) or target_length < 0:
            raise ValueError("Target length must be a non-negative integer.")

        return input_string[:target_length]

    @staticmethod
    def write_to_file(file_path: str, content: str) -> None:
        """Write content to a file."""
        with open(file_path, "w") as f:
            f.write(content)

    @staticmethod
    def read_from_file(file_path: str) -> bool | str:
        """Read content from a file. Return None if file does not exist."""
        if not os.path.exists(file_path):
            return False
        with open(file_path, "r") as f:
            return f.read().strip()

