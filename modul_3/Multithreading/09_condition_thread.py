from threading import Condition, Thread, current_thread
import logging
from time import sleep


def master(con: Condition):
    logging.info('Master thread start')
    sleep(3)
    with con:
        logging.info('Time to work for master')
        sleep(3)
        logging.info('master finished')
        con.notify_all()


def worker(con: Condition):
    logging.info('Waiting order...')
    with con:
        con.wait()
        logging.info('Worker start working')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    con = Condition()

    m = Thread(target=master, args=(con,))
    w1 = Thread(target=worker, args=(con,))
    w2 = Thread(target=worker, args=(con,))

    w1.start()
    w2.start()
    m.start()
