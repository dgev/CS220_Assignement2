import glob
import os
import shutil
import threading
from threading import Thread
import time


def func(src, dest):
    for filename in glob.glob(os.path.join(src, '*.*')):
        shutil.copy(filename, dest)


def main(src, dest):
    thread: Thread = threading.Thread(target=func, args=(src, dest))
    thread.start()


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))
