def quick_sort(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n//2]
    left = [el for el in arr if el < pivot]
    middle = [el for el in arr if el == pivot]
    right = [el for el in arr if el > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    numbers = [3, 15, 13, 25, 1, 17, 9]
    print(quick_sort(numbers))