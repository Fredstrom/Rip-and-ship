import PySimpleGUI as sg
from variables import *


def customer_window():
    header_list = ['First Name', 'Last Name', 'Address', 'City', 'zip-code', 'phone', 'E-mail']
    layout = [
        # Row 1
        [sg.Text('Customers', **h1)],

        # Row 2
        [sg.Table(values=data, headings=header_list, **table, key='-TABLE-')],

        # Row 3
        [sg.Button('Add Customer', **button2),
         sg.Button('Remove Customer', **button2),
         sg.Button('Edit Customer', **button2)
         ]

    ]
    return sg.Window('Customers', layout, **wdw)


def add_customer_window():
    layout = [

        [sg.Text('First Name', **h2), sg.In(key='first_name')],
        [sg.Text('Last Name:', **h2), sg.In(key='last_name')],
        [sg.Text('Address: ', **h2), sg.In(key='address')],
        [sg.Text('City: ', **h2), sg.In(key='city')],
        [sg.Text('Zip-code: ', **h2), sg.In(key='zip_code')],
        [sg.Text('Phone No: ', **h2), sg.In(key='phone')],
        [sg.Text('E-mail: ', **h2), sg.In(key='email')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Add Customer', **button2, key='-ADD-'), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add Customer', layout, **wdw, keep_on_top=True)


def remove_customer_window():
    layout = [
        [sg.Text("Remove Customer", **h1)],

        [sg.Text("Which row do you want to remove?", **p)],

        [sg.In(key='customer_id')],

        [sg.Button('Remove Customer'), sg.Button('Cancel')]
    ]

    return sg.Window('Remove customer', layout, **wdw)
