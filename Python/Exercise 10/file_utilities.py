"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Provide OS-aware logfile directory.
    2) Generate timestamp-based logfile names.
"""

from datetime import datetime as dt
import sys
import os


def path_name() -> str:
    """
    Return an OS-aware logfile directory.
    Creates the directory if it doesn't exist.
    """
    this_os = sys.platform

    if this_os == "win32":
        log_dir = "./logfiles/"
    elif this_os.startswith("linux"):
        log_dir = "./logfiles/"
    else:
        raise OSError(f"Unsupported OS: {this_os}")

    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def log_file_name(extension: str) -> str:
    """
    Create a timestamp filename (YYYYMMDD-HHMMSS) + extension.
    """
    now = dt.now()
    stamp = "%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d" % (
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
    )
    return stamp + extension


if __name__ == "__main__":
    print(f"This module is called {__name__} and executes as a standalone script")
    log_path = path_name()
    filename = log_file_name(".log")
    print(log_path + filename)
else:
    pass
