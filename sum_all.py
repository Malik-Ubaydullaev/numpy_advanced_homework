import numpy as np

def sum_all(arr: np.ndarray) -> int:
    """
    Returns the sum of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: sum of all numbers
    """
    Sum = 0
    row, col = arr.shape
    
    
    for i in range(row):
        for j in range(col):
            Sum = Sum +  arr[i,j]
    return Sum

#arr = np.array([[ 1,  2,  3],
#       [ 4,  5,  6],
#       [ 7,  8,  9],
#       [10, 11, 0]])
#print(arr)
#Summa = sum_all(arr)
#print(Summa)