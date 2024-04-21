from multiprocessing import Pool, current_process, cpu_count
from random import randint
from time import sleep, ctime


def worker():
    name = current_process().name
    print(f'Start proces {name}: {ctime()}')
    r = randint(1, 3)
    sleep(r)
    print(f'End process {name}: {ctime()}')
    return f'Process {name}, run time: {r} sec'


def callback(result):
    print(result.upper())


if __name__ == '__main__':
    print(f'Count CPU: {cpu_count()}')
    with Pool(cpu_count()) as pool:
        for i in range(cpu_count()):
            print(i)
            pool.apply_async(worker, callback=callback)
        # pool.apply_async(worker, callback=callback)
        pool.close()  # finish allocate processes in pool
        # pool.terminate()  # to kill all
        pool.join()  # wait all processes to finish

    print(f'End {current_process().name}')



