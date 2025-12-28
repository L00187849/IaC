import ftplib

FTP = {
    "PATH": '/mirrors/ubuntu-cdimage/releases/22.04/release',
    "FILENAME": 'SHA256SUMS',
    "URL": 'ftp.heanet.ie'
}

ftp = ftplib.FTP(FTP['URL'])
ftp.login()
ftp.cwd(FTP["PATH"])
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()
