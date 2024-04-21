from threading import Event, Thread, current_thread
import logging
from time import sleep


def worker_smart(event: Event, time: float):
    while not event.is_set():
        logging.info('Waiting for event set to complete')
        e_wait = event.wait(time)  # sleep(time) returns True or False
        if e_wait:
            logging.info('make job because master ordered')
        else:
            logging.info('can play cell phone')


def worker_stupid(event: Event):
    logging.info(f'{current_thread().name} waiting')
    event.wait()
    logging.info(f'{current_thread().name} made work')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()

    wrk = Thread(target=worker_stupid, args=(event,))
    wrk.start()

    wrk_smart = Thread(target=worker_smart, args=(event, 1))
    wrk_smart.start()

    sleep(3)

    event.set()
    logging.info('End Program')



