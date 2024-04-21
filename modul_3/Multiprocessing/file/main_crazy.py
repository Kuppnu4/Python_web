"""
Sort files in the folder
"""

import argparse
import sys
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging
from multiprocessing import Process, cpu_count, current_process


"""
--source = [-s]
--output = [-o] default folder = dist
"""


parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', help='Source folder', required=True)
parser.add_argument('--output', '-o', help='Output folder', default='dist')
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')

args = vars(parser.parse_args())

source = Path(args['source'])
output = Path(args['output'])


def reader_folders(path: Path):
    logging.info(f'Start process {current_process()} in {path}')
    for el in path.iterdir():
        if el.is_dir():
            inner_process = Process(target=reader_folders, args=(el, ))
            inner_process.start()
        else:
            copy_file(el)


def copy_file(path: Path) -> None:
    # logging.info(f'  files in {path} to copy')

    ext = path.suffix[1:]
    ext_folder = output / ext
    try:
        ext_folder.mkdir(exist_ok=True, parents=True)
        copyfile(path, ext_folder / path.name)
    except OSError as err:
        logging.error(err)
        sys.exit(1)


if __name__ == '__main__':
    pr = Process(target=reader_folders, args=(source,))
    pr.start()
    pr.join()

    print(f'Ready to remove {source}')





