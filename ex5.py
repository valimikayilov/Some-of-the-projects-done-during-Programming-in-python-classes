"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 5
"""

import re
filename = "data_00-000.raw.seq"
with open(filename, 'r') as fh:
    data_as_string = fh.read()
subsequence='AT'
def count_bases_and_subsequence(data_as_string, subsequence):
    a_counter = 0
    c_counter = 0
    g_counter = 0
    t_counter = 0
    arr = []
    arrjn = ''
    file = data_as_string.splitlines()
    for x in file:
        if str(x) == '% End of data':
            break
        if x == '' or re.match('[%]', x):
            arr.append('%')
        if re.match('^[a-zA-Z]+', x) is not None:
            arrsl = x.split(";")
            if float(arrsl[2]) >= 0.08:
                arr.append(arrsl[1])
            # counts the instances of A and a with a value higher than 0.08
            if arrsl[1] == 'A' or arrsl[1] == 'a':
                if float(arrsl[2]) >= 0.08:
                    a_counter = a_counter + 1
            # counts the instances of C and c with a value higher than 0.08
            if arrsl[1] == 'C' or arrsl[1] == 'c':
                if float(arrsl[2]) >= 0.08:
                    c_counter = c_counter + 1
            # counts the instances of G and g with a value higher than 0.08
            if arrsl[1] == 'G' or arrsl[1] == 'g':
                if float(arrsl[2]) >= 0.08:
                    g_counter = g_counter + 1
            # counts the instances of T and t with a value higher than 0.08
            if arrsl[1] == 'T' or arrsl[1] == 't':
                if float(arrsl[2]) >= 0.08:
                    t_counter = t_counter + 1

    occurances={
    'a': a_counter,
    'c': c_counter,
    'g': g_counter,
    't': t_counter
    }
    arrjn = ''.join(arr)
    arrjn2 = arrjn.upper()
    subsequence2 = subsequence.upper()
    counter_sub = arrjn2.count(subsequence2)
    result = (counter_sub, occurances)
    return result

count_bases_and_subsequence(data_as_string, subsequence)
