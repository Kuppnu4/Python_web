def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


if __name__ == '__main__':
    numbers = [3, 15, 13, 25, 1, 17, 9]
    print(selection_sort(numbers))