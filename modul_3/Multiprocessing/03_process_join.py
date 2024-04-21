from multiprocessing import Process
import sys
from time import sleep


def example_work(params):
    sleep(1.5)
    print(params)
    sys.exit(0)


if __name__ == '__main__':
    process = []
    for i in range(5):
        pr = Process(target=example_work, args=(f'Count process - {i}',), daemon=True)  # daemon = True
        # daemon=True - kills processes which have not been finished before the  end of program
        pr.start()
        process.append(pr)

    [pr.join() for pr in process]
    sleep(1)
    print('End program')
