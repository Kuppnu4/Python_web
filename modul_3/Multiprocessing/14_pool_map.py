from multiprocessing import Pool, current_process, cpu_count


def worker(val):
    sum = 0
    for i in range(val):
        sum += i

    print(f'{val}: {sum}')
    return sum


def callback(result):
    print(f'Result in callback: {result}')


if __name__ == '__main__':
    print(f'Count CPU: {cpu_count()}')
    with Pool(cpu_count()) as pool:
        pool.map_async(
            worker,
            [100, 200, 1024, 10, 23, 2314, 34, 24, 242, 24, 12, 2222, 3333, 444, 55],
            callback=callback
        )
        pool.close()
        pool.join()

    print(f'End of: {current_process().name}')

