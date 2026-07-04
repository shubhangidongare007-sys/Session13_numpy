import numpy as np

A = np.random.randint(1,51,20)

print("1D Array:")
print(A)

B = A.reshape(4,5)

print("\n4x5 Matrix:")
print(B)

print("Sum:", np.sum(B))
print("Mean:", np.mean(B))
print("Standard Deviation:", np.std(B))
print("Maximum in Each Row:", np.max(B, axis=1))