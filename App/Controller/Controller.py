from PIL import Image

import App.Model.Model as model
import App.View.View as view


# Efface le fond de couleur unique
def DeleteBackground(img: Image, color_to_delete: model.Color, tolerance=5, transparency=1):

    width, height = img.size
    new_img = Image.new('RGBA', (width, height))

    for i in range(width):
        for j in range(height):

            r, g, b, a = img.getpixel((i, j))

            # Efface tout les pixels equivalent à : colorToDelete +/- la tolerance
            if (color_to_delete.r - tolerance) <= r <= (color_to_delete.r + tolerance) and \
                    (color_to_delete.g - tolerance) <= g <= (color_to_delete.g + tolerance) and \
                    (color_to_delete.b - tolerance) <= b <= (color_to_delete.b + tolerance) and \
                    (color_to_delete.a - tolerance) <= a <= (color_to_delete.a + tolerance):
                pixel_to_put = (int(0), int(0), int(0), int(0))

            # Réajuste la transparence du reste de l'image
            else:
                a = (abs((color_to_delete.r - r)) + abs((color_to_delete.g - g)) + abs((color_to_delete.b - b))) * transparency
                if a > 255:
                    a = 255
                elif a < 0:
                    a = 0

                pixel_to_put = (int(r), int(g), int(b), int(a))

            new_img.putpixel((i, j), pixel_to_put)
    return new_img


# Inverse les couleurs sur l'image
def ReverseColor(img: Image):
    width, height = img.size
    data = []

    for j in range(width):
        for i in range(height):

            r, g, b, a = img.getpixel((i, j))

            pixel_to_put = (int(abs(r - 255)), int(abs(g - 255)), int(abs(b - 255)), int(a))

            position_and_color = [i, j, pixel_to_put]
            data.append(position_and_color)

    for i, j, pixel_to_put in data:
        img.putpixel((i, j), pixel_to_put)

    return img


# Efface le bord d'une image
def SelectOutline(img: Image):
    width, height = img.size
    data = []

    for i in range(width):
        for j in range(height):

            r, g, b, a = img.getpixel((i, j))

            if isNextToVoid(i, j, img) and a != 0:
                position = [i, j]
                data.append(position)

    for i, j in data:
        img.putpixel((i, j), (0, 0, 0, 0))

    return img


# Verifie si un pixel en [i, j] est isolé
def isNextToVoid(i, j, img: Image):
    try:
        left_pixel = img.getpixel((i - 1, j))
        up_pixel = img.getpixel((i, j - 1))
        right_pixel = img.getpixel((i + 1, j - 1))
        down_pixel = img.getpixel((i, j + 1))
    except IndexError:
        left_pixel = (0, 0, 0, 0)
        up_pixel = (0, 0, 0, 0)
        right_pixel = (0, 0, 0, 0)
        down_pixel = (0, 0, 0, 0)

    if left_pixel[3] == 0 or up_pixel[3] == 0 or right_pixel[3] == 0 or down_pixel[3] == 0:
        return True
    else:
        return False
