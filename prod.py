import numpy as np

def arr_product(arr: np.ndarray) -> int:
    """
    Returns the product of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: product of all numbers
    """
    Prod = 1
    row, col = arr.shape
    
    for i in range(row):
        for j in range(col):
            Prod = Prod *  arr[i,j]
    return Prod

#arr = np.array([[ 1,  2,  3],
#       [ 4,  5,  6],
#       [ 7,  8,  9],
#       [10, 11, 1]])
#print(arr)
#Proda = arr_product(arr)
#print(Proda)