from random import randint
from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,args=args, kwargs=kwargs, daemon=daemon)

    def run(self):
        ttl = randint(1, 3)
        sleep(ttl)
        logging.info(f'In my thread {self.name}: {ttl} seconds')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    threads = []

    for i in range(5):
        th = MyThread(name=f'Thread#{i+1}', args=(f'count th = {i}',), daemon=True)
        '''in  daemon=True mode program kills all the threads which were not finished'''
        th.start()
        threads.append(th)

    #threads[0].join()
    #[thr.join() for thr in threads]
    sleep(2)
    logging.info('End Program')
