import os,sys

import ftplib

print('helloworld')

PUREUDON_FTP_HOST = os.getenv('PUREUDON_FTP_HOST')
PUREUDON_FTP_PASSWORD = os.getenv('PUREUDON_FTP_PASSWORD')
PUREUDON_FTP_USERNAME = os.getenv('PUREUDON_FTP_USERNAME')
PUREUDON_HOMEPAGE_PATH = os.getenv('PUREUDON_HOMEPAGE_PATH')

session = ftplib.FTP(PUREUDON_FTP_HOST,PUREUDON_FTP_USERNAME,PUREUDON_FTP_PASSWORD)
file = open('index.html','rb')                  # file to send
session.storbinary('STOR index.html', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
print('helloworld')
