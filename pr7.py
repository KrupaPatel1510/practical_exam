import numpy as np

a = np.arange(5, 56, 5)
print(a)
zeros = np.zeros((2, 6))
ones = np.ones((3, 3), dtype=float)
print(zeros.shape, ones.shape, np.sum(ones))
print(np.eye(3) * 6)
lin = np.linspace(0, 10, 50)
print(len(lin), round(float(lin[1]), 4), float(lin[-1]))
np.random.seed(3)
r = np.random.randint(1, 21, size=(4, 4))
print(r)
r[0, :] = 100
print(r[0, :])
print(r[-2:, -2:])