import glob
import os
import shutil
import multiprocessing
import time


def func(src, dest):
    for filename in glob.glob(os.path.join(src, '*.*')):
        shutil.copy(filename, dest)


def main(src, dest):
    p = multiprocessing.Process(target=func, args=(src, dest))

    # starting process
    p.start()


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))
