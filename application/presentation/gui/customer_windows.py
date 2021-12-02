import PySimpleGUI as sg
from variables import *


def customer_window():

    header_list = ['First Name', 'Last Name', 'Address', 'City', 'zip-code', 'phone', 'E-mail']
    layout = [

        # Row 1
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Customers', **h1), sg.Text("", **h1), sg.Button('Search', font=('Sora SemiBold', 12))],

        # Row 2
        [sg.Table(values=data, headings=header_list, **table, key='-TABLE-', enable_events=True)],

        # Row 3

        [ sg.Button('Add Customer', **button2),
         sg.Button('Remove Customer', **button2),
         sg.Button('Edit Customer', **button2), sg.Text("", **filler)
         ]
    ]

    return sg.Window('Table', layout, **wdw)


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
        [sg.Text("", **h2), sg.Button('Add Customer', **button2, key='-ADD-', bind_return_key=True), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add Customer', layout, size=(500, 600), finalize=True, keep_on_top=True)


def edit_customer_window(idx):
    layout = [
        [sg.Text('First Name', **h2), sg.In(default_text=idx[0], key='first_name')],
        [sg.Text('Last Name:', **h2), sg.In(default_text=idx[1], key='last_name')],
        [sg.Text('Address: ', **h2), sg.In(default_text=idx[2], key='address')],
        [sg.Text('City: ', **h2), sg.In(default_text=idx[3], key='city')],
        [sg.Text('Zip-code: ', **h2), sg.In(default_text=idx[4], key='zip_code')],
        [sg.Text('Phone No: ', **h2), sg.In(default_text=idx[5], key='phone')],
        [sg.Text('E-mail: ', **h2), sg.In(default_text=idx[6], key='email')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Submit', **button2, key='-EDIT-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Edit Customer', layout, size=(500, 600), finalize=True, keep_on_top=True)
