import numpy as np

def min_all(arr: np.ndarray) -> int:
    """
    Returns the min of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: min of all numbers
    """
    row, col = arr.shape
    
    mini = arr[0,0]
    for i in range(row):
        for j in range(col):
            if arr[i,j] < mini:
                mini = arr[i,j]
    
    return mini

#arr = np.arange(10)
#print(arr)
#minimumi = min_all(arr)
#print(minimumi)