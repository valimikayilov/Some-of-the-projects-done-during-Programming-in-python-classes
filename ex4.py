"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 4
"""

#
# Start of code block that should not be modified.
#

# The next 3 lines will ask the user for input through the console and set the variables var1 and var2
# to the input the user typed in the console. These values will be of datatype string, so if you want to do
# numerical computations  with them, you will need to convert them to the datatype int or float. See the assignment
# sheet for more details.
datatype = input('Select a datatype (type "int", "float" or "string" and hit enter) for var1:')
var1 = input('Enter var1:')
var2 = input('Enter var2:')
result = None  # This variable should be overwritten with the result of your operation later.

#
# End of code block that should not be modified.
#

# Place your code here. Store the result in the variable "result".
#putting conditions for each value type
if datatype == 'int':
        v1 = int(var1)
elif datatype == 'float':
        v1 = float(var1)
elif datatype == 'string':
        v1 = var1
#setting up the var2 to an integer data type
v2= int(var2)
#multiplying the var 1&2 and assigning the value to result
result = v1*v2
#
# Do not modify the code below this line.
#

# This will print the result to the console.
print(f"Result: {result}")
