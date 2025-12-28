"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Download a file via anonymous FTP using externalised settings.
"""

import ftplib
import settings.ftp as settings

ftp = ftplib.FTP(settings.FTP['URL'])
ftp.login()
ftp.cwd(settings.FTP["PATH"])
ftp.retrbinary(
    "RETR " + settings.FTP["FILENAME"],
    open(settings.FTP["FILENAME"], 'wb').write
)
ftp.quit()
