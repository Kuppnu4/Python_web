def count_sort(arr: list, pos):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # счет вхождений определенного разряда
    for i in range(0, size):
        index = arr[i] // pos % 10
        count[index] += 1

    for i in range(0, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // pos % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr: list) -> list:
    max_num = max(arr)
    position = 1
    while max_num // position > 0:
        count_sort(arr, position)
        position *= 10
    return arr


if __name__ == '__main__':
    numbers = [3, 15, 13, 25, 1, 17]
    print(radix_sort(numbers))
