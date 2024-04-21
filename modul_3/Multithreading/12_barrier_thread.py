from threading import Barrier, Thread, RLock, current_thread
import logging
from time import sleep, ctime
from random import randint


def worker(barrier: Barrier):
    name = current_thread().name
    logging.info(f'Start thread {name}: {ctime()}')
    num = barrier.wait()
    sleep(randint(1, 3))
    logging.info(f'{name}#{num}: {ctime()} Barrier was overcome')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    br = Barrier(4)
    for i in range(12):
        w = Thread(target=worker, args=(br, ))
        w.start()
