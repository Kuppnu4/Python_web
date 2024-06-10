numbers = [1, 3, 5, 7, 11, 15]


def linear_search(arr: list, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


print(linear_search(numbers, 7))


