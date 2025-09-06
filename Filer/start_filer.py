import sys

from Filer.copy_files import copy_files
from Filer.walk_directory import walk_directory


def start_files():

    if len(sys.argv) == 3:
        path_source = sys.argv[1]
        path_dest = sys.argv[2]
    elif len(sys.argv) == 2:
        path_source = sys.argv[1]
        path_dest = 'dist'
    elif len(sys.argv) < 2:
        print("Має бути передано один шлях до вихідної директорії "
              "та шлях до директорії призначення")
        return
    else:
        print("Занадто багато параметрів")
        return

    files = walk_directory(path_source)
    copy_files(files, path_dest)

start_files()