import PySimpleGUI as sg

button = {'size': (8, 2), 'font': ('Roboto Mono', 10), 'button_color': ("black", "#F8F8F8")}
button2 = {'size': (5, 1), 'font': ('Roboto Mono', 8), 'button_color': ("black", "#474EAA")}


def make_window1():
    layout = [
        [sg.Text('Rip and Ship', size=(30,1), justification='c',background_color="#54C5C9",
                       text_color='black', font=('Arial', 30, 'bold'))],
        [sg.Text('Search engine', size=(30,1), justification='c', background_color="#54C5C9",
                       text_color='black', font=('Arial', 15, 'bold'))],
        [sg.Text('        ', size=(30, 1), justification='c', background_color="#54C5C9",
                       text_color='black', font=('Arial', 15, 'bold'))],
        [sg.Button('Customers', **button), sg.Button('Orders', **button), sg.Button('Inventory', **button)]]

    return sg.Window('Rip and Ship', layout, finalize=True,
                     background_color="#54C5C9", size=(500, 400), resizable=True, element_justification='center')


def make_window2():
    data = []
    header_list = []
    layout = [[sg.Text('Customers', size=(30,1), justification='c', background_color="#54C5C9",
               text_color='black', font=('Arial', 30, 'bold'))],
              [sg.Button('Exit')],
              [sg.Table(values=data,
                        headings=header_list,
                        auto_size_columns=False,
                        num_rows=min(25, len(data)))]
              ]

    return sg.Window('Customers', layout, finalize=True,
                     background_color="#54C5C9", size=(500, 400), resizable=True, element_justification='center')


def make_window3():
    layout = [
        [sg.Text('Orders', size=(30,1), justification='c', background_color="#54C5C9",
                 text_color='black', font=('Arial', 30, 'bold'))],
        [sg.Button('Exit')]
    ]
    return sg.Window('Orders', layout, finalize=True)


def make_window_4():
    pass


def main():
    # Design pattern 1 - First window does not remain active
    # window2 = None
    # window1 = make_window1()

    window1, window2, window3 = make_window1(), None, None

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == window1:
            break

        if event == 'Customers' and not window2:
            window1.hide()
            window2 = make_window2()

        if window == window2 and (event in (sg.WIN_CLOSED, 'Exit')):
            window2.close()
            window2 = None
            window1.un_hide()
    window1.close()


if __name__ == '__main__':
    main()
