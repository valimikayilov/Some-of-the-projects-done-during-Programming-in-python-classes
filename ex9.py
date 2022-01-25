"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 9
"""
import pandas as pd
from matplotlib import pyplot as plt
import os
import sys
import subprocess

command_line_args = sys.argv
output_folder = command_line_args[1]
os.mkdir(output_folder)
path = os.path.join(output_folder, '200')
os.mkdir(path)
subprocess.call([sys.executable,'hamstergenegen.py', path])
file = os.path.join(output_folder, 'patterns_analysis.csv')
subprocess.call([sys.executable,'ex8.py', path, file, 'ctag'])
subprocess.call([sys.executable,'plot_csv.py', output_folder])

command_line_args = sys.argv
def plot_csv(inputfilename: str, outputfilename: str):
    data = pd.read_csv(inputfilename, sep=' ')
    fig, ax = plt.subplots()
    for label in data.columns:
        if label == 'subsequence':
            ax.plot(data[label]*100, label=label+" x100")
        else:
            ax.plot(data[label], label=label)
    ax.set(xlabel='time (days)', ylabel='counts',
           title='Base and subsequence counts')
    ax.grid()
    plt.legend()
    fig.savefig(outputfilename)
    plt.close(fig)
    del fig
input = os.path.join(output_folder, 'patterns_analysis.csv')
output = os.path.join(output_folder, 'patterns_analysis.png')

if __name__ == '__main__':
    # Example usage:
    plot_csv(inputfilename = input, outputfilename = output)
