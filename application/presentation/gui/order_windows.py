import PySimpleGUI as sg
from variables import *


def orders_window():
    header_list = ['Order ID', 'Customer ID', 'Price', 'Employee', 'Order date']
    layout = [

        # Row 1
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Orders', **h1), sg.Text("", **h1), sg.Button('Search', font=('Sora SemiBold', 12))],

        # Row 2
        [sg.Table(values=order_data, headings=header_list, **table, key='-TABLE-', enable_events=True)],

        # Row 3
        [sg.Button('Place order', **button2),
         sg.Button('Cancel order', **button2),
         sg.Button('Edit order', **button2),
         ]
    ]

    return sg.Window('Table', layout, **wdw)


def place_order_window():
    layout = [

        [sg.Text('Order ID ', **h2), sg.In(key='order_id')],
        [sg.Text('Customer ID: ', **h2), sg.In(key='customer_id')],
        [sg.Text('Price: ', **h2), sg.In(key='price')],
        [sg.Text('Employee: ', **h2), sg.In(key='employee_id')],
        [sg.Text('Order date: ', **h2), sg.In(key='order_date')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Place order', **button2, key='-PLACE-', bind_return_key=True), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Place order', layout, size=(500, 600), finalize=True, keep_on_top=True)
