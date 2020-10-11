import App.View.View as view

from PIL import Image
from pathlib import Path


class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

def GetFileName(path):
    return Path(path).stem


def GetFolderOfFile(path):
    return str(Path(path).parent)


def GetAbsoFolderOfFile(path):
    return str(Path(path).resolve())


def FindImage(path):
    view.CheckingFile(path)

    my_file = Path(path)
    if my_file.is_file():
        abso_path = str(my_file.resolve())
        view.ImageFound(abso_path)
        return True
    else:
        view.Error(1)
        return False


def ImageOpened(path):
    return Image.open(path)
