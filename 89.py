import numpy as np

try:
    n = int(input("Enter how many numbers to generate: "))

    arr = np.random.randint(10,101,n)

    print("\nArray:")
    print(arr)

    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))

    rows = int(input("\nEnter number of rows for reshape: "))

    if n % rows == 0:
        mat = arr.reshape(rows, n//rows)
        print("\nReshaped Array:")
        print(mat)

        print("Row-wise Sum:")
        print(np.sum(mat, axis=1))
    else:
        print("Reshape not possible.")

except ValueError:
    print("Invalid Input!")