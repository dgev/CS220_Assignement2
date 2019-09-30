import glob
import os
import shutil
import time


def main(src, dest):
    # Copy files to another directory
    for filename in glob.glob(os.path.join(src, '*.*')):
        shutil.copy(filename, dest)


if __name__ == '__main__':
    start_time = time.time()
    main('/Oldfolder', '/Newfolder')
    print("--- %s seconds ---" % (time.time() - start_time))



