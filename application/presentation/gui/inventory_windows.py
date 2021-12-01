import PySimpleGUI as sg
from variables import *


def inventory_window():
    layout = [
        [sg.Text('Inventory', **h1)],

        [sg.Button('Back', **button2)]
    ]
    return sg.Window('Inventory', layout, **wdw)
