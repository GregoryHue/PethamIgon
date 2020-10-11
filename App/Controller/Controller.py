import threading

from PIL import Image

import App.Model.Model as model


def DeleteBackground(img: Image, colorToDelete: model.Color, tolerance=5, transparency=1):
    width, height = img.size
    newImg = Image.new('RGBA', (width, height))

    for i in range(width):
        for j in range(height):

            R, G, B, A = img.getpixel((i, j))

            # Efface tout les pixels equivalent à colorToDelete +/- la tolerance
            if (colorToDelete.red - tolerance) <= R <= (colorToDelete.red + tolerance) and \
                    (colorToDelete.green - tolerance) <= G <= (colorToDelete.green + tolerance) and \
                    (colorToDelete.blue - tolerance) <= B <= (colorToDelete.blue + tolerance) and \
                    (colorToDelete.alpha - tolerance) <= A <= (colorToDelete.alpha + tolerance):
                pixelToPut = (int(0), int(0), int(0), int(0))

            # Réajuste la transparence du reste de l'image
            else:
                A = (abs((colorToDelete.red - R)) + abs((colorToDelete.green - G)) + abs((colorToDelete.blue - B))) * transparency
                if A > 255:
                    A = 255
                elif A < 0:
                    A = 0

                pixelToPut = (int(R), int(G), int(B), int(A))

            newImg.putpixel((i, j), pixelToPut)
    return newImg


def SelectOutline(img: Image):
    width, height = img.size
    data = []

    for i in range(width):
        for j in range(height):

            R, G, B, A = img.getpixel((i, j))

            if isNextToVoid(i, j, img) and A != 0:
                position = [i, j]
                data.append(position)

    return data


def ModifyData(data, img: Image):
    for i, j in data:
        img.putpixel((i, j), (0, 0, 0, 0))
    return img


def isNextToVoid(i, j, img):
    try:
        leftPixel = img.getpixel((i - 1, j))
        upPixel = img.getpixel((i, j - 1))
        rightPixel = img.getpixel((i + 1, j - 1))
        downPixel = img.getpixel((i, j + 1))
    except IndexError:
        leftPixel = (0, 0, 0, 0)
        upPixel = (0, 0, 0, 0)
        rightPixel = (0, 0, 0, 0)
        downPixel = (0, 0, 0, 0)

    if leftPixel[3] == 0 or upPixel[3] == 0 or rightPixel[3] == 0 or downPixel[3] == 0:
        return True
    else:
        return False
