from variables import *


def remove_customer(selection):
    if selection < 0:
        selection = 0
    data.pop(selection - 1)