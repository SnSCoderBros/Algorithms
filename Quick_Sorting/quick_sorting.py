A = [5, 4, 3, 2, 1]


def quick_sort(A):
    _quick_sort(A, 0, len(A) - 1)


def split(A, start, end):
    i = start
    pivot = A[end]

    for j in range(start, end):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[end], A[i] = A[i], A[end]

    return i


def _quick_sort(A, start, end):
    if start < end:
        idx = split(A, start, end)
        _quick_sort(A, idx + 1, end)
        _quick_sort(A, start, idx - 1)


quick_sort(A)
print(A)
