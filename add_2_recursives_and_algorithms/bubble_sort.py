def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],  arr[j + 1] = arr[j + 1],  arr[j]
    return arr


numbers = [21, 12, 45, 3, 9, 15, 30]

print(bubble_sort(numbers))
