import numpy as np

# Questão 1
np.random.seed(5)

arr = np.random.randn(10)*100
arr_int = arr.astype(int)

print(arr_int)

print(np.rint(arr))

# Questão 2
np.random.seed(10)

arr4x4 = np.random.randint(1,50,16).reshape(4,4)

print(arr4x4)

# Questão 3
arrC = arr4x4.mean(axis=0)
arrL = arr4x4.mean(axis=1)

print(arrC.max())
print(arrL.max())

# Questão 4
arr_count = np.unique(arr4x4,return_counts=True)
print(arr_count[0])
print(arr_count[1])

for c in range(len(arr_count[0])):
    if arr_count[1][c] == 2:
        print(arr_count[0][c])