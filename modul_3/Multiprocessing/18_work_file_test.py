from multiprocessing import Process, RLock as PRLock
from multiprocessing.dummy import Pool, RLock as DummyLock  # Thread with Process shell
from threading import Thread, RLock as TRLock
from time import time


def worker(values, filename, lock):
    with lock:
        with open(filename, 'a') as f:
            for num in values:
                f.write(f'{num ** 2}/n')


if __name__ == '__main__':
    values = list(range(600_000))

    th_filename = 'th_squares.txt'
    th_lock = TRLock()
    threads = [
        Thread(target=worker, args=(values[:200_000], th_filename, th_lock)),
        Thread(target=worker, args=(values[200_000:400_000], th_filename, th_lock)),
        Thread(target=worker, args=(values[400_000:], th_filename, th_lock))
    ]
    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Done by 3 threads: {round(time() - timer, 4)}')

    pr_filename = 'pr_squares.txt'
    pr_lock = PRLock()
    processes = [
        Process(target=worker, args=(values[:200_000], pr_filename, pr_lock)),
        Process(target=worker, args=(values[200_000:400_000], pr_filename, pr_lock)),
        Process(target=worker, args=(values[400_000:], pr_filename, pr_lock))
    ]
    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    [process.close() for process in processes]
    print(f'Done by 3 processes: {round(time() - timer, 4)}')

    timer = time()
    worker(values, 'squares.txt', th_lock)
    print(f'Done by 1 processes: {round(time() - timer, 4)}')

    pl_filename = 'pl_squares.txt'
    pl_lock = DummyLock()
    timer = time()
    with Pool(3) as pool:
        result = pool.starmap(worker, [
            (values[:200_000], pl_filename,pl_lock),
            (values[200_000:400_000], pl_filename, pl_lock),
            (values[400_000:], pl_filename, pl_lock)
        ])
    print(f'Done by 3 pool processes dummy: {round(time() - timer, 4)}')


