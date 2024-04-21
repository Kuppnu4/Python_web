from threading import Thread


def worker(args):
    print(args)


if __name__ == '__main__':
    for i in range(5):
        th = Thread(target=worker, args=(f'count th = {i}',))
        th.start()
