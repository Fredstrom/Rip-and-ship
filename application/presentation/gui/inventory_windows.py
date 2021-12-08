import PySimpleGUI as sg
from variables import *


def inventory_window():
    header_list = ['Units in stock', 'Capacity', 'Product ID', 'Supplier', 'Manufacturer']
    layout = [

        # Huvudrubrik
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Inventory', **h1), sg.Text("", **h1),
         sg.Button('Search', font=('Sora SemiBold', 12))],

        [sg.Text('Orders', **h2)],
        [sg.Table(values=inventory_data, headings=header_list, **table, key='-TABLE-', enable_events=True)],
        [sg.Button('Place order', **button2),
         sg.Button('Delete order', **button2),
         sg.Button('Update order', **button2), sg.Text("", **filler)
         ],
        [sg.Text('Pendling orders', **h2)],
        [sg.Table(values=inventory_data, headings=header_list, **table, key='-TABLE-', enable_events=True)],

        [sg.Button('Place order', **button2),
         sg.Button('Delete order', **button2),
         sg.Button('Update order', **button2), sg.Text("", **filler)
         ]
    ]

    return sg.Window('Table', layout, **wdw)


def place_order_change_customer_window():
    pass


