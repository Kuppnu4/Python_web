from threading import Event, Thread, current_thread
import logging
from time import sleep


def worker(event: Event):
    while True:
        if event.is_set():
            break
        sleep(1)
        logging.info('DDOS server')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    event = Event()

    th = Thread(target=worker, args=(event, ))
    th.start()

    sleep(5)
    event.set()
    logging.info('End program')

