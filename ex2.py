"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 2
"""

import sys
import os
import glob
import shutil
import imghdr
from PIL import Image
from PIL import ImageStat
import imagehash
from scipy import ndimage
import numpy as np


def ex2(inp_dir,out_dir,logfile):
    hashes_of_images = []
    i = 0
    inp_dir = os.path.abspath(inp_dir)
    found_files = glob.glob(os.path.join(inp_dir, '**', '*'), recursive=True)
    found_files.sort()
    os.makedirs(out_dir, exist_ok=True)
    for file in found_files:
        if not os.path.splitext(file)[1] == r'.jpg' and not os.path.splitext(file)[1] == r'.JPG' and not os.path.splitext(file)[1] == r'.jpeg' and not os.path.splitext(file)[1] == r'.JPEG':
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+';1\n')
            continue

        if os.path.getsize(file) <= 10000:
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+';2\n')
            continue

        if not imghdr.what(file)==r'jpeg':
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+';3\n')
            continue

        im = Image.open(file)
        width, height = im.size
        if width < 100 or height < 100 or len(ImageStat.Stat(im).var) >= 2:
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+';4\n')
            continue

        if ImageStat.Stat(im).var[0] <= 0:
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+';5\n')
            continue
        hash = imagehash.average_hash(Image.open(file))
        hash = str(hash)
        if hash in hashes_of_images:
            with open(logfile, 'a') as f:
                f.write(os.path.relpath(file, inp_dir)+ ';6\n')
            continue
        hashes_of_images.append(hash)
        shutil.copy(file, out_dir)
        os.rename(os.path.join(out_dir, os.path.basename(file)), os.path.join(out_dir, '{0:07}'.format(i)+'.jpg'))
        i = i + 1
    return i


#python ex2.py "C:\Users\Vello\Desktop\Programming in Python 2\ex2\unittests\unittest_input_3\f_2" "C:\Users\Vello\Desktop" "C:\Users\Vello\Desktop\logfile.log"
