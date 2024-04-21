from threading import Semaphore, Thread, current_thread
import logging
from time import sleep


def worker(semaphore: Semaphore):
    logging.info('waiting for semaphore...')
    with semaphore:
        logging.info('Got semaphore')
        sleep(1)
        logging.info('Finished operation')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    pool = Semaphore(3)

    for i in range(10):
        w = Thread(target=worker, args=(pool,))
        w.start()