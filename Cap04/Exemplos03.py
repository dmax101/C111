import numpy as np

# Slicing e, arrays 1-D


arr = np.array([2,1,5,3,7,4,6,8])
#print(arr[3:])
#print(arr[-2:])

# Slicing e, arrays 2-D
mtz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
])

#print(mtz[0:2][-1])

# Condicionais do mumpy
arr = np.array([2,1,5,3,7,4,6,8])

#print(arr<5)
#print(arr[arr<5])
#print(arr[arr%2 == 0])

# Cópias de arrays
arr = np.array([2,1,5,3,7,4,6,8])
arr2 = arr[4:].copy()
arr2[0] = 100
print(arr2)

# Padrões textuais (numpy.char)
arr = np.array(['Inatel', 'ICC', 'Nesp', 'NEmp', 'CTIC', 'Incitel'])
print(np.char.find(arr,'tel'))