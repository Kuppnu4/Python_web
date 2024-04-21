from threading import Semaphore, Thread, RLock, current_thread
import logging
from time import sleep
from random import randint


class Logger:
    def __init__(self):
        self.active = []
        self.lock = RLock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.info(f'Started the job thread {name}. Now in the pool: {self.active}')

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.info(f'Finished the job thread {name}. Now in the pool: {self.active}')


def worker(semaphore: Semaphore, log: Logger):
    logging.info('waiting for semaphore...')
    with semaphore:
        name = current_thread().name
        logging.info(f'{name} Got semaphore')
        log.make_active(name)
        sleep(randint(1, 3))
        logging.info(f'{name} Finished operation')
        log.make_inactive(name)
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    pool = Semaphore(3)
    logger = Logger()

    for i in range(7):
        w = Thread(target=worker, args=(pool, logger))
        w.start()