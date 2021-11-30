import PySimpleGUI as sg
from variables import *


def customer_window():
    header_list = ['Customer ID', 'First Name', 'Last Name', 'Address', 'zip-code']
    layout = [
        # Row 1
        [sg.Text('Customers', **h1)],

        # Row 2
        [sg.Table(values=data, headings=header_list, **table)],

        # Row 3
        [sg.Button('Add Customer', **button2),
         sg.Button('Remove Customer', **button2),
         sg.Button('Edit Customer', **button2)
         ]

    ]
    return sg.Window('Customers', layout, **wdw)


def add_customer_window():
    layout = [
        # input fields...
        [sg.Text('First Name', **h2), sg.In(key="first_name")],
        [sg.Text('Last Name:', **h2), sg.In(key="last_name")],
        [sg.Text('Address: ', **h2), sg.In(key="address")],
        [sg.Text('City: ', **h2), sg.In(key="city")],
        [sg.Text('Zip-code: ', **h2), sg.In(key="zip_code")],
        [sg.Text('Phone No: ', **h2), sg.In(key="phone")],
        [sg.Text('E-mail: ', **h2), sg.In(key="email")],

        # Bottom row
        [sg.Button('Add Customer', **button2), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add Customer', layout, **wdw)
