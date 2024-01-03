import numpy as np

arr = np.array([5, 6, 7, 8])

def compound():
    new = []
    new.append(arr[0])
    for i in range(1,len(arr)):
        new.append(arr[i]*arr[i-1])
    print(new)

compound()
