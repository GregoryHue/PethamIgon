import time



def Success(path):
    return print("Process is done. Check it here : ", path)


def CheckingFile(path):
    return print('Checking if file exists in : ' + path + ' . . .')


def ImageFound(path):
    return print('Image found here : ' + path)


# Unused
def WorkingDots(isWorking):
    while isWorking:
        print('Working . . .')
        time.sleep(5)


def Error(typeError):
    message = ''
    message += 'There bas been an error : '
    if typeError == 1:
        message += 'Image not found'
    elif typeError == 2:
        message += 'Image wrong type'
    elif typeError == 3:
        message += ''
    elif typeError == 4:
        message += ''
    else:
        message += 'error unknown'

    return print(message)
