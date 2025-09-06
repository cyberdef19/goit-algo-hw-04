import os
import shutil

def copy_files(files: list, dest: str):
    subdirs = []
    for f in files:
        try:
            ext = os.path.basename(f).split('.')[1]
            if ext not in subdirs:
                subdirs.append(ext)
        except Exception as ex:
            if "_" not in subdirs:
                subdirs.append("_")

    for subdir in subdirs:
        try:
            os.mkdir(os.path.join(dest, subdir))
        except Exception as ex:
            print(str(ex))

    for f in files:
        try:
            ext = os.path.basename(f).split('.')[1]
            os.path.join(dest, ext)
            shutil.copy2(f, os.path.join(os.path.join(dest, os.path.basename(f).split(".")[1]), os.path.basename(f)))
        except Exception as ex:
            print(str(ex))




