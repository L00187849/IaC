"""
Name: Liam Saunders
Student Number: L00187849
Date: 20-OCT-2023
Version: 1.0
Purpose:
    Centralise important project paths using pathlib.
"""

from pathlib import Path

# The directory where this file lives (project root)
PROJECT_ROOT = Path(__file__).resolve().parent

# A specific settings file inside your project
UDP_SETTINGS = PROJECT_ROOT / "Network" / "settings" / "udp.py"

if __name__ == "__main__":
    # Quick diagnostic test
    print(f"PROJECT_ROOT = {PROJECT_ROOT}")
    print(f"UDP_SETTINGS  = {UDP_SETTINGS}")
    print(f"Exists?       = {UDP_SETTINGS.exists()}")
