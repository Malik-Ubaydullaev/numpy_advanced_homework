import numpy as np

def sum_axis_1(arr: np.ndarray) -> int:
    """
    Returns the max of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: max of each row
    """
       
    return arr.min(axis=0)

#arr = np.arange(10)
#print(arr)
#minimumi = min_all(arr)
#print(minimumi)