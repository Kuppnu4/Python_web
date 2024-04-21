from threading import Thread
import logging
from time import sleep


def example_work(delay):
    sleep(delay)
    logging.debug('Wake up!!!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()