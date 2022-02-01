import os
from time import localtime, asctime

dir_name = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_name, 'requests_logs')

for root, directories, files in os.walk(path, topdown=True):
    i = 0
    for name in files:
        time_stamp = float(name[:-4])
        # print(time_stamp, f'\t{time.gmtime(float(time_stamp))}')
        print(time_stamp, f'\t{asctime(localtime(time_stamp))}')
        i += 1

print(i)
