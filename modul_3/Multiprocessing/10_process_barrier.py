import sys
from random import randint
from multiprocessing import Process, Barrier, current_process
from time import sleep, ctime


def worker(barrier: Barrier):
    name = current_process().name
    print(f'Start process {name}: {ctime()}')
    sleep(randint(1,3))  # imitation of some work
    barrier.wait()
    print(f'Barrier closed for {name}')
    print(f'End work process {name}: {ctime()}')
    sys.exit(0)


if __name__ == '__main__':
    barrier = Barrier(2)
    prs = []
    for i in range(10):
        pr = Process(name=f'Process {i}', target=worker, args=(barrier, ))
        pr.start()
        prs.append(pr)

    [pr.join() for pr in prs]
    print('End program')
