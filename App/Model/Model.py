import App.View.View as view
from pathlib import Path


def FindImage(path):
    print(view.CheckingFile(path))

    my_file = Path(path)
    if my_file.is_file():
        abso_path = str(my_file.resolve())
        print(view.ImageFound(abso_path))
        return True
    else:
        print(view.Error(1))
        return False
