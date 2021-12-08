import PySimpleGUI as sg
from variables import *


def inventory_window():
    header_list = ['Units in stock', 'Capacity', 'Product ID', 'Supplier', 'Manufacturer']
    layout = [

        # Row 1
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Inventory', **h1), sg.Text("", **h1),
         sg.Button('Search', font=('Sora SemiBold', 12))],

        # Row 2
        [sg.Table(values=inventory_data, headings=header_list, **table, key='-TABLE-', enable_events=True)],

        # Row 3

        [sg.Button('Place order', **button2),
         sg.Button('Delete order', **button2),
         sg.Button('Edit order', **button2), sg.Text("", **filler)
         ]
    ]

    return sg.Window('Table', layout, **wdw)
