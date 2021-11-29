import PySimpleGUI as sg
from variables import *

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
    main_screen, customer_screen, orders_screen, inventory_screen, add_customer_screen = \
        main_menu(), None, None, None, None

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

        # Add Customer - button
        if window == customer_screen and (event in (sg.Button, 'Add Customer')):
            add_customer_window()
            customer_screen.close()
            customer_screen = customer_window()


if __name__ == '__main__':
    event_handler()
