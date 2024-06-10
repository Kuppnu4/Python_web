def insert_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):  # 4
        temp = arr[i]  # 1
        j = i - 1  # -1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  # [3, 3, 13, 15, 25, 17]
            j = j - 1  # 0
        arr[j + 1] = temp  # [1, 3, 13, 15, 25, 17]
    return arr


if __name__ == '__main__':
    numbers = [3, 15, 13, 25, 1, 17]
    print(insert_sort(numbers))