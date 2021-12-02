import PySimpleGUI as sg
from variables import *
from temp_functions import *
from main_menu import *
from customer_windows import *
from order_windows import *
from inventory_windows import *

'''
Main window for the GUI, containing the Event-handler-loop.
In order to run the GUI, run this file.

Variables = edit settings for the windows and buttons. (Fonts etc.)
'''


def event_handler():
    # Windows:
    main_screen, customer_screen, orders_screen, inventory_screen, add_customer_screen, remove_customer_screen = \
        main_menu(), None, None, None, None, None

    # Event handler loop
    while True:
        # prepare all windows
        window, event, values = sg.read_all_windows()

        # Closing main screen
        if event == sg.WIN_CLOSED or None and window == main_screen:
            break

        # Customers - button
        if event == 'Customers' and not customer_screen:
            main_screen.hide()
            customer_screen = customer_window()

        # Orders - button
        if event == 'Orders' and not orders_screen:
            main_screen.hide()
            orders_screen = orders_window()

        # Inventory - button
        if event == 'Inventory' and not inventory_screen:
            main_screen.hide()
            inventory_screen = inventory_window()

        # Customer Screen buttons
        if window == customer_screen:
            if event in (sg.Button, 'Add Customer'):
                customer_screen.close()
                add_customer_screen = add_customer_window()

            if event == '-TABLE-DOUBLE-CLICK-':
                column = values[event]
                print(f'Click on column {column}')
                customer_screen.close()
                customer_screen = customer_window()

            elif event in (sg.Button, 'Remove Customer'):
                customer_screen.close()
                remove_customer_screen = remove_customer_window()

        # ADD CUSTOMER SCREEN
        if window == add_customer_screen:

            # Add Customer
            if event in (sg.Button, '-ADD-'):
                output = [str(values[key]) for key in values]
                data.append(output)
                add_customer_screen.close()
                customer_screen = customer_window()
                add_customer_screen = None
            # Cancel
            elif event in (sg.Button, 'Cancel'):
                customer_screen = customer_window()
                add_customer_screen.close()
                add_customer_screen = None

        # REMOVE CUSTOMER WINDOW
        if window == remove_customer_screen:
            if event in (sg.Button, 'Remove Customer'):
                selection = int(values['customer_id'])
                remove_customer(selection)
                customer_screen = customer_window()
                remove_customer_screen.close()
                remove_customer_screen = None

            elif event in (sg.Button, 'Cancel'):
                customer_screen = customer_window()
                remove_customer_screen.close()
                remove_customer_screen = None

        if window == inventory_screen:
            if event in (sg.Button, "Back"):
                main_screen.un_hide()
                inventory_screen.close()
                inventory_screen = None


if __name__ == '__main__':
    event_handler()
