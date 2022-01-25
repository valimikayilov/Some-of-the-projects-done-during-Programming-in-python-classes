"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 8
"""

import numpy as np
import pandas as pd
import sys

def count_bases_and_subsequence(data_as_string, subsequence):

    # We can convert the subsequence string to lower case letters to make the
    # subsequence count case insensitive:
    subsequence = subsequence.lower()  # this converts everything to lower case

    # We could also convert data_as_string to lower case but this is less
    # memory efficient (we would duplicate the whole string in memory), so we
    # will use a different approach later.

    # Split file content string into lines
    lines = data_as_string.split("\n")  # alternative: data_as_string.splitlines()

    # Dictionary to store the counts of individual bases in
    counts = dict(a=0, c=0, g=0, t=0)

    # Our counter for the subsequence
    subsequence_count = 0

    # Split the subsequence string to a list where each element is a character
    subsequence_list = list(subsequence)

    # Create a dummy-list which we will later fill with the most recent bases
    # to compare with subsequence_list. We will use None to initialize the
    # list elements. Later we will add None as element instead of a base if
    # the line is invalid.
    recent_bases_list = [None] * len(subsequence_list)

    # Iterate over all lines
    for line in lines:
        if line == "% End of data":  # End of data reached?
            # If end of data is reached, escape from loop
            break
        elif (len(line) == 0) or line.startswith('%'):  # Invalid data line?
            # Add None to the end and remove first element for subsequence
            # comparison:
            recent_bases_list = recent_bases_list[1:] + [None]
            # If empty line or comment line, skip to next line
            continue

        # Get values of columns in this line:
        info, base, quality = line.split(";")

        if float(quality) < 0.08:  # Quality too low?
            # Add None to the end and remove first element for subsequence
            # comparison:
            recent_bases_list = recent_bases_list[1:] + [None]
            # If quality < 0.05, skip to next line
            continue

        # Remove leading and trailing whitespace characters, just in case
        base = base.strip()

        # Make sure we are case insensitive
        base = base.lower()

        # We could use if-elif-else conditions here to increase count-variables
        # for the individual bases. But since we use a dictionary for the
        # counts, we can just use the base itself as key:
        try:
            # Increase counter for the specific base
            counts[base] += 1
            # Add the base to the end and remove first element
            recent_bases_list = recent_bases_list[1:] + [base]
        except KeyError:  # Current Base does not exist in our dictionary keys
            # Add None to the end and remove first element for subsequence
            recent_bases_list = recent_bases_list[1:] + [None]
            # If the base entry was not in our dictionary keys, go to the next line
            continue

        # If the recent bases match the subsequence, we increase the
        # subsequence count by 1:
        if recent_bases_list == subsequence_list:
            subsequence_count += 1
            # Add None as last list character to avoid over-lapping matches
            # (this is not relevant for the grading but makes more sense in
            # this setting)
            recent_bases_list = recent_bases_list[1:] + [None]

    # Return the counts
    return [subsequence_count, counts["a"],counts["c"],counts["g"],counts["t"]]
#ex5.py end
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
#ex6.py end
import re
matches = ["% SeqHeadStart", "% SeqHeadEnd", "% End of data"]
matches_rest = ['ID:', 'Date:','Columns:']
def  get_file_metadata(data_as_string):
    split_data = data_as_string.split('\n')
    enum_data = enumerate(split_data,0)
    #set the value of the % SeqHeadEnd to a and % End of data to b
    for x in enum_data:
        if x[1] == '% SeqHeadStart':
            a = x[0]
        if x[1] == '% SeqHeadEnd':
            b = x[0]
        if x[1] == '% End of data':
            c = x[0]
    #if the value has all the matches and End of data doesn't come after SeqHead then return an error
    if not all(x in data_as_string for x in matches):
        raise AttributeError(f"the data doesn't contain % SeqHeadStart, % SeqHeadEnd, % End of data")
    if c<b:
        raise AttributeError(f" the End of data doesn't come after SeqHead")
    if b<a:
        raise AttributeError(f" the SeqEnd doesn't come after SeqHead")
    header_slice = slice(0,b+1)
    header = split_data[header_slice]
    # raise attribute error if matches are not found
    if not all(x in data_as_string for x in matches_rest):
        raise AttributeError(f"AttributeError")
    #ID, date and column name
    id = re.findall(r'ID: (\S+)', data_as_string)[0]
    #raise error if the date is incorrect
    try:
        date = int(re.findall(r'Date: (\d+)', data_as_string)[0])
    except (IndexError) as ex:
        raise TypeError(f"TypeError this one")
    else:
        date = int(re.findall(r'Date: (\d+)', data_as_string)[0])
    columns = re.findall(r'Columns: (\S+)', data_as_string)[0]
    columns_split = columns.split(';')

    for x in header:
        if not x.startswith('%') and not x == '':
            raise AttributeError(f"AttributeError")
    return [id,date]

x=0
command_line_args = sys.argv
input_folder = command_line_args[1]
output_file = command_line_args[2]
subsequence = command_line_args[3]
file_reader = get_hamsters(input_folder)
arr = np.zeros(shape=(200, 5), dtype=np.float)
f = open(output_file, "a")
for filename, file_content in file_reader:
        data_as_string = file_content
        meta_data = get_file_metadata(data_as_string)
        i = meta_data[1]
        base_count = count_bases_and_subsequence(data_as_string,subsequence)
        arr[i][0] = arr[i][0] + float((base_count[0])/20)
        arr[i][1] = arr[i][1] + float((base_count[1])/20)
        arr[i][2] = arr[i][2] + float((base_count[2])/20)
        arr[i][3] = arr[i][3] + float((base_count[3])/20)
        arr[i][4] = arr[i][4] + float((base_count[4])/20)

pd.DataFrame(arr).to_csv(output_file, header=['subsequence', 'a', 'c','g','t'], index=None, sep=' ')
