"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 7
"""
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
    return (id,date,columns_split)
