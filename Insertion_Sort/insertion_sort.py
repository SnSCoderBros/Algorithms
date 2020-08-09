import numpy as np


def insertion_sort(A):
    for i in range(1, len(A)):
        while i > 0 and A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1


A = np.random.randint(low=0, high=50, size=15)

print(A)
insertion_sort(A)
print(A)
