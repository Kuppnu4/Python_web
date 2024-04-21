from threading import Event, Thread, current_thread
import logging
from time import sleep


def master(event: Event):
    logging.info('Master make work')
    sleep(1)
    logging.info('Master set event')
    event.set()


def worker(event: Event):
    logging.info(f'{current_thread().name} waiting')
    event.wait()
    logging.info(f'{current_thread().name} made work')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()

    m = Thread(target=master, args=(event,))
    w1 = Thread(target=worker, args=(event,))
    w2 = Thread(target=worker, args=(event,))
    w3 = Thread(target=worker, args=(event,))

    w1.start()
    w2.start()
    w3.start()

    sleep(0.5)

    m.start()
