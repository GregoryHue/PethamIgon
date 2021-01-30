import App.Model.Model as model
import App.Controller.Controller as controller

path = 'Images/'
imageName = 'Hands'
extension = ".png"

firstPath = path + imageName + extension
secondPath = path + imageName + '_new' + extension

color_to_delete = model.Color(0, 0, 0, 255)
img = model.Img(firstPath)


def main():
    if model.FindImage(firstPath):

        print(img.path_absolute)
        print(img.path_working)
        print(img.path_local)
        print(img.file)
        print(img.extension)
        print(img.file_extension)
        print(img.path_file)
        print(img.path_file_extension)

        # DeleteBackground
        new_img = controller.DeleteBackground(model.open_image(img.path_file_extension).convert('RGBA'), color_to_delete, tolerance=3)
        new_img.save(img.path_file + '_new' + img.extension)

        exit(0)

        # SelectOutline
        new_img = controller.SelectOutline(model.open_image(secondPath).convert('RGBA'))
        new_img.save(model.GetFolderOfFile(firstPath) + '\\' + model.GetFileName(firstPath) + '_outlined_new.png')

        # ReverseColor
        new_img = controller.ReverseColor(model.open_image(firstPath).convert('RGBA'))
        new_img.save(model.GetFolderOfFile(firstPath) + '\\' + model.GetFileName(firstPath) + '_reversed.png')

    else:
        exit(0)


if __name__ == '__main__':
    main()

# TODO
# - Permettre l'execution en ligne de commande, à l'aide d'arguments.
# - Permettre d'executer la fonction "OutLine" X fois
# - Permettre de choisir une couleur plutot que définir les pixels RGBA
# - Permettre d'executer sur toutes les images d'un dossier
# - Réorganiser le main
# - Ajouter Django pour une interface web
