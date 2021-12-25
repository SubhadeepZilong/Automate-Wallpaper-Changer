# ---------- Packages -----------


import os
from os.path import isfile, join
import ctypes
import time


# ------------ Start Execution -------------

# Folder path
folderpath = os.getcwd() + r"\images"

# Adding all available files in a list
all_files = [ f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]

# Setting the wallpaper
for image in all_files:
    # Check the folder
    print(folderpath+ "\\" + image)
    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, (folderpath+ "\\" + image), 0)
    # Set Interval
    time.sleep(1)
