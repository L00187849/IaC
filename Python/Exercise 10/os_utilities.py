"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    1) Detect the operating system.
    2) Return basic CPU metrics using psutil (if installed).
"""

import platform

# Optional dependency (will fail if psutil is not installed)
try:
    import psutil
except ImportError:
    psutil = None


def detect_os() -> str:
    """Detect the OS in use (e.g., Windows, Linux, Darwin)."""
    return platform.system()


def cpu_load() -> tuple[int, float]:
    """
    Return basic CPU metrics.

    Returns:
        (cpu_count, cpu_percent)

    Notes:
        - Requires psutil.
        - cpu_percent() returns a percentage over an interval; first call can be 0.0.
    """
    if psutil is None:
        raise ImportError("psutil is not installed. Run: python -m pip install psutil")

    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=None)
    return cpu_count, cpu_percent


if __name__ == "__main__":
    print(f"This module is called {__name__} and executes as a standalone script")

    my_os = detect_os().lower()
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    else:
        print(f"Unidentified system = {my_os}")

    # Quick test (only if psutil exists)
    try:
        print(f"CPU metrics: {cpu_load()}")
    except Exception as err:
        print(f"CPU test failed: {err}")
else:
    # Quiet when imported
    pass
