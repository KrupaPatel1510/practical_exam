import numpy as np
ages = np.array([19, 42, 16, 28, 33, 15, 51])
print(ages[ages >= 18])
print(ages[(ages > 25) & (ages < 45)])
print(ages[~(ages >= 18)])
scores = np.array([48, 91, 66, 73, 59, 85])
result = np.where(scores >= 70, "Pass", "Fail")
print(result)
temps = np.array([31, 27, 36, 40, 29, 33])

mask = temps > 35

temps[mask] = 34

print(temps, int(mask.sum()))
mat = np.arange(3, 28).reshape(5, 5)
print(mat[1:4, 2:5])
view = mat[0]
view[0] = 99
print(mat[0, 0])
copy = mat[1].copy()
copy[0] = -1
print(mat[1, 0])

