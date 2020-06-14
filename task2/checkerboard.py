import numpy as np
from PIL import Image


def checkerboard(shape1, shape2, n):
    row_index = shape1 * 100
    col_index = shape2 * 100
    array = np.array([[((index[0] // 100 + index[1] // 100) % n)*255, 0, 0] for index in
                      np.ndindex(row_index, col_index)], dtype=np.uint8)
    array = array.reshape(row_index, col_index, 3)
    '''row_index = shape1*100
    col_index = shape2*100
    array = np.zeros((row_index, col_index, 3), dtype=np.uint8)
    for row in range(0, row_index):
        for col in range(0, col_index):
            if (row//100 + col//100) % n == 1:
                array[row, col] = [255, 0, 0]'''
    return array


data = checkerboard(8, 8, 2)
img = Image.fromarray(data, 'RGB')
img.save("new.png")
img.show()
