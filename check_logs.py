import os
from time import localtime, asctime

dir_name = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_name, 'quotes')
quote_list = []

for root, directories, files in os.walk(path, topdown=True):
    for name in files:
        time_stamp = float(name[:-4])
        quote_list.append(time_stamp)

quote_list.sort()

for time_stamp in quote_list:
    print(time_stamp, f'\t{asctime(localtime(time_stamp))}')

print(len(quote_list))
