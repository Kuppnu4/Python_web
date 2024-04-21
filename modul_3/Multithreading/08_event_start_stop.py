from threading import Event, Thread, current_thread
import logging
from time import sleep


def worker(event: Event, event_for_exit: Event):
    while True:
        if event_for_exit.is_set():
            break
        sleep(1)
        if event.is_set():
            logging.info('Running idle')
            continue
        else:

            logging.info('DDOS server')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    event = Event()
    event_exit = Event()

    th = Thread(target=worker, args=(event, event_exit))
    th.start()

    logging.info('Start program')
    sleep(4)
    event.set()  # stop the thread
    logging.info('Stop Thread')
    sleep(4)
    event.clear()
    logging.info('Start Thread')
    sleep(3)
    event_exit.set()
    logging.info('End program')


