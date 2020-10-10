import sys
import App.Model.Model as model
import App.View.View as view
import App.Controller.Controller as controller
from PIL import Image
from colour import Color


path = 'Images/Img.png'
color = Color(255, 255, 255, 255)

def main():
    if model.FindImage(path):
        controller.DeleteBackground(path, color)
    else:
        exit(0)


if __name__ == '__main__':
    main()
