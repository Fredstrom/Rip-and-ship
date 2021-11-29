import PySimpleGUI as sg

data = [
    ["Anders", "Testsson", "Testgatan 1", "024-224934", "Test@epost.se"],
    ['Berit', "Testberg", 'Storgatan 22', '202192392', 'Berit@telia.se'],
    ["ny kund", "bla bla", "bla bla"],

]
button = {'size': (10, 2),
          'font': ('Roboto Mono', 10, 'bold'),
          'button_color': ("white", "#000000")}

button2 = {'size': (5, 1),
           'font': ('Roboto Mono', 8),
           'button_color': ("black", "#474EAA")}


def frontpage_window():
    layout = [
        [sg.Text('Rip and Ship',
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Helvetica', 30, 'bold'))],

        [sg.Text('Search engine',
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 15, 'bold'))],

        [sg.Text('        ',
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 15, 'bold'))],

        [sg.Button('Customers', **button),
         sg.Button('Orders', **button),
         sg.Button('Inventory', **button)]]

    return sg.Window('Rip and Ship', layout,
                     finalize=True,
                     background_color="#54C5C9",
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def customer_window():
    header_list = ["First Name", "Last Name", "Address", "Phone", "e-mail"]
    layout = [
        [sg.Button('Back'),

         sg.Text('Customers',
                 justification="c",
                 size=(15, 1),
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 30, 'bold')),

         sg.Text("",
                 size=10,
                 background_color="#54C5C9")
         ],

        [sg.Table(values=data,
                  headings=header_list,
                  auto_size_columns=False,
                  background_color="#54C5C9",
                  num_rows=min(25, len(data)))],

        [sg.Button('Add Customer'),
         sg.Button('Remove Customer'),
         sg.Button('Update Customer')
         ]
    ]

    return sg.Window('Customers', layout,
                     finalize=True,
                     background_color="#54C5C9",
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def order_window():
    data = []
    header_list = []
    layout = [
        [sg.Text('Orders',
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 30, 'bold'))],

        [sg.Button('Back')],

        [sg.Table(values=data,
                  headings=header_list,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]
    return sg.Window('Orders', layout,
                     finalize=True,
                     background_color="#54C5C9",
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def inventory_window():
    layout = [
        [sg.Text('Inventory',
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 30, 'bold'))],

        [sg.Button('Back')]
    ]
    return sg.Window('Inventory', layout,
                     finalize=True,
                     background_color="#54C5C9",
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def add_customer_window():
    layout = [
        # Header
        [sg.Text("Add Customer",
                 size=(30, 1),
                 justification='c',
                 background_color="#54C5C9",
                 font=('Arial', 30, 'bold'),
                 text_color='black')],
        # H1
        [sg.Text("Customer First Name:",
                 size=(20, 1),
                 background_color="#54C5C9",
                 text_color='black'),
         # I1
         sg.InputText("", size=(20, 1))],

        [sg.Text("Customer Last Name", size=(20, 1),
                 background_color="#54C5C9",
                 text_color='black'
                 ),
         sg.InputText("",
                      size=(20, 1))
         ],
        [sg.Text("Customer Address:",
                 size=(20, 1),
                 background_color="#54C5C9",
                 text_color='black'),
         # I1
         sg.InputText("", size=(20, 1))],
        [sg.Text("Customer Phone No.:",
                 size=(20, 1),
                 background_color="#54C5C9",
                 text_color='black'),
         # I1
         sg.InputText("", size=(20, 1))],
        [sg.Text("Customer Email:",
                 size=(20, 1),
                 background_color="#54C5C9",
                 text_color='black'),
         sg.InputText("", size=(20, 1))],
        [sg.Button('Save'), sg.Button('Cancel')
    ]
    ]



    return sg.Window('Add Customer', layout,
                     finalize=True,
                     background_color="#54C5C9",
                     size=(500, 400),
                     resizable=True,
                     element_justification='c',
                     keep_on_top=True,
                     modal=True
                     )


def add_customer():
    print("Adding customer...")


def remove_customer():
    selection = int(input("Which row do you want to remove?:"))
    data.pop(selection - 1)


def update_customer():
    print("updating customer")


def main():
    # Design pattern 1 - First window does not remain active
    # customer_screen = None
    # main_screen = make_window1()

    main_screen, customer_screen, order_screen, inventory_screen, add_customer_screen = \
        frontpage_window(), None, None, None, None

    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED or None and window == main_screen:
            break

        if event == 'Customers' and not customer_screen:
            main_screen.hide()
            customer_screen = customer_window()

        if window == customer_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            customer_screen.close()
            customer_screen = None
            main_screen.un_hide()

        if window == customer_screen and (event in (sg.Button, 'Add Customer')):
            add_customer_window()
            customer_screen.close()
            customer_screen = customer_window()

        if window == customer_screen and (event in (sg.Button, 'Remove Customer')):
            remove_customer()
            customer_screen.close()
            customer_screen = customer_window()

        if window == customer_screen and (event in (sg.Button, 'Update Customer')):
            update_customer()
            customer_screen.close()
            customer_screen = customer_window()

        if event == 'Orders' and not order_screen:
            main_screen.hide()
            order_screen = order_window()

        if window == order_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            order_screen.close()
            order_screen = None
            main_screen.un_hide()

        if window == 'Inventory' and not inventory_screen:
            main_screen.hide()
            inventory_screen = inventory_window()

        if window == inventory_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            inventory_screen.close()
            inventory_screen = None
            main_screen.un_hide()

    main_screen.close()


if __name__ == '__main__':
    main()
