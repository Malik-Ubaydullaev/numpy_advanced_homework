import numpy as np

def max_all(arr: np.ndarray) -> int:
    """
    Returns the max of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: max of all numbers
    """
    row, col = arr.shape
    
    maxi = arr[0,0]
    for i in range(row):
        for j in range(col):
            if arr[i,j] > maxi:
                maxi = arr[i,j]    
    return maxi
    

#arr = np.arange(10)
#arr = np.reshape(arr, (10, 1))
#print(arr)
#maximumi = max_all(arr)
#print(maximumi)
