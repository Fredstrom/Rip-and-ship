from variables import *


def remove_customer(selection):
    if selection < 0:
        selection = 0
    data.pop(selection - 1)


def add_customer(output):
    data.append(output)


def add_customer(output):
    data.append(output)


def edit_customer(row, output):
    data[row] = output

