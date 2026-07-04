import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("1D Array:", a)
print("Shape:", a.shape)
print("Data Type:", a.dtype)

print("\n2D Array:")
print(b)
print("Shape:", b.shape)
print("Data Type:", b.dtype)