from glob import glob
import os

files = glob("*")

for file in files:
    new_file = file.split('.')
    new_file_name = new_file[0] + new_file[1] + '.apk'
    os.rename(file, new_file_name)
