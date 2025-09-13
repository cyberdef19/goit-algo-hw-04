import os
import shutil

def walk_directory(path: str):
    try:
        paths = []
        if len(os.listdir(path)) == 0:
            return []

        oFiles = os.listdir(path)
        for f in oFiles:
            obj = os.path.join(path, f)
            if os.path.isdir(obj):
                paths.extend(walk_directory(obj))
            elif os.path.isfile(obj):
                paths.append(obj)
    except PermissionError as ex:
        print(f"Немає прав доступу до об'єкта {str(ex)}")
    except NotADirectoryError as ex:
        print(f"Спроба звернутися до неіснуючої директорії {str(ex)}")
    except Exception as ex:
        print(str(ex))
    return paths

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


