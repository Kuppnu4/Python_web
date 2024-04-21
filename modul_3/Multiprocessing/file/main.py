"""
Sort files in the folder
"""

import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging


"""
--source = [-s]
--output = [-o] default folder = dist
"""


parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', help='Source folder', required=True)
parser.add_argument('--output', '-o', help='Output folder', default='dist')

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = Path(args['source'])
output = Path(args['output'])

folders = []


def grabs_folders(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folders(el)


def copy_file(path: Path) -> None:
    logging.info(f'  files in {path} to copy')
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')

    logging.info('folders сollecting')
    folders.append(source)
    grabs_folders(source)
    logging.info('folders collected')
    print(folders)

    threads = []
    logging.info('threads creating')
    for folder in folders:
        logging.info(f'')
        th = Thread(target=copy_file, args=(folder, ))
        th.start()
        logging.info(f'thread {th} started')
        threads.append(th)

    [th.join() for th in threads]
    print(f'Ready to remove {source}')





