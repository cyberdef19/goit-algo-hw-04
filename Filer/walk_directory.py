import os

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



