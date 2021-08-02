import os

import App.View.View as view

from PIL import Image
from pathlib import Path


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


class Img:
    def __init__(self, path_to_img):
        self.path_absolute = str(Path(path_to_img).resolve())
        self.path_working = os.getcwd()
        self.path_local = str(Path(path_to_img).parent)
        self.file = Path(path_to_img).stem
        self.extension = os.path.splitext(path_to_img)[1]
        self.file_extension = Path(path_to_img).stem + os.path.splitext(path_to_img)[1]
        self.path_file = os.path.splitext(path_to_img)[0]
        self.path_file_extension = path_to_img


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


def open_image(path):
    return Image.open(path)
