"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate the use of Python's logging module to produce
    system-style log messages at different severity levels,
    including logging output to a timestamped logfile.
"""

import logging
from datetime import datetime

# --------------------------------------------------
# Create a timestamped log filename (YYYYMMDD-HHMMSS)
# --------------------------------------------------
now = datetime.now()
file_name = "%04d%02d%02d-%02d%02d%02d.log" % (
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
)

# --------------------------------------------------
# Configure logging
# --------------------------------------------------
logging.basicConfig(
    filename=file_name,
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Generate log messages at different levels
# --------------------------------------------------
logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print(f"Logging complete. Logfile created: {file_name}")
