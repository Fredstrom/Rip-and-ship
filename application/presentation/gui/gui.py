import PySimpleGUI as sg

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
    data = [["", "", ""], ["", "", ""]]
    header_list = []
    layout = [
        [sg.Button('Back'), sg.Text('Customers',
                 size=(30, 1),
                 background_color="#54C5C9",
                 text_color='black',
                 font=('Arial', 30, 'bold'))],

        [sg.Table(values=data,
                  headings=["First Name", "Last Name", "Address", "Phone", "e-mail"],
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))],

        [sg.Button('Add Customer'), sg.Button('Remove Customer'), sg.Button('Update Customer')]]

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


def main():
    # Design pattern 1 - First window does not remain active
    # window2 = None
    # window1 = make_window1()

    window1, window2, window3, window4 = frontpage_window(), None, None, None

    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED and window == window1:
            break

        if event == 'Customers' and not window2:
            window1.hide()
            window2 = customer_window()

        if window == window2 and (event in (sg.WIN_CLOSED, 'Back')):
            window2.close()
            window2 = None
            window1.un_hide()

        if event == 'Orders' and not window3:
            window1.hide()
            window3 = order_window()

        if window == window3 and (event in (sg.WIN_CLOSED, 'Back')):
            window3.close()
            window3 = None
            window1.un_hide()

        if window == 'Inventory' and not window4:
            window1.hide()
            window4 = inventory_window()

        if window == window4 and (event in (sg.WIN_CLOSED, 'Back')):
            window4.close()
            window4 = None
            window1.un_hide()

    window1.close()


if __name__ == '__main__':
    main()
