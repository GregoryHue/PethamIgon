import App.Model.Model as model
import App.Controller.Controller as controller
import App.View.View as view

import sys
from PIL import Image

path = 'Images/Hands.png'
# newPath = 'Images/Hands_new.png'
colorToDelete = model.Color(0, 0, 0, 255)


def main():
    if model.FindImage(path):
        newImg = controller.DeleteBackground(model.ImageOpened(path).convert('RGBA'), colorToDelete, tolerance=3)
        newImg.save(model.GetFolderOfFile(path) + '\\' + model.GetFileName(path) + '_new.png')

        # outlineData = controller.SelectOutline(model.ImageOpened(newPath).convert('RGBA'))
        # newImg = controller.ModifyData(outlineData, newImg)
        # newImg.save(model.GetFolderOfFile(path) + '\\' + model.GetFileName(path) + '_outlined_new.png')
        view.Success(model.GetAbsoFolderOfFile(path))
    else:
        exit(0)


if __name__ == '__main__':
    main()
