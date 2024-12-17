"""Framework: https://github.com/eshut/Inject-Framework"""


from typing import Any


class Context:
    """
    A class to store shared values across PageObjects.
    Supports dictionary-like access for getting and setting values.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Context, cls).__new__(cls)
            # Initialize context data here
            cls._instance.data = {}
        return cls._instance

    def __init__(self):
        self._data = {}

    def __setitem__(self, key: str, value: Any) -> None:
        """Set a value in the context using dictionary-like syntax."""
        self._data[key] = value

    def __getitem__(self, key: str) -> Any:
        """Retrieve a value from the context using dictionary-like syntax."""
        if key not in self._data:
            raise KeyError(f"'{key}' not found in context")
        return self._data[key]

    def __contains__(self, key: str) -> bool:
        """Check if a key exists in the context."""
        return key in self._data

    def __repr__(self):
        return f"Context({self._data})"
