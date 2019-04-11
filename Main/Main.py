import os
import time

source = '"D:\ces"'
target_dir = '"D:\target"'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Backup added to', target)
else:
    print('Backup failed')
