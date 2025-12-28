"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Download the Ubuntu SHA256SUMS file over HTTPS (FTP mirror may be unavailable).
"""

from urllib.request import urlretrieve

URL = "https://old-releases.ubuntu.com/releases/22.04/source/SHA256SUMS"
FILENAME = "SHA256SUMS"

print(f"Downloading {FILENAME}...")
urlretrieve(URL, FILENAME)
print(f"Saved as: {FILENAME}")
