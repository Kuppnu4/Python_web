import sys
from multiprocessing import Process, Condition
from time import sleep


def master(con: Condition):
    print('Master process start')
    sleep(3)
    with con:
        print('Time to work for master')
        sleep(3)
        print('master finished and gave permission')
        con.notify_all()
        sys.exit(0)


def worker(con: Condition):
    print('Waiting order...')
    with con:
        con.wait()
        print('Worker makes work')
        sys.exit(0)


if __name__ == '__main__':
    con = Condition()
    m_pr = Process(target=master, args=(con,))
    w1_pr = Process(target=worker, args=(con,))
    w2_pr = Process(target=worker, args=(con,))
    w1_pr.start()
    w2_pr.start()
    sleep(1)
    m_pr.start()
    sleep(1)

