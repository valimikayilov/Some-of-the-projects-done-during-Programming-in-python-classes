"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 3
"""

import os
import glob
from PIL import Image
import numpy as np

class ImageNormalizer:
    def __init__(self, input_dir):
        files = []
        inp_dir = os.path.abspath(input_dir)
        found_files = glob.glob(os.path.join(inp_dir, '**', '*.jpg'), recursive=True)
        found_files.sort()
        self.found_files = found_files
        for file in found_files:
            files.append(os.path.relpath(file, input_dir))
        self.file_paths = files
        self.n_file_paths = len(files)
        self.mean = None
        self.std = None
    def analyze_images(self):
        self.stds = []
        self.means = []
        for x in self.found_files:
            img = Image.open(x)
            numpyimage = np.asarray(img)
            float64 = np.array(numpyimage, dtype=np.float64)
            self.stds.append(np.std(float64))
            self.means.append(np.mean(float64))
        av_mean = sum(self.means)/len(self.means)
        av_std = sum(self.stds)/len(self.stds)
        self.mean = np.float64(av_mean)
        self.std = np.float64(av_std)
        return (self.mean, self.std)
    def get_images_data(self):
        if  self.mean == None or self.std == None:
            raise ValueError(f"mean or std is none")
        for img in self.found_files:
            loaded = Image.open(img)
            numpyimage = np.asarray(loaded)
            float32 = np.array(numpyimage, dtype=np.float32)
            float32 = (float32 - self.mean)/self.std
            yield float32
