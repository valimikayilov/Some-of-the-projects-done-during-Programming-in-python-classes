"""
Author: Vali Mikayilov
Matr.Nr.: K12037083
Exercise 4
"""

import numpy as np



def ex4(image_array, border_x, border_y):
    #Errors:
    if type(image_array) is not np.ndarray:
        raise NotImplementedError(f"not a numpy array")
    if image_array.ndim != 2:
        raise NotImplementedError(f"not 2D")
    try:
        int(border_x[0])
        int(border_x[1])
        int(border_y[0])
        int(border_y[1])
    except ValueError:
        print(f"not convertible to int!")
    if int(border_x[0]) < 1 or int(border_y[0]) < 1 or int(border_x[1]) < 1 or int(border_y[1]) < 1:
        raise ValueError(f"mean or std is none")

    x1 = int(border_x[0])
    x2 = int(border_x[1])
    y1 = int(border_y[0])
    y2 = int(border_y[1])
    l1 = len(image_array)
    l2 = len(image_array[0])

    #input_array
    input_array = np.copy(image_array)
    input_array[:, 0:x1] = 0
    input_array[:, l2-x2:l2] = 0
    input_array[0:y1, :] = 0
    input_array[l1-y2:l1, :] = 0

    #known_array
    known_array = np.copy(image_array)
    known_array[:, 0:x1] = 0
    known_array[:, l2 - x2:l2] = 0
    known_array[0:y1, :] = 0
    known_array[l1 - y2:l1, :] = 0
    known_array[x1:l2-x2, y1:l1-y2] = 1

    #target_array
    #image = np.copy(image_array)
    #bool_known = known_array.astype(bool)

    image = np.copy(image_array)
    bool_known = image.astype(np.bool)
    target_array = image[bool_known]
    if target_array.shape[0] < 256:
        raise ValueError(f"less than 16")

    return (input_array, known_array, target_array)