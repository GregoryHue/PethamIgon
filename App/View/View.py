import time


def Success(path):
    return print("Process is done. Check it here : ", path)


def CheckingFile(path):
    return print('Checking if file exists in : ' + path + ' . . .')


def ImageFound(path):
    return print('Image found here : ' + path)


# Unused
def WorkingDots(is_working):
    while is_working:
        print('Working . . .')
        time.sleep(5)


def Error(type_error):
    message = ''
    message += 'There bas been an error : '
    if type_error == 1:
        message += 'Image not found'
    elif type_error == 2:
        message += 'Image wrong type'
    elif type_error == 3:
        message += 'Define a color'
    elif type_error == 4:
        message += ''
    else:
        message += 'error unknown'

    return print(message)
