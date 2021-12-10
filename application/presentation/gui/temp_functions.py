from variables import *


def remove_customer(selection):
    if selection < 0:
        selection = 0
    data.pop(selection - 1)


def add_customer(output):
    data.append(output)


def edit_customer(row, output):
    data[row] = output


def place_order(output):
    order_data.append(output)


def edit_item(row, output):
    inventory_data[row] = output


def edit_order(row, output):
    order_data[row] = output
