from random import randint


def sort(arr):
    n = len(arr)
    print(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr = []
    for _ in range(10):
        arr.append(randint(1, 100))
    print(sort(arr))
