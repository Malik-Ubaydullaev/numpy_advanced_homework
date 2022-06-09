import numpy as np

def sum_axis_1(arr: np.ndarray) -> int:
    """
    Returns the sum of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: sum of each row
    """
    
    return arr.sum(axis=0)

#arr = np.array([[ 1,  2,  3],
#       [ 4,  5,  6],
#       [ 7,  8,  9],
#       [10, 11, 0]])
#print(arr)
#Summa = sum_axis_1(arr)
#print(Summa)