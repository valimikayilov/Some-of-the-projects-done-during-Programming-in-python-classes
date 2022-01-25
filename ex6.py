"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 6
"""

import glob
import os

def get_hamsters(folderpath):
    found_files = glob.glob(os.path.join(folderpath, '**', '*.raw.seq'), recursive=True)
    found_files = sorted(found_files)
    for x in found_files:
        with open(x, 'r') as f:
            file_content = f.read()
            filename = os.path.basename(x)
            yield filename, file_content
