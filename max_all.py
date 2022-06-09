import numpy as np

def max_all(arr: np.ndarray) -> int:
    """
    Returns the max of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: max of all numbers
    """
    maximum = arr[0]
    for i in range(10):
        
        if arr[i] > arr[0]:
            maximum = arr[i]
    
    return maximum
    

#arr = np.arange(10)
#arr = np.reshape(arr, (10, 1))
#print(arr)
#maximumi = max_all(arr)
#print(maximumi)
