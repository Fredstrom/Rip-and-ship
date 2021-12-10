from variables import *


def inventory_window():
    inv_header_list = ['Units in stock', 'Capacity', 'Product ID', 'Supplier', 'Manufacturer']
    ord_header_list = ['order id', 'Product name', 'quantity', 'price each', 'total']
    layout = [

        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Inventory', **h1), sg.Text("", **h1),
         sg.Button('Search', font=('Sora SemiBold', 12))],

        # Inventory Table
        [sg.Table(values=inventory_data, headings=inv_header_list, **table, key='-TABLE-', enable_events=True)],
        [sg.Button('Place order', **button2),
         sg.Button('Delete item', **button2),
         sg.Button('Update item', **button2)
         ],

        [sg.Text('Pending orders', **h1)],
        [sg.Table(values=temp, headings=ord_header_list, **table, key='-TABLE-', enable_events=True)],

        [sg.Button('Approve orders', **button2),
         sg.Button('Delete order', **button2),
         sg.Button('Edit order', **button2)
         ]
    ]

    return sg.Window('Table', layout, **wdw)


def edit_item_window(idx):
    layout = [
        [sg.Text('Units in stock', **h2), sg.In(default_text=idx[0], key='units_in_stock')],
        [sg.Text('Capacity: ', **h2), sg.In(default_text=idx[1], key='capacity')],
        [sg.Text('Price: ', **h2), sg.In(default_text=idx[2], key='price')],
        [sg.Text('ProductID: ', **h2), sg.In(default_text=idx[3], key='product_id')],
        [sg.Text('Product Name ', **h2), sg.In(default_text=idx[4], key='product_name')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Submit', **button2, key='-EDIT-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Edit order', layout, size=(500, 600), finalize=True, keep_on_top=True)


def edit_int_order_window(idx):

    layout = [
        [sg.Text('Order ID ', **h2), sg.In(default_text=idx[0], key='order_id')],
        [sg.Text('Customer ID: ', **h2), sg.In(default_text=idx[1], key='customer_id')],
        [sg.Text('Price: ', **h2), sg.In(default_text=idx[2], key='price')],
        [sg.Text('Employee: ', **h2), sg.In(default_text=idx[3], key='employee_id')],
        [sg.Text('Order date: ', **h2), sg.In(default_text=idx[4], key='order_date')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Submit', **button2, key='-EDIT-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Edit order', layout, size=(500, 600), finalize=True, keep_on_top=True)


def add_item_window():
    layout = [
        [sg.Text('Units in stock', **h2), sg.In(key='units_in_stock')],
        [sg.Text('Capacity: ', **h2), sg.In(key='capacity')],
        [sg.Text('Price: ', **h2), sg.In(key='price')],
        [sg.Text('ProductID: ', **h2), sg.In(key='product_id')],
        [sg.Text('Product Name ', **h2), sg.In(key='product_name')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Submit', **button2, key='-Submit-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add item', layout, size=(500, 600), finalize=True, keep_on_top=True)
